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
print("Printed after 2.4 seconds.")

print()

## Fungsi Python time.localtime()
import time

result = time.localtime(1672214933)
print("Result: ", result)
print("\nyear: ", result.tm_year)
print("tm_hour: ", result.tm_hour)

print()

## Fungsi Python time.gmtime() 
import time 

result = time.gmtime(1672214933)

print("result: ", result)
print("\nyear: ", result.tm_year)
print("tm_hour: ", result.tm_hour)

print() 

## Fungsi Python time.mktime()
import time

time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

seconds = time.mktime(time_tuple)

print(seconds)

print()

## Fungsi Python time.asctime() 
import time

t = (2022, 12, 28, 8, 44, 4, 4, 362, 0)

result = time.asctime(t)
print("Result:", result)

## Fungsi Python time.strftime() 
import time 

named_tuple = time.localtime() 
time_string = time.strftime("%d/%m/%Y, %H:%M:%S")

print(time_string)

print() 

## Fungsi Python time.strptime()
import time 

time_string = "25 November, 2026"
result = time.strptime(time_string, "%d %B, %Y")

print(result)