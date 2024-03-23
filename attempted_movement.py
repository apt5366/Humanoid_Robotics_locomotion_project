import time
from helper_utils import *

########################################
### Define some actions
########################################



def stacking_cubes():
    set_body_pos(BODY_LSHO, 831, 750)
    set_body_pos(BODY_LUPA, 524, 750)
    set_body_pos(BODY_RSHO, 183, 750)
    set_body_pos(BODY_RUPA, 515, 750)
    time.sleep(1.5)
    
    set_body_pos(BODY_LSHO, 336, 750)
    set_body_pos(BODY_RSHO, 664, 750)
    time.sleep(1.5)
    
    set_body_pos(BODY_RUPA, 28, 750)
    time.sleep(1.5)
    
    set_body_pos(BODY_LSHO, 444, 750)
    set_body_pos(BODY_LUPA, 862, 750)
    set_body_pos(BODY_LELB, 568, 750)
    set_body_pos(BODY_RHAN, 498, 750)
    
    set_body_pos(BODY_RSHO, 539, 750)
    set_body_pos(BODY_RUPA, 31, 750)
    set_body_pos(BODY_RELB, 372, 750)
    set_body_pos(BODY_LHAN, 500, 750)
    
    time.sleep(0.75)
    
def walk_one_step():
    set_body_pos(BODY_RHIP, 525, 1500)
    set_body_pos(BODY_RTHI, 391, 1500)
    set_body_pos(BODY_RKNE, 362, 1500)
    set_body_pos(BODY_RSHI, 739, 1500)
    set_body_pos(BODY_LHIP, 506, 1500)
    set_body_pos(BODY_LTHI, 847, 1500)
    set_body_pos(BODY_LKNE, 704, 1500)
    set_body_pos(BODY_LSHI, 328, 1500)
    set_body_pos(BODY_LANK, 496, 1500)
    time.sleep(1.5)
   
    
# Nod head as if saying "yes"
def nod():
    # Reset head height
    set_head_pos(HEAD_UD, timing=100)
    time.sleep(0.1)
    # Nod a few times
    set_head_pos(HEAD_UD, 1700, 200)
    time.sleep(0.2)
    set_head_pos(HEAD_UD, 1300, 200)
    time.sleep(0.2)
    set_head_pos(HEAD_UD, 1700, 200)
    time.sleep(0.2)
    set_head_pos(HEAD_UD, 1300, 200)
    time.sleep(0.2)
    set_head_pos(HEAD_UD, 1700, 200)
    time.sleep(0.2)
    # Reset head height
    set_head_pos(HEAD_UD, timing=100)
    time.sleep(0.1)

# Shake head as if saying "no"
def shake():
    # Make head face forward
    set_head_pos(HEAD_LR, timing=100)
    time.sleep(0.1)
    # Shake a few times
    set_head_pos(HEAD_LR, 1700, 200)
    time.sleep(0.2)
    set_head_pos(HEAD_LR, 1300, 200)
    time.sleep(0.2)
    set_head_pos(HEAD_LR, 1700, 200)
    time.sleep(0.2)
    set_head_pos(HEAD_LR, 1300, 200)
    time.sleep(0.2)
    set_head_pos(HEAD_LR, 1700, 200)
    time.sleep(0.2)
    # Make head face forward
    set_head_pos(HEAD_LR, timing=100)
    time.sleep(0.1)

# Wave left arm as if saying "hello"
def wave_left():
    # Raise arm
    set_body_pos(BODY_LSHO, 50, 750)
    set_body_pos(BODY_LUPA, 900, 750)
    set_body_pos(BODY_LELB, 500, 750)
    time.sleep(0.75)
    # Wave a few times
    set_body_pos(BODY_LUPA, 750, 400)
    time.sleep(0.4)
    set_body_pos(BODY_LUPA, 900, 400)
    time.sleep(0.4)
    set_body_pos(BODY_LUPA, 750, 400)
    time.sleep(0.4)
    set_body_pos(BODY_LUPA, 900, 400)
    time.sleep(0.4)
    set_body_pos(BODY_LUPA, 750, 400)
    time.sleep(0.4)
    set_body_pos(BODY_LUPA, 900, 400)
    time.sleep(0.4)
    # Reset the arm
    set_body_pos(BODY_LSHO)
    set_body_pos(BODY_LUPA)
    set_body_pos(BODY_LELB)
    time.sleep(0.75)
    

# Wave right arm as if saying "hello"
def wave_right():
    # Raise arm
    set_body_pos(BODY_RSHO, 950, 750)
    set_body_pos(BODY_RUPA, 100, 750)
    set_body_pos(BODY_RELB, 500, 750)
    time.sleep(0.75)
    # Wave a few times
    set_body_pos(BODY_RUPA, 250, 400)
    time.sleep(0.4)
    set_body_pos(BODY_RUPA, 100, 400)
    time.sleep(0.4)
    set_body_pos(BODY_RUPA, 250, 400)
    time.sleep(0.4)
    set_body_pos(BODY_RUPA, 100, 400)
    time.sleep(0.4)
    set_body_pos(BODY_RUPA, 250, 400)
    time.sleep(0.4)
    set_body_pos(BODY_RUPA, 100, 400)
    time.sleep(0.4)
    # Reset the arm
    set_body_pos(BODY_RSHO)
    set_body_pos(BODY_RUPA)
    set_body_pos(BODY_RELB)
    time.sleep(0.75)

# Squat down a small bit and then stand back up
def squat():
    # Squat down
    set_body_pos(BODY_LTHI, 675, 1500)
    set_body_pos(BODY_LKNE, 750, 1500)
    set_body_pos(BODY_LSHI, 250, 1500)
    set_body_pos(BODY_RTHI, 325, 1500)
    set_body_pos(BODY_RKNE, 250, 1500)
    set_body_pos(BODY_RSHI, 750, 1500)
    time.sleep(1.5)
    # Stay there for a short time
    time.sleep(0.75)
    # Reverse the motion
    set_body_pos(BODY_LTHI, timing=1500)
    set_body_pos(BODY_LKNE, timing=1500)
    set_body_pos(BODY_LSHI, timing=1500)
    set_body_pos(BODY_RTHI, timing=1500)
    set_body_pos(BODY_RKNE, timing=1500)
    set_body_pos(BODY_RSHI, timing=1500)
    time.sleep(1.5)

# Squat down a lot and then stand back up
def deepsquat():
    # Squat down
    set_body_pos(BODY_LTHI, 775, 1000)
    set_body_pos(BODY_LKNE, 950, 1000)
    set_body_pos(BODY_LSHI, 150, 1000)
    set_body_pos(BODY_RTHI, 225, 1000)
    set_body_pos(BODY_RKNE,  50, 1000)
    set_body_pos(BODY_RSHI, 850, 1000)
    time.sleep(1.0)
    # Stay there for a short time
    time.sleep(0.75)
    # Reverse the motion
    set_body_pos(BODY_LTHI, timing=1000)
    set_body_pos(BODY_LKNE, timing=1000)
    set_body_pos(BODY_LSHI, timing=1000)
    set_body_pos(BODY_RTHI, timing=1000)
    set_body_pos(BODY_RKNE, timing=1000)
    set_body_pos(BODY_RSHI, timing=1000)
    time.sleep(1.0)


########################################
### The main code
########################################

# Initialize the data
init_robot_data()

# # Reset the body and head servos
reset_all_body()
reset_all_head()
time.sleep(1.0)

stacking_cubes()
time.sleep(1.0)



# walk_one_step()
# time.sleep(1.0)

# Print all body servo information
print_body_data(verbose=True)

# Turn off the body servos
body_power_off()
