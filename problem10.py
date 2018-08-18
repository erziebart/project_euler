import divisors as pt

n = 2E6

m = 3
primes = [2]
s = 2

while m < n:
	if pt.is_prime(primes, m):
		primes.append(m)
		s += m
	m += 2

#print(primes)
print(s)