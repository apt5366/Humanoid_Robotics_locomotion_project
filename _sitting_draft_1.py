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
    
    set_body_pos(BODY_LSHO, 474, 750)
    set_body_pos(BODY_LUPA, 741, 750)
    set_body_pos(BODY_LELB, 767, 750)
    set_body_pos(BODY_RHAN, 498, 750)
    
    set_body_pos(BODY_RSHO, 517, 750)
    set_body_pos(BODY_RUPA, 40, 750)
    set_body_pos(BODY_RELB, 331, 750)
    set_body_pos(BODY_LHAN, 501, 750)
    
    time.sleep(0.75)
    
def walk_one_step():
    set_body_pos(BODY_LHIP, 502, 1500)
    set_body_pos(BODY_LTHI, 692, 1500)
    set_body_pos(BODY_LKNE, 674, 1500)
    set_body_pos(BODY_LSHI, 156, 1500)
    set_body_pos(BODY_LANK, 493, 1500)
    set_body_pos(BODY_RHIP, 514, 1500)
    set_body_pos(BODY_RTHI, 411, 1500)
    set_body_pos(BODY_RKNE, 471, 1500)
    set_body_pos(BODY_RSHI, 610, 1500)
    set_body_pos(BODY_RANK, 519, 1500)
    
    time.sleep(1.5)
   
   
def sitting_down():
    set_body_pos(BODY_LHIP, 479, 1500)
    set_body_pos(BODY_LTHI, 852, 1500)
    set_body_pos(BODY_LKNE, 943, 1500)
    set_body_pos(BODY_LSHI, 224, 1500)
    set_body_pos(BODY_LANK, 495, 1500)
    set_body_pos(BODY_RHIP, 500, 1500)
    set_body_pos(BODY_RTHI, 155, 1500)
    set_body_pos(BODY_RKNE, 60, 1500)
    set_body_pos(BODY_RSHI, 789, 1500)
    set_body_pos(BODY_RANK, 503, 1500)
    
    time.sleep(1.5)
     
    set_body_pos(BODY_LSHO, 944, 750)
    set_body_pos(BODY_RSHO, 39, 750)
     
    time.sleep(1.5)
    
    set_body_pos(BODY_LSHI, 363, 1500)
    set_body_pos(BODY_RSHI, 625, 1500)
    time.sleep(1.5)
    
    set_body_pos(BODY_LHIP, 478, 1500)
    set_body_pos(BODY_LTHI, 723, 1500)
    set_body_pos(BODY_LKNE, 868, 1500)
    set_body_pos(BODY_LSHI, 367, 1500)
    set_body_pos(BODY_LANK, 500, 1500)
    set_body_pos(BODY_RHIP, 498, 1500)
    set_body_pos(BODY_RTHI, 144, 1500)
    set_body_pos(BODY_RKNE, 86, 1500)
    set_body_pos(BODY_RSHI, 721, 1500)
    set_body_pos(BODY_RANK, 539, 1500)
    time.sleep(1.5)
    
    set_body_pos(BODY_RHIP, 498, 1500)
    set_body_pos(BODY_RTHI, 149, 1500)
    set_body_pos(BODY_RKNE, 97, 1500)
    set_body_pos(BODY_RSHI, 842, 1500)
    set_body_pos(BODY_RANK, 538, 1500)
    time.sleep(1.5)
    
    set_body_pos(BODY_RHIP, 461, 1500)
    set_body_pos(BODY_RTHI, 523, 1500)
    set_body_pos(BODY_RKNE, 803, 1500)
    set_body_pos(BODY_RSHI, 422, 1500)
    set_body_pos(BODY_RANK, 508, 1500)
    time.sleep(1.5)
    
    set_body_pos(BODY_LHIP, 454, 1500)
    set_body_pos(BODY_LTHI, 853, 1500)
    set_body_pos(BODY_LKNE, 889, 1500)
    set_body_pos(BODY_LSHI, 378, 1500)
    set_body_pos(BODY_LANK, 498, 1500)
    time.sleep(1.5)
    
    set_body_pos(BODY_LKNE, 699, 1500)
    time.sleep(1.5)
    
    set_body_pos(BODY_RKNE, 998, 1500)
    time.sleep(1.5)
    
    set_body_pos(BODY_LHIP, 469, 1500)
    set_body_pos(BODY_LTHI, 741, 1500)
    set_body_pos(BODY_LKNE, 171, 1500)
    set_body_pos(BODY_LSHI, 327, 1500)
    set_body_pos(BODY_LANK, 498, 1500)
    set_body_pos(BODY_RHIP, 486, 1500)
    set_body_pos(BODY_RTHI, 241, 1500)
    set_body_pos(BODY_RKNE, 900, 1500)
    set_body_pos(BODY_RSHI, 522, 1500)
    set_body_pos(BODY_RANK, 509, 1500)
    time.sleep(1.5)
    
    set_body_pos(BODY_LTHI, 842, 1500)
    set_body_pos(BODY_RTHI, 141, 1500)
    time.sleep(1.5)
    
    set_body_pos(BODY_LSHO, 990, 750)
    set_body_pos(BODY_RSHO, 7, 750)
     
    time.sleep(1.5)
    ### Sat down successful
    
    
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

sitting_down()
time.sleep(1.0)


# walk_one_step()
# time.sleep(1.0)

# stacking_cubes()
# time.sleep(1.0)





# Print all body servo information
print_body_data(verbose=True)

# Turn off the body servos
body_power_off()
