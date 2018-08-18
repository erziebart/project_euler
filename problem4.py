import math

# returns the largest palindromic number less than n
def prev_palindrome(n):
	s = str(n-1)
	c = math.floor(0.5*len(s))
	first = s[:c]
	second = s[-c:]

	diff = int(second) - int(first[::-1])
	if diff >= 0:
		return n - diff - 1
	else:
		return prev_palindrome(n-int(second)-1)

def find_3digit_factor(n):
	lower = math.floor(math.sqrt(n))

	for f in range(999,lower,-1):
		if(n % f == 0):
			return f

	return None


n = 999*999
while True:
	f = find_3digit_factor(n)
	if f:
		print(f,"*",n/f,"=",n)
		break
	n = prev_palindrome(n)