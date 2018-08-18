''' perform a miller-rabin primality test '''

# deterministic for n < 341,550,071,728,321

def is_prime(n):
	if n<2:
		return False # less than 2 nothing is prime, by definition
	if n<4:
		return True # 2 and 3 are prime

	if n%2 == 0:
		return False # even numbers above 2 are composite
	
	# decide what the witnesses are
	if n < 2047:
		witnesses = [2]
	elif n < 1373653:
		witnesses = [2, 3]
	elif n < 9080191:
		witnesses = [31, 73]
	elif n < 25326001:
		witnesses = [2, 3, 5]
	elif n < 3215031751:
		witnesses = [2, 3, 5, 7]
	elif n < 4759123141:
		witnesses = [2, 7, 61]
	elif n < 1122004669633:
		witnesses = [2, 13, 23, 1662803]
	elif n < 2152302898747:
		witnesses = [2, 3, 5, 7, 11]
	elif n < 3474749660383:
		witnesses = [2, 3, 5, 7, 11, 13]
	else:
		witnesses = [2, 3, 5, 7, 11, 13, 17]

	# test all the witnesses
	for a in witnesses:
		if is_witness(n, a):
			return False

	return True

def is_witness(n, a):
	# find unique s,d such that 2^s*d = n-1 and d is odd
	s = 0
	d = n-1
	while d%2 == 0:
		s += 1
		d //= 2

	# test if a^d = 1 (mod n)
	if ex_mod_n(a,int(d),n) == 1:
		return False

	# test if a^(2^r*d) = -1 (mod n) for all 0 <= r <= s-1
	for r in range(0,s):
		if ex_mod_n(a,int(2**r*d),n) == n-1:
			return False

	return True

def ex_mod_n(base, exp, n):
	powers = [(1,base)]
	power = 2
	while power < exp:
		p,b = powers[-1]
		powers.append((power,(b**2)%n))
		power *= 2

	result = 1
	for p,b in reversed(powers):
		if p <= exp:
			result *= b
			result %= n
			exp -= p

	return result