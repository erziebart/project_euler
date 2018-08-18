def digits_remove(digits, n):
	for char in str(n): 
		if char in digits:
			digits.remove(char)
		else:
			return False
	return True

def get_pandigital_product(n):
	# setup digits 1-9
	digits = [str(x) for x in range(1,10)]

	# remove digits in product
	if not digits_remove(digits, n):
		return None

	# cycle through single digit multipliers
	for digit in digits:
		mltplyr = int(digit)
		if n%mltplyr == 0:
			mltcnd = n//mltplyr
			remains = [d for d in digits if d!=digit]
			if digits_remove(remains, mltcnd) and not remains:
				return (mltcnd, mltplyr, n)

	# cycle through two-digit multipliers
	for i in range(len(digits)):
		for j in range(len(digits)):
			if i == j: continue
			mltplyr = int(digits[i]+digits[j])
			if n%mltplyr == 0:
				mltcnd = n//mltplyr
				remains = [d for d in digits if d!=digits[i] and d!=digits[j]]
				if digits_remove(remains, mltcnd) and not remains:
					return (mltcnd, mltplyr, n)

	# solution not found
	return None

products = []
s = 0
for n in range(1111,10000):
	prod = get_pandigital_product(n)
	if prod:
		products.append(prod)
		s += n

print(products)
print(s)