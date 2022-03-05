import speedtest
from datetime import datetime
from time import sleep, mktime
date_time = datetime.now()
print(int(date_time.strftime("%M"))%5)