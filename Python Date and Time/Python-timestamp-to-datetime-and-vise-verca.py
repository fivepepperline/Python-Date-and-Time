##Konversi timestamp Python menjadi fprmat datetime
from datetime import datetime

timestamp = 1545730073

dt_object = datetime.fromtimestamp(timestamp)
print("dt_objwct:", dt_object)
print("type dt_object:", type(dt_object))

print() 

## Konversi tanggal/waktu dari format Python datetime ke format timestamp
from datetime import datetime 

now = datetime.now()

ts = datetime.timestamp(now)

print("Timestamp:", ts)