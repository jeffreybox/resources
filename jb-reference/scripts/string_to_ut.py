#string_to_UT

from datetime import datetime
import time

dt = '2019-05-01'
uTime = time.mktime(datetime.strptime(dt, "%Y-%m-%d").timetuple())
uTime