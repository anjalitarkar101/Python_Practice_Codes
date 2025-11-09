# Program to implement exponential backoff strategy for retrying an operation such that 
# the wait time doubles with each retry attempt, starting from 1 second, up to a maximum of 5 retries.

import time      # to use sleep function

wait_time = 1    # initial wait time in seconds
max_retries = 5  # maximum number of retries
attempts = 0     # current attempt count

while attempts < max_retries:
    print("Attempt", attempts + 1 , "Wait time", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time *= 2   # double the wait time
    attempts += 1    # increase the attempts by 1