def number_letters(n):
	# negatives not supported
	if n < 0:
		return None

	if n == 0:
		return 4 # "zero"

	digits = [int(c) for c in str(int(n))]

	# 4+ digits not supported
	if len(digits) > 3:
		return None

	# get all 3 digits
	while len(digits) < 3:
		digits.insert(0,0)

	hundreds = digits[0]
	tens = digits[1]
	ones = digits[2]

	# first
	if hundreds == 0:
		first = 0 # ""
	elif hundreds == 1:
		first = 10 # "one hundred"
	elif hundreds == 2:
		first = 10 # "two hundred"
	elif hundreds == 3:
		first = 12 # "three hundred"
	elif hundreds == 4:
		first = 11 # "four hundred"
	elif hundreds == 5:
		first = 11 # "five hundred"
	elif hundreds == 6:
		first = 10 # "six hundred"
	elif hundreds == 7:
		first = 12 # "seven hundred"
	elif hundreds == 8:
		first = 12 # "eight hundred"
	elif hundreds == 9:
		first = 11 # "nine hundred"

	# middle
	if tens == 0:
		middle = 0 # ""
	elif tens == 1:
		middle = 0 # ""
	elif tens == 2:
		middle = 6 # "twenty"
	elif tens == 3:
		middle = 6 # "thirty"
	elif tens == 4:
		middle = 5 # "forty"
	elif tens == 5:
		middle = 5 # "fifty"
	elif tens == 6:
		middle = 5 # "sixty"
	elif tens == 7:
		middle = 7 # "seventy"
	elif tens == 8:
		middle = 6 # "eighty"
	elif tens == 9:
		middle = 6 # "ninety"

	# end
	if tens == 1:
		if ones == 0:
			end = 3 # "ten"
		elif ones == 1:
			end = 6 # "eleven"
		elif ones == 2:
			end = 6 # "twelve"
		elif ones == 3:
			end = 8 # "thirteen"
		elif ones == 4:
			end = 8 # "fourteen"
		elif ones == 5:
			end = 7 # "fifteen"
		elif ones == 6:
			end = 7 # "sixteen"
		elif ones == 7:
			end = 9 # "seventeen"
		elif ones == 8:
			end = 8 # "eighteen"
		elif ones == 9:
			end = 8 # "nineteen"
	else:
		if ones == 0:
			end = 0 # ""
		elif ones == 1:
			end = 3 # "one"
		elif ones == 2:
			end = 3 # "two"
		elif ones == 3:
			end = 5 # "three"
		elif ones == 4:
			end = 4 # "four"
		elif ones == 5:
			end = 4 # "five"
		elif ones == 6:
			end = 3 # "six"
		elif ones == 7:
			end = 5 # "seven"
		elif ones == 8:
			end = 5 # "eight"
		elif ones == 9:
			end = 4 # "nine"

	if hundreds == 0 or (tens == 0 and ones == 0):
		return first + middle + end
	else:
		# adds an and
		return 3 + first + middle + end
		

s = 0
for i in range(1,1000):
	s += number_letters(i)

print(11 + s)

print(number_letters(195))