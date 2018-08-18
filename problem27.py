import divisors as div
import divisors as pt

def get_primes_generated(a,b):
	count = 0
	n = 1
	while True:
		val = n*n + a*n + b
		if not pt.is_prime_n(val):
			break
		count += 1
		n += 1
	return count

limit_b = 1000
limit_a = 1000

# first, find all primes less than or equal limit_b
primes = [2]
for n in range(3, limit_b+1, 2):
	if div.is_prime(primes, n):
		primes.append(n)
#print(primes)

# make limit_a an odd number
if limit_a % 2 == 0:
	limit_a -= 1

# find the record number of primes
record = 0
record_a = 0
record_b = 0
for b in primes:
	for a in range(-limit_a,limit_a+1,2):
		cur = get_primes_generated(a,b)
		if cur > record:
			record = cur
			record_a = a
			record_b = b

print(record_a, record_b, 1+record)
print(record_a*record_b)

#print(get_primes_generated(1,41))