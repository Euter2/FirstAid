from datetime import datetime, timedelta
from astral import Location
info=( 'Brno', 'Czech Republic', 49.241921, 16.566693, 'Europe/Prague', 278 )
l=Location(info)

brno_today_sunrise=l.sunrise(datetime.today().date(), True)
brno_today_sunset=l.sunset(datetime.today().date(), True)

#brno_tomorrow_sunrise=l.sunrise(datetime.today().date()+timedelta(days=1), True)
#brno_tomorrow_sunset=l.sunset(datetime.today().date()+timedelta(days=1), True)


print(brno_today_sunrise.time())
print(brno_today_sunset.time())
print(brno_tomorrow_sunrise.time())
print(brno_tomorrow_sunset.time())

if brno_today_sunrise.time()<datetime.now().time()<brno_today_sunset.time():
    print ('Sun is UP since %s!' % str(brno_today_sunrise.time()))
else:
    print('Sun is DOWN!')
