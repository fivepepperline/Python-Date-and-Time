## 1. Mengonversi string menjadi objek datetime
from datetime import datetime 
date_string = "21 June, 2026"

print("date_string =", date_string)
print("Type of data_strin =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("Type of date_object =", type(date_object))

print() 

##2. Mengonversi string menjadi objeck datetime
from datetime import datetime

dt_string = "12/11/2025 09:30:50"

dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print('dt_object1 =', dt_object1)

dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2 =", dt_object2)

## 3. Value error pada fungsi strptime() 
'''
from datetime import datetime 
date_string = "12/11/2026
date_object = datetime.strptime(date_string, "%d %m %Y")

print("date_object =", date_object)
penjelasan: kesalahan ada pada ketidaksesuaian format pada variabel data objek %d %m %Y pada 12/11/2026. Perbaikannya adalah menambahkan tanda slash seperti %d/%m/%Y'''