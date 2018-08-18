def is_leap_year(year):
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	return False


def days_in_month(year, month):
	if month==3 or month==5 or month==8 or month==10:
		return 30
	if month==1:
		if is_leap_year(year):
			return 29
		else:
			return 28
	return 31


year = 1901
month = 0
weekday = 2

count  = 0

while year < 2001:
	days = days_in_month(year, month)
	weekday = (weekday + days) % 7
	if weekday == 0:
		count += 1
	#print(year,month,days)

	month += 1
	if month > 11:
		year += 1
		month %= 12
	#print(month, weekday)

print(count)