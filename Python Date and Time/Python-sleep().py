import time 

time.sleep(2)
print("Wait until 2 seconds")

## Example sleep() method 
import time 

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")

#create digital clock in py 
import time 
while True:
    curernt_time = time.localtime()
    formatted_time = time.strftime("%I:%M:%S %p", curernt_time)

    print(formatted_time)
    time.sleep(1)