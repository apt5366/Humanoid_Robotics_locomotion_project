import argparse
import sys
import time
import inspect
import csv
import threading
import numpy as np
from helper_utils import *

########################################
### Data and Helper functions
########################################

# Global variables
mpu_data = []
column_headers = ["Time",
                  "Acc X", "Acc Y", "Acc Z",
                  "Gyro X", "Gyro Y", "Gyro Z"]
mpu_resolution = 0.05 #20Hz

# A more accurate sleep function
# Kind of hacky, but it avoids the overhead on time.sleep()
def my_sleep(sleep_time):
    if sleep_time < 0:
        sys.exit("Negative value passed to {}; value must be nonnegative!".format(inspect.stack()[0][3]))
    end_time = time.time() + sleep_time
    while time.time() <= end_time:
        pass

# Round all values in a 2D array
def round_data(data_in):
    return [[round(col, 3) for col in row] for row in data_in]

# Collect accelerometer and gyroscope data
def mpu_data_collector(stop_sig, start_time):
    tick = start_time
    (temp_acc, temp_gyro) = get_mpu_movement()
    while not stop_sig.is_set():
        tick += mpu_resolution
        while time.time() <= tick:
            (temp_acc, temp_gyro, _) = get_mpu_all()
        mpu_data.append([tick - start_time] + temp_acc + temp_gyro)

# Do the movement defined by the input data
def do_movement(times, body_angs, head_angs):
    for i in range(len(times)):
        for j in range(len(ALL_BODY)):
            set_body_pos(ALL_BODY[j], body_angs[i][j], times[i])
        for j in range(len(ALL_HEAD)):
            set_head_pos(ALL_HEAD[j], head_angs[i][j], times[i])
        my_sleep(times[i] / 1000)

# Read movement CSV file
def read_movement_file(file_in):
    times = []
    body_angs = []
    head_angs = []
    with open(file_in) as input_fp:
        input_reader = csv.reader(input_fp, delimiter = ',')
        next(input_reader, None) # Skip the headers
        for line in input_reader:
            times.append(int(line[0]))
            body_angs.append([int(x) for x in line[1:19]])
            head_angs.append([int(x) for x in line[19:21]])
    return (times, body_angs, head_angs)

# Write the output data to a CSV
def write_csv(filename, data):
    with open(filename, 'w', newline='') as csv_fp:
        csv_writer = csv.writer(csv_fp, delimiter=',')
        csv_writer.writerows([column_headers] + data)


########################################
### Main functionality
########################################

# Main functionality of the program
def main(args):
    # Try reading the input file
    (times, body_angs, head_angs) = read_movement_file(args.input_filename + ".csv")

    # Initialize the robot
    init_robot_data(swap_hands = args.swap_hands)

    # Let user know that the process has started
    print()
    print("Running movement and collecting data")
    
    # Create event to stop thread
    stop_sig = threading.Event()

    # Create and start the separate thread for collecting data
    sensor_thread = threading.Thread(target=mpu_data_collector, args=(stop_sig, time.time(), ))
    sensor_thread.start()

    # Do all the movement here
    my_sleep(0.5)
    do_movement(times, body_angs, head_angs)
    my_sleep(0.5)
    body_power_off()

    # Signal that movement is done and join the sensor thread
    stop_sig.set()
    sensor_thread.join()

    # Let user know that process has finished
    parsed_file_out = ""
    if args.output_filename == "":
        parsed_file_out = args.input_filename + "_output.csv"
    else:
        parsed_file_out = args.output_filename + ".csv"
    print("Data collection complete, outputting to {:}".format(parsed_file_out))
    print()

    # Output the data to a CSV file
    write_csv(parsed_file_out, round_data(mpu_data))

# Parse input args
def parse_input_args():
    arg_obj = argparse.ArgumentParser(description="Run movement in a file and get sensor data.")
    arg_obj.add_argument('-i', '--input', required=True, type=str, dest='input_filename', help="Path to an input movement file for the robot to perform, do not include .csv")
    arg_obj.add_argument('-o', '--output', type=str, default="", dest='output_filename', help="Output file for the data collected during runtime, do not include .csv")
    arg_obj.add_argument('-s', '--swap_hands', action='store_true', help="Swaps the robot's hand ID values")
    return arg_obj.parse_args()

# Requires arguments to be passed into it
if __name__ == "__main__":
    args = parse_input_args()
    main(args)