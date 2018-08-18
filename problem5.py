import miller_rabin as pt

def get_multiplicities(primes, n):
	res = []
	for i in range(len(primes)):
		p = primes[i]
		count = 0
		while n%p == 0:
			n /= p
			count += 1
		res.append(count)
	return res

n = 20

# find all primes <= n
primes = [2]
for p in range(3,n+1,2):
	if pt.is_prime(p):
		primes.append(p)

# initialize the multiplicities
multiplicities = [0 for p in primes]

# find multiplicities of all the primes
for i in range(1,n+1):
	mults = get_multiplicities(primes, i)
	for j in range(len(mults)):
		if mults[j] > multiplicities[j]:
			multiplicities[j] = mults[j]

print(primes)
print(multiplicities)

# compute the total
total = 1
for i in range(len(primes)):
	total *= primes[i]**multiplicities[i]

print(total)