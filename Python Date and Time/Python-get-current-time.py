## Waktu saat ini menggunakan objek datetime
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Waktu sekarang =", current_time)

print()

## Waktu saat ini, sesuai dengan data yang diberikan oleh model waktu 
import time 

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

print()

## Waktu saat ini di zona waktu tertentu

from datetime import datetime
import pytz

tz_Riyadh = pytz.timezone('Asia/Riyadh')
datetime_Riyadh = datetime.now(tz_Riyadh)
print("Riyadh time:", datetime_Riyadh.strftime("%H:%M:%S"))


tz_Barcelona = pytz.timezone('Europe/Madrid')
datetime_Barcelona = datetime.now(tz_Barcelona)
print("Barcelona time:", datetime_Barcelona.strftime("%H:%M:%S"))
