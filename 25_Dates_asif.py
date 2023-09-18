# Dates

import datetime

x = datetime.datetime.now()

print(x)

# Date Output

x = datetime.datetime.now()

print(x.year)

print(x.strftime("%A"))

# Creating Date Objects

x = datetime.datetime(2020, 5, 17)

print(x)

# The strftime() Method
# Weekday, short version	, Wed

x = datetime.datetime.now()

print(x.strftime("%a"))

# Weekday, full version	 , Wednesday

x = datetime.datetime.now()

print(x.strftime("%A"))

# Weekday as a number 0-6, 0 is Sunday	, 3

x = datetime.datetime.now()

print(x.strftime("%w"))

# Day of month 01-31	, 31

x = datetime.datetime.now()

print(x.strftime("%d"))

# Month name, short version	, Dec

x = datetime.datetime.now()

print(x.strftime("%b"))

# Month name, full version	, December

x = datetime.datetime.now()

print(x.strftime("%B"))

# Month as a number 01-12	, 12

x = datetime.datetime.now()

print(x.strftime("%m"))

# Year, short version, without century	, 18

x = datetime.datetime.now()

print(x.strftime("%y"))

# Year, full version	, 2018

x = datetime.datetime.now()

print(x.strftime("%Y"))

# Hour 00-23	, 17

x = datetime.datetime.now()

print(x.strftime("%H"))

# 	Hour 00-12	, 05

x = datetime.datetime.now()

print(x.strftime("%I"))

# 	AM/PM	, PM

x = datetime.datetime.now()

print(x.strftime("%p"))

# Minute 00-59	, 41

x = datetime.datetime.now()

print(x.strftime("%M"))

# Second 00-59	, 08

x = datetime.datetime.now()

print(x.strftime("%S"))

# Microsecond 000000-999999	, 548513

x = datetime.datetime.now()

print(x.strftime("%f"))

# 	UTC offset	, +0100

x = datetime.datetime.now()

print(x.strftime("%z"))

# 	Timezone	, CST

x = datetime.datetime.now()

print(x.strftime("%Z"))

# Day number of year 001-366	, 365

x = datetime.datetime.now()

print(x.strftime("%j"))

# Week number of year, Sunday as the first day of week , 00-53	, 52

x = datetime.datetime.now()

print(x.strftime("%U"))

# Week number of year, Monday as the first day of week, 00-53	, 52

x = datetime.datetime(2018, 5, 31)

print(x.strftime("%W"))

# Local version of date and time	, Mon Dec 31 17:41:00 2018

x = datetime.datetime.now()

print(x.strftime("%c"))

# Century	, 20

x = datetime.datetime.now()

print(x.strftime("%C"))

# Local version of date	, 12/31/18

x = datetime.datetime.now()

print(x.strftime("%x"))

# Local version of time	, 17:41:00

x = datetime.datetime.now()

print(x.strftime("%X"))

# A % character	, %

x = datetime.datetime.now()

print(x.strftime("%%"))

# ISO 8601 year	, 2018

x = datetime.datetime.now()

print(x.strftime("%G"))

# ISO 8601 weekday (1-7)	, 1

x = datetime.datetime.now()

print(x.strftime("%u"))

# ISO 8601 weeknumber (01-53)	, 01

x = datetime.datetime.now()

print(x.strftime("%V"))








