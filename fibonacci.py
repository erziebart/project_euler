def fib(n):
	phi = 0.5*(1 + math.sqrt(5))
	return math.floor((phi**n)/math.sqrt(5) + 0.5)