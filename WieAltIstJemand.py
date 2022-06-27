"""Code that tells me number of years, days, hours and minutes person have been alive."""

def years_days_hours_minutes(td): ## Includes leap year so 26/06/2022 and 26/06/2002 is 20Y and 5D for the 5 leap years over the period
    years = td.days // 365
    days = td.days % 365
    hours = td.seconds//3600
    minutes =  (td.seconds//60)%60
    formated = (years, days, hours, minutes) ## Tuple
    return formated 

from datetime import *

raw_birth_date = input("Enter date and time of birth, formate dd/mm/yyyy; mm:hh (e.g. 07/03/1850; 04:07):")
##----------------------------------- works only on my defined format, add GUI with drop lists in future to be fool-proof
b_year = int(raw_birth_date[6:10])
b_month = int(raw_birth_date[3:5])
b_day = int(raw_birth_date[0:2])
b_hour = int(raw_birth_date[12:14])
b_minute = int(raw_birth_date[15:17])
##------------------------------------

## The two days to compare
current_date = datetime.now()
birth_date = datetime(year=b_year, month=b_month, day=b_day, hour=b_hour, minute=b_minute)

timedelta = current_date - birth_date ## This way we can do operations on time objects

neat_timedelta = years_days_hours_minutes(timedelta)

print(neat_timedelta)