## Fungsi Python time.time()
import time 

second = time.time() 

print("Second since epoch =", second)

print() 

## Fungsi Python time.ctime() 
import time 
second = 1672215379.5045543

local_time = time.ctime(second)

print("Local Time:", local_time)

print() 

## Fungsi Python time.sleep()
import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds. ")