import sys
import inspect
import hiwonder.Board as Board
import hiwonder.PWMServo as PWM
import hiwonder.Mpu6050 as Mpu6050
import pigpio

########################################
### A Note to Students
########################################
'''
As a matter of convention, variables and functions beginning with a single 
underscore such as _init_flag or _intern_read_body_devs() should not be accessed
by you directly.

Python does not have a defined way for doing private variables, so the
single underscore indicates that you should not be accessing these items from
an external file.

If you have any problems with this code, please reach out to the TA so we can 
try to troubleshoot them as quickly as possible. It's possible that some of the
functions don't work exactly as expected, so we will need to update the code for
all students.
'''


################################################################################
### Private Data
################################################################################

# Global flags
_init_flag = False
_safe_mode = True

# Data structures for motor info
_body_names = {}
_body_resets = {}
_body_pos = {}
_body_devs = {}
_body_lims = {}
_body_power = {}
_body_temp = {}
_body_max_temp = {}
_body_volt = {}
_body_volt_lims = {}

# Data structures for the head motors
_head_names = {}
_head_objs = {}
_head_resets = {}
_head_pos = {}
_head_lims = {}

# Data structures for the MPU-6050 sensor
# This is the accelerometer + gyroscope combo
_mpu = None
_mpu_acc = {}
_mpu_gyro = {}
_mpu_temp = 0


################################################################################
### Public Data
################################################################################

# Individual body joint IDs
BODY_LSHO = 8   # Left shoulder
BODY_LUPA = 7   # Left upper arm
BODY_LELB = 6   # Left elbow
BODY_LHAN = 17  # Left hand
BODY_RSHO = 16  # Right shoulder
BODY_RUPA = 15  # Right upper arm
BODY_RELB = 14  # Right elbow
BODY_RHAN = 18  # Right hand
BODY_LHIP = 5   # Left hip
BODY_LTHI = 4   # Left thigh
BODY_LKNE = 3   # Left knee
BODY_LSHI = 2   # Left shin
BODY_LANK = 1   # Left ankle
BODY_RHIP = 13  # Right hip
BODY_RTHI = 12  # Right thigh
BODY_RKNE = 11  # Right knee
BODY_RSHI = 10  # Right shin
BODY_RANK = 9   # Right ankle

# All body joint IDs
ALL_BODY = [BODY_LSHO, BODY_LUPA, BODY_LELB, BODY_LHAN,
            BODY_RSHO, BODY_RUPA, BODY_RELB, BODY_RHAN,
            BODY_LHIP, BODY_LTHI, BODY_LKNE, BODY_LSHI, BODY_LANK,
            BODY_RHIP, BODY_RTHI, BODY_RKNE, BODY_RSHI, BODY_RANK]

# Individual head joint IDs
HEAD_UD = -1
HEAD_LR = -2

# All head joint IDs
ALL_HEAD = [HEAD_UD, HEAD_LR]


################################################################################
### Private Helper Functions
###     Do not directly use these
################################################################################

########################################
### Safety checks
########################################

# Check initialization status, terminate if uninitialized
def _check_init_status():
    if not _init_flag:
        sys.exit("Failure to call initialization function, terminating execution")

# Check safe mode status, terminate if enabled
def _check_safe_mode():
    if _safe_mode:
        sys.exit("-------- Safe mode enabled, terminating execution")


########################################
### Body Servos
########################################

# Populate dict of all body names
def _init_body_names():
    _body_names[BODY_LSHO] = "BODY_LSHO"
    _body_names[BODY_LUPA] = "BODY_LUPA"
    _body_names[BODY_LELB] = "BODY_LELB"
    _body_names[BODY_LHAN] = "BODY_LHAN"
    _body_names[BODY_RSHO] = "BODY_RSHO"
    _body_names[BODY_RUPA] = "BODY_RUPA"
    _body_names[BODY_RELB] = "BODY_RELB"
    _body_names[BODY_RHAN] = "BODY_RHAN"
    _body_names[BODY_LHIP] = "BODY_LHIP"
    _body_names[BODY_LTHI] = "BODY_LTHI"
    _body_names[BODY_LKNE] = "BODY_LKNE"
    _body_names[BODY_LSHI] = "BODY_LSHI"
    _body_names[BODY_LANK] = "BODY_LANK"
    _body_names[BODY_RHIP] = "BODY_RHIP"
    _body_names[BODY_RTHI] = "BODY_RTHI"
    _body_names[BODY_RKNE] = "BODY_RKNE"
    _body_names[BODY_RSHI] = "BODY_RSHI"
    _body_names[BODY_RANK] = "BODY_RANK"

# Populate dict of all body reset positions
def _init_body_resets():
    _body_resets[BODY_LSHO] = 688
    _body_resets[BODY_LUPA] = 775
    _body_resets[BODY_LELB] = 575
    _body_resets[BODY_LHAN] = 500
    _body_resets[BODY_RSHO] = 312
    _body_resets[BODY_RUPA] = 225
    _body_resets[BODY_RELB] = 425
    _body_resets[BODY_RHAN] = 500
    _body_resets[BODY_LHIP] = 500
    _body_resets[BODY_LTHI] = 575
    _body_resets[BODY_LKNE] = 500
    _body_resets[BODY_LSHI] = 390
    _body_resets[BODY_LANK] = 500
    _body_resets[BODY_RHIP] = 500
    _body_resets[BODY_RTHI] = 425
    _body_resets[BODY_RKNE] = 500
    _body_resets[BODY_RSHI] = 610
    _body_resets[BODY_RANK] = 500

# Populate dict of all body servo deviations
def _init_body_devs():
    for joint in ALL_BODY:
        temp_dev = None
        while temp_dev is None:
            #print("Servo deviation failure... retrying...")
            temp_dev = Board.getBusServoDeviation(joint)
        if temp_dev > 127:
            temp_dev = temp_dev - 256
        _body_devs[joint] = temp_dev

# Populate dict of all body servo limits
def _init_body_lims():
    for joint in ALL_BODY:
        _body_lims[joint] = Board.getBusServoAngleLimit(joint)

# Populate dict of all body servo max temperatures
def _init_body_max_temps():
    for joint in ALL_BODY:
        _body_max_temp[joint] = Board.getBusServoTempLimit(joint)

# Populate dict of all body servo max voltages
def _init_body_volt_lims():
    for joint in ALL_BODY:
        _body_volt_lims[joint] = Board.getBusServoVinLimit(joint)

# Populate dict of all body servo positions
def _populate_body_pos():
    for joint in ALL_BODY:
        _body_pos[joint] = Board.getBusServoPulse(joint)

# Populate dict of all body servo power statuses
def _populate_body_power():
    for joint in ALL_BODY:
        _body_power[joint] = bool(Board.getBusServoLoadStatus(joint))

# Populate dict of all body servo temperatures
def _populate_body_temps():
    for joint in ALL_BODY:
        _body_temp[joint] = Board.getBusServoTemp(joint)

# Populate dict of all body servo voltages
def _populate_body_volt():
    for joint in ALL_BODY:
        _body_volt[joint] = Board.getBusServoVin(joint)

# Check validity of a provided body timing
def _is_valid_body_timing(timing):
    if timing < 0:
        print("WARNING: Negative timing ({}) passed to {}() at line {} of {}".format(timing, inspect.stack()[1][3], inspect.stack()[2][2], inspect.stack()[2][1]))
        print("-------- Body servo timing must be nonnegative")
        return False
    if timing > 30000:
        print("WARNING: Excessive timing ({}) passed to {}() at line {} of {}".format(timing, inspect.stack()[1][3], inspect.stack()[2][2], inspect.stack()[2][1]))
        print("-------- Body servo timing must be less than 30000 (30 seconds)")
        return False
    return True

# Check validity of a provided body position
def _is_valid_body_pos(id, pos):
    if pos < _body_lims[id][0] or pos > _body_lims[id][1]:
        print("WARNING: Out of bounds value {} for servo {} passed to {}() at line {} of {}". format(pos, _body_names[id], inspect.stack()[1][3], inspect.stack()[2][2], inspect.stack()[2][1]))
        print("-------- Value must be on range [{}, {}]".format(_body_lims[id][0], _body_lims[id][1]))
        return False
    return True


########################################
### Head Servos
########################################

# Populate dict of all head servo resets
def _init_head_names():
    _head_names[HEAD_UD] = "HEAD_UD"
    _head_names[HEAD_LR] = "HEAD_LR"

# Initialize the head servo objects
def _init_head_objs():
    pi = pigpio.pi()
    for joint in ALL_HEAD:
        _head_objs[joint] = PWM.PWM_Servo(pi, 11 - joint, deviation=0, control_speed=True)

# Populate dict of all head servo resets
def _init_head_resets():
    _head_resets[HEAD_UD] = 1500
    _head_resets[HEAD_LR] = 1500

# Populate dict of all head servo limits
def _init_head_lims():
    for joint in ALL_HEAD:
        _head_lims[joint] = (500, 2500)

# Populate dict of all head servo positions
def _populate_head_pos():
    for joint in ALL_HEAD:
        _head_pos[joint] = _head_objs[joint].getPosition()

# Check validity of head timing
def _is_valid_head_timing(timing):
    if timing < 20:
        print("WARNING: Insufficient timing ({}) passed to {}() at line {} of {}".format(timing, inspect.stack()[1][3], inspect.stack()[2][2], inspect.stack()[2][1]))
        print("-------- Head servo timing must be greater than 20 (0.02 seconds)")
        return False
    if timing > 30000:
        print("WARNING: Excessive timing ({}) passed to {}() at line {} of {}".format(timing, inspect.stack()[1][3], inspect.stack()[2][2], inspect.stack()[2][1]))
        print("-------- Head servo timing must be less than 30000 (30 seconds)")
        return False
    return True

# Check validity of a provided head position
def _is_valid_head_pos(id, pos):
    if pos < _head_lims[id][0] or pos > _head_lims[id][1]:
        print("WARNING: Out of bounds value {} for servo {} passed to {}() at line {} of {}". format(pos, _head_names[id], inspect.stack()[1][3], inspect.stack()[2][2], inspect.stack()[2][1]))
        print("-------- Value must be on range [{}, {}]".format(_head_lims[id][0], _head_lims[id][1]))
        return False
    return True


########################################
### MPU-6050 Sensor
########################################

# Populate all the MPU-6050 data
def _init_mpu_data():
    acc, gyro, temp = _mpu.get_all_data()
    _mpu_acc['x'] = acc['x']
    _mpu_acc['y'] = acc['y']
    _mpu_acc['z'] = acc['z']
    _mpu_gyro['x'] = gyro['x']
    _mpu_gyro['y'] = gyro['y']
    _mpu_gyro['z'] = gyro['z']
    global _mpu_temp
    _mpu_temp = temp


################################################################################
### Public Helper Functions
###     These are the functions that you should be using directly
################################################################################

########################################
### Initialization
########################################

# Initialize all the robot data
#     This function MUST be called at the start of a program
def init_robot_data(safe_mode=True, swap_hands=False):
    # Notify user of initialization
    print("Beginning initialization")

    # Swap hands if needed
    global BODY_LHAN
    global BODY_RHAN
    if swap_hands:
        BODY_LHAN = 17
        BODY_RHAN = 18
    else:
        BODY_LHAN = 18
        BODY_RHAN = 17

    # Initialize body servos
    _init_body_names()
    _init_body_resets()
    _init_body_devs()
    _init_body_lims()
    _init_body_max_temps()
    _init_body_volt_lims()
    _populate_body_pos()
    _populate_body_power()
    _populate_body_temps()
    _populate_body_volt()

    # Initialize head servos
    _init_head_names()
    _init_head_objs()
    _init_head_resets()
    _init_head_lims()
    _populate_head_pos()

    # Initialize the MPU-6050 sensor
    global _mpu
    _mpu = Mpu6050.mpu6050(0x68)
    _mpu.set_gyro_range(_mpu.GYRO_RANGE_2000DEG)
    _mpu.set_accel_range(_mpu.ACCEL_RANGE_2G)
    _init_mpu_data()

    # Set the initialization flag
    global _init_flag
    _init_flag = True

    # Set the safe mode
    global _safe_mode
    _safe_mode = safe_mode

    # Notify user that initialization is done
    print("Initialization complete")


########################################
### Get Body Servo Data
########################################

# Get body servo position(s) based on ID(s)
def get_body_pos(id=None): 
    # Initialization check
    _check_init_status()

    # Case: No input provided
    # Return: Dict of body positions
    if id is None:
        _populate_body_pos()
        return _body_pos.copy()

    # Case: Input is a single ID value
    # Return: Single position value
    if isinstance(id, int):
        # Case: Input ID is valid
        # Return: Current position of body servo
        if id in ALL_BODY:
            _body_pos[id] = Board.getBusServoPulse(id)
            return _body_pos[id]
        # Case: Input ID is invalid
        # Return: None
        print("WARNING: Invalid single ID ({}) passed to {}() at line {} of {}".format(id, inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][1]))
        _check_safe_mode()
        print("-------- Returning None")
        return None

    # Case: Input is a list of ID values
    # Return: List with body servo position values
    if isinstance(id, list):
        # Create temporary storage
        ret_vals = []
        invalid = []
        # Iterate over all provided IDs
        for x in range(len(id)):
            # Case: ID at index x is valid
            if id[x] in ALL_BODY:
                _body_pos[id[x]] = Board.getBusServoPulse(id[x])
                ret_vals.append(_body_pos[id[x]])
            # Case: ID at index x is invalid
            else:
                ret_vals.append(None)
                invalid.append((x, id[x]))
        # If there are any invalid IDs, warn user
        if invalid:
            print("WARNING: Invalid ID in list passed to {}() at line {} of {}".format(inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][1]))
            _check_safe_mode()
            print("-------- Placing None at their indices and returning")
            for x in invalid:
                print("-------- Index: {:2d}, Value: {:2d} --> None".format(x[0], x[1]))
        # Now return
        return ret_vals


########################################
### Display Body Servo Data
########################################

# Get body servo position(s) based on ID(s)
def print_body_data(id=None, positions=True, temps=True, volts=True, verbose=False): 
    # Initialization check
    _check_init_status()
    
    # Update everything
    _populate_body_pos()
    _populate_body_temps()
    _populate_body_volt()

    # Populate lists of servos
    servo_list_in = []
    if id is None:
        servo_list_in = ALL_BODY
    elif isinstance(id, int):
        servo_list_in.append(id)
    elif isinstance(id, list):
        servo_list_in = id

    # Remove all invalid joints
    for i in range(len(servo_list_in)):
        if servo_list_in[i] not in ALL_BODY:
            # Print messages for all invalid servos
            print("WARNING: Invalid  ID ({}) passed to {}() at line {} of {}".format(id, inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][1]))
            _check_safe_mode()
            print("-------- Removing {} from list".format(servo_list_in[i]))
    servo_list = [i for i in servo_list_in if i in ALL_BODY]
    print()

    # Display servo info
    if positions:
        # Verbose: Name | ID | Position | Min | Max | Default | Deviation | Power 
        if verbose:
            print("----------------------------------------------------------------------")
            print("Position info")
            print("----------------------------------------------------------------------")
            print("   Name   | ID | Position | Min. | Max. | Default | Deviation | Power ")
            print("----------|----|----------|------|------|---------|-----------|-------")
            for servo in servo_list:
                print("{:^} | {:>2d} |   {:>4d}   | {:>4d} | {:>4d} |   {:>4d}  |    {:> 4d}   | {:>5}".format(_body_names[servo], servo, _body_pos[servo], _body_lims[servo][0], _body_lims[servo][1], _body_resets[servo], _body_devs[servo], str(_body_power[servo])))
        # Not verbose: Name | Position | Default
        else:
            print("-------------------------------")
            print("Position info")
            print("-------------------------------")
            print("   Name   | Position | Default ")
            print("----------|----------|---------")
            for servo in servo_list:
                print("{:^} |   {:>4d}   |   {:>4d}".format(_body_names[servo], _body_pos[servo], _body_resets[servo]))
        # Add a space
        print()

    # Display temp info   
    if temps:
        # Verbose: Name | ID | Temp | Max
        if verbose:
            print("-----------------------------")
            print("Temperature info")
            print("-----------------------------")
            print("   Name   | ID | Cur. | Max.")
            print("----------|----|------|------")
            for servo in servo_list:
                print("{:^} | {:>2d} | {:>2d}".format(_body_names[servo], servo, _body_temp[servo]) + u"\N{DEGREE SIGN}" + "C | {:>2d}".format(_body_max_temp[servo]) + u"\N{DEGREE SIGN}" + "C")
        # Not verbose: Name | Temp
        else:
            print("-----------------")
            print("Temperature info")
            print("-----------------")
            print("   Name   | Cur. ")
            print("----------|------")
            for servo in servo_list:
                print("{:^} | {:>2d}".format(_body_names[servo], _body_temp[servo]) + u"\N{DEGREE SIGN}" + "C")
        # Add a space
        print()

    # Display voltage info
    if volts:
        # Verbose: Name | ID | Voltage | Min | Max
        if verbose:
            print("------------------------------------------")
            print("Voltage info")
            print("------------------------------------------")
            print("   Name   | ID |  Cur.  |  Min.  |  Max.  ")
            print("----------|----|--------|--------|--------")
            for servo in servo_list:
                 print("{:^} | {:>2d} | {:>5.2f}V | {:>5.2f}V | {:>5.2f}V".format(_body_names[servo], servo, _body_volt[servo]/1000, _body_volt_lims[servo][0]/1000, _body_volt_lims[servo][1]/1000))
        # Not verbose: Name | Voltage
        else:
            print("-------------------")
            print("Voltage info")
            print("-------------------")
            print("   Name   |  Cur.  ")
            print("----------|--------")
            for servo in servo_list:
                 print("{:^} | {:>5.2f}V".format(_body_names[servo], _body_volt[servo]/1000))
        # Add a space
        print()
        

########################################
### Set Body Servo Data
########################################

# Set body servo position to specified values
def set_body_pos(id, value=None, timing=None):
    # Initialization check
    _check_init_status()
    
    # Check to make sure the ID is valid
    if id not in ALL_BODY:
        print("WARNING: Invalid ID ({}) passed to {}() at line {} of {}".format(id, inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][1]))
        _check_safe_mode()
        print("-------- Skipping function execution")
        return

    # Case: No value is provided
    if value is None:
        # If no timing is provided, use 750ms, otherwise validate
        if timing is None:
            timing = 750
        else:
            if not _is_valid_body_timing(timing):
                _check_safe_mode()
                print("-------- Skipping function execution")
                return
        # Reset the servo to default position and return
        Board.setBusServoPulse(id, _body_resets[id], timing)
        return

    # Case: Out of bounds value
    if not _is_valid_body_pos(id, value):
        _check_safe_mode()
        print("-------- Skipping function execution")
        return

    # Check parameters, require timing if value is present
    if timing is None and value is not None:
        print("WARNING: No timing provided to {}() at line {} of {}".format(inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][1]))
        print("-------- Parameter timing is required when parameter value is present")
        _check_safe_mode()
        print("-------- Skipping function execution")
        return

    # Validate timing before continuing
    if not _is_valid_body_timing(timing):
        _check_safe_mode()
        print("-------- Skipping function execution")
        return

    # If everything is valid, run the motion
    Board.setBusServoPulse(id, value, timing)

# Reset all joints in the body
def reset_all_body(timing=None):
    # Initialization check
    _check_init_status()

    # If no timing is provided, use 750ms, otherwise validate
    if timing is None:
        timing = 750
    else:
        if not _is_valid_body_timing(timing):
            _check_safe_mode()
            print("-------- Skipping function execution")
            return

    # Reset all the body joints
    for id in ALL_BODY:
        Board.setBusServoPulse(id, _body_resets[id], timing)

# Set body servo position to specified values
def body_power_off(id=None):
    # Initialization check
    _check_init_status()

    # Populate lists of servos
    servo_list_in = []
    if id is None:
        servo_list_in = ALL_BODY
    elif isinstance(id, int):
        servo_list_in.append(id)
    elif isinstance(id, list):
        servo_list_in = id

    # Remove all invalid joints
    for i in range(len(servo_list_in)):
        if servo_list_in[i] not in ALL_BODY:
            # Print messages for all invalid servos
            print("WARNING: Invalid  ID ({}) passed to {}() at line {} of {}".format(id, inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][1]))
            _check_safe_mode()
            print("-------- Removing {} from list".format(servo_list_in[i]))
    servo_list = [i for i in servo_list_in if i in ALL_BODY]

    # Shut down listed servos
    for servo in servo_list:
        Board.unloadBusServo(servo)
    

########################################
### Get Head Servo Data
########################################

# Get head servo position(s) based on ID(s)
def get_head_pos(id=None): 
    # Initialization check
    _check_init_status()

    # Case: No input provided
    # Return: Dict of head positions
    if id is None:
        _populate_head_pos()
        return _head_pos.copy()

    # Case: Input is a single ID value
    # Return: Single ID value
    if isinstance(id, int):
        # Case: Input ID is valid
        # Return: Current position of head servo
        if id in ALL_HEAD:
            _head_pos[id] = _head_objs[id].getPosition()
            return _head_pos[id]
        # Case: Input ID is invalid
        # Return: None
        print("WARNING: Invalid single ID ({}) passed to {}() at line {} of {}".format(id, inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][1]))
        _check_safe_mode()
        print("-------- Returning None")
        return None

    # Case: Input is a list of ID values
    # Return: List with head servo position values
    if isinstance(id, list):
        # Create temporary storage
        ret_vals = []
        invalid = []
        # Iterate over all provided IDs
        for x in range(len(id)):
            # Case: ID at index x is valid
            if id[x] in ALL_HEAD:
                _head_pos[id[x]] = _head_objs[id[x]].getPosition()
                ret_vals.append(_head_pos[id[x]])
            # Case: ID at index x is invalid
            else:
                ret_vals.append(None)
                invalid.append((x, id[x]))
        # If there are any invalid IDs, warn user
        if invalid:
            print("WARNING: Invalid ID in list passed to {}() at line {} of {}".format(inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][1]))
            _check_safe_mode()
            print("-------- Placing None at their indices")
            for x in invalid:
                print("-------- Index: {:2d}, Value: {:2d} --> None".format(x[0], x[1]))
        # Now return
        return ret_vals


########################################
### Set Head Servo Data
########################################

# Set head servo position to specified values
def set_head_pos(id, value=None, timing=None):
    # Initialization check
    _check_init_status()
    
    # Check to make sure the ID is valid
    if id not in ALL_HEAD:
        print("WARNING: Invalid ID ({}) passed to {}() at line {} of {}".format(id, inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][1]))
        _check_safe_mode()
        print("-------- Skipping function execution")
        return

    # Case: No value is provided
    if value is None:
        # If no timing is provided, use 750ms, otherwise validate
        if timing is None:
            timing = 750
        else:
            if not _is_valid_head_timing(timing):
                _check_safe_mode()
                print("-------- Skipping function execution")
                return
        # Reset the servo to default position and return
        Board.setPWMServoPulse(-id, _head_resets[id], timing)
        return

    # Case: Out of bounds value
    if not _is_valid_head_pos(id, value):
        _check_safe_mode()
        print("-------- Skipping function execution")
        return

    # Check parameters, require timing if value is present
    if timing is None and value is not None:
        print("WARNING: No timing provided to {}() at line {} of {}".format(inspect.stack()[0][3], inspect.stack()[1][2], inspect.stack()[1][1]))
        print("-------- Parameter timing is required when parameter value is present")
        _check_safe_mode()
        print("-------- Skipping function execution")
        return

    # Validate timing before continuing
    if not _is_valid_head_timing(timing):
        _check_safe_mode()
        print("-------- Skipping function execution")
        return

    # If everything is valid, run the motion
    Board.setPWMServoPulse(-id, value, timing)

# Reset all joints in the head
def reset_all_head(timing=None):
    # Initialization check
    _check_init_status()

    # If no timing is provided, use 750ms, otherwise validate
    if timing is None:
        timing = 750
    else:
        if not _is_valid_head_timing(timing):
            _check_safe_mode()
            print("-------- Skipping function execution")
            return

    # Reset all the body joints
    for id in ALL_HEAD:
        Board.setPWMServoPulse(-id, _head_resets[id], timing)


########################################
### Get MPU-6050 Sensor Data
########################################

# Get accelerometer data
def get_mpu_acc():
    acc = _mpu.get_accel_data()
    (x, y, z) = (acc['x'], acc['y'], acc['z'])
    _mpu_acc['x'] = x
    _mpu_acc['y'] = y
    _mpu_acc['z'] = z
    return (x, y, z)

# Get gyroscope data
def get_mpu_gyro():
    gyro = _mpu.get_gyro_data()
    (x, y, z) = (gyro['x'], gyro['y'], gyro['z'])
    _mpu_gyro['x'] = x
    _mpu_gyro['y'] = y
    _mpu_gyro['z'] = z
    return (x, y, z)

# Get temperature data
def get_mpu_temp():
    global _mpu_temp
    _mpu_temp = _mpu.get_temp()
    return _mpu_temp