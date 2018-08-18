import math

def divides(divisors, n):
	for d in divisors:
		if n%d == 0:
			return True
	return False

def is_prime(known, n):
	if n < 2:
		return False
	m = math.sqrt(n)
	for p in known:
		if p > m:
			break
		if n%p == 0:
			return False
	return True

def is_prime_n(n):
	if n < 2:
		return False
	if n == 2:
		return True

	m = math.floor(math.sqrt(n))

	if n%2 == 0:
		return False

	for i in range(3,m+1,2):
		if n%i == 0:
			return False

	return True

def prime_factors(n):
	ret = []

	while n%2 == 0:
		ret.append(2)
		n /= 2

	p = 3
	while n > 1:
		while n%p == 0:
			ret.append(p)
			n /= p
		p += 2

	return ret

def factor_count(n):
	prod = 1

	count = 1
	while n%2 == 0:
		n /= 2
		count += 1
	prod *= count

	p = 3
	while n > 1:
		count = 1
		while n%p == 0:
			n /= p
			count += 1
		prod *= count
		p += 2

	return prod

def factorize(n):
	if n == 0:
		return []

	factors = [n]

	cur = n
	while cur%2 == 0:
		cur //= 2
		factors.append(cur)

	p = 3
	done = False
	while p <= n:
		if n%p == 0 and n//p not in factors:
			to_add = []
			for cur in factors:
				while cur%p == 0:
					cur //= p
					to_add.append(cur)
					if cur == 1:
						done = True
			factors.extend(to_add)

			if done:
				break
		p += 2

	return factors

def proper_divisors(n):
	if n == 0:
		return []
	ret = factorize(n)
	ret.remove(n)
	return ret

def reduce_frac(num, den):
	while num%2==0 and den%2==0:
		num //= 2
		den //= 2

	p = 3
	while p<=num and p<=den:
		while num%p==0 and den%p==0:
			num //= p
			den //= p
		p += 2

	return (num,den)

def gcd(a,b):
	if a < b:
		t = a
		a = b
		b = t

	r = 1
	while r != 0:
		r = a % b
		a = b
		b = r

	return a

def lcm(a,b):
	return a*b//gcd(a,b)

def is_coprime(a,b):
	return gcd(a,b) == 1