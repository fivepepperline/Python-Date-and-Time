## 1. Cara mendapatkan tanggal hari ini menggunakan Python 
from datetime import date 

today = date.today() 
print("Tanggal hari ini adalah:", today)

print() 

## 2. Tanggal saat ini dalam berbagai format
from datetime import date 

today = date.today()

d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

print() 

## Get the current date and time in Pyhton 
from datetime import datetime

now = datetime.now() 

print("sekarang :", now)

dt_string = now.datetime("%d/%m/%Y %H:%M:%S")
print("tanggal dan waktu :", dt_string)

print()