# Python Date and Time 
## 1. Mendapatkan tanggal dan waktu terbaru
import datetime 

now = datetime.datetime.now() 

print(now)

print() 

## 2. Mendapatkan tanggal saat ini 
import datetime 
current_date = datetime.date.today()

print(current_date)

print() 

## Atribute of Datetieme Model 
import datetime

print(dir(datetime))

print() 

## Python datetime.date Class 
## 3. Objek tunggal yang digunakan untuk mempresentasikan suatu tanggal tertentu. 
import datetime

d = datetime.date(2026, 12, 20)
print(d)

print() 

## Import only date class 
from datetime import date 

d = date(2025, 12, 10)
print(d)

print() 

## 4. Mendapatkan tanggal saat ini menggunakan fungsi today() 
from datetime import date 

tanggal_hari_ini = date.today()
print(tanggal_hari_ini)

print()

## 5. Mendapatkan nilai tanggal dari nilai timestamp 
from datetime import date 

timestamp = date.fromtimestamp(1326244364)
print("Date = ", timestamp)

print() 

## 6. Print tahun, bulan, dan hari ini
from datetime import date 

hari_ini = date.today() 

print("Tahun ini : ", hari_ini.year)
print("Bulan ini : ", hari_ini.month)
print("Hari ini  : ", hari_ini.day)

print() 

## Python datetime.time Class
## 7. Objek waktu untuk mempresentasikan waktu 
from datetime import time

a = time() 
print(a)

b = time(12, 45, 30)
print(b)

c = time(hour=12, minute=10, second=30)
print(c)

d = time(14, 31, 44, 777213)
print(d)

print()

## 8. Print nilai jam, menit, detik, dan mikrodetik
from datetime import time 

a = time(9, 45, 15)

print("Jam        : ", a.hour)
print("Menit      : ", a.minute)
print("Detik      : ", a.second)
print("Mikrodetik : ", a.microsecond)

print() 

## The datetime.datetime Class
## 9. Objek datetime dalam Python 
from datetime import datetime 

a = datetime(2026, 12, 30)
print(a)

b = datetime(2024, 3, 12, 21, 0, 0, 112346)
print(b)

print() 

## 10. Print tahun, bulan, jam, menit, dan waktu tertentu
from datetime import datetime

a = datetime(2023, 12, 30, 20, 30, 15, 123234)
print("Tahun: ", a.year)
print("Bulan: ", a.month)
print("Tanggal: ", a.day)
print("Jam: ", a.hour)
print("menit: ", a.minute)
print("Timestamp: ", a.timestamp())

print() 

## Python datetime.timedelta.Class
from datetime import datetime, date 

t1 = date(year = 2003, month = 11, day = 9)
t2 = date(year = 2000, month = 5, day = 20)

t3 = t1 - t2
print("t3: ", t3)

t4 = datetime(year = 2005, month = 3, day = 30, hour = 7, minute = 30 , second = 12)
t5 = datetime(year = 2006, month = 1, day = 12, hour = 8, minute = 16, second = 4)
t6 = t4 -t5 
print("t6: ", t6)

print("Type of t3: ", type(t3))
print("type of t6: ", type(t6))

## 12. Perbedaan antara dua objek timedelta 
from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 44)
t3 = t1 - t2

print("t3: ", t3)

print() 

## 14. Durasi waktu dalam detik 
from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds =233423)

print("Total seconds = ", t.total_seconds()) 

## Metode strftime() dalam Python 
from datetime import datetime

now = datetime.now()

t = now.strftime("%H:%M:%S")
print("Time: ", t)

s1 = now.strftime("%m: %d: %Y, %H: %M: %S")
print("S1: ", s1)

s2 = now.strftime("%d: %m: %y, %H: %M: %S")
print("S2: ", s2)

print() 

## Metode strptime() dalam Python 
from datetime import datetime

date_string = "25 December, 2025"
print("Date String: ", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Date Object: ", date_object)

print() 

## Mengelola Zona Waktu di Python 
from datetime import datetime 
import pytz

local = datetime.now() 
print("Local: ", local.strftime("%m%d%Y, %H: %M: %S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY: ", datetime_NY.strftime("%m%d%Y, %H: %M: %S"))

tz_london = pytz.timezone('Europe/London')
datetime_london = datetime.now(tz_london)
print("London: ", datetime_london.strftime("%m%d%Y, %H: %M: %Y"))

