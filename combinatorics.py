def factorial(n):
	if n%1 != 0 or n < 0:
		return None

	res = 1
	for i in range(1,n+1):
		res *= i

	return res

def binomial(n,r):
	return None