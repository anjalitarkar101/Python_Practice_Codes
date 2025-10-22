import time

wait_time = 1  # initial wait time in seconds
max_retries = 5  # maximum number of retries
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1 , "Wait time", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time = wait_time*2  # double the wait time   # wait_time *= 2 (shorthand)
    attempts = attempts+1    # increase the attempts by 1                         #attempts += 1 (shorthand)