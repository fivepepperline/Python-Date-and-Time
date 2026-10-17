## 1. Mengubah format datetime menjadi string menggunakan fungsi strftime 
from datetime import datetime 

now = datetime.now()

year = now.strftime("%Y")
print("Tahun: ", year)

month = now.strftime("%m")
print("Bulan: ", month)

day = now.strftime("%d")
print("Tanggal: ", day)

time = now.strftime("%H: %M: %S")
print("Waktu: ", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Tanggal dan Waktu: ", date_time)

print()

## 2. Membuat string dari tanggal dan waktu 
from datetime import datetime 

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object: ", date_time)

d = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)

d = date_time.strftime("%d, %b, %Y")
print("Output 3:", d)

d = date_time.strftime("%d, %m, %Y")
print("Ouput 4:", d)

d = date_time.strftime("%I%p")
print("Output 5:", d)

print() 

## 3. Tanggal dan waktu yang sesuai dengan pengaturan lokal
from datetime import datetime 

timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

d = date_time.strftime("%c")
print("Ouput 1:", d)

d = date_time.strftime("%x")
print("Output 2:", d)

d = date_time.strftime("%C")
print("Output 3:", d)