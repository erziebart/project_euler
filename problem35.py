import divisors as pt

def list_combos(ls, n):
	if n <= 0:
		return None
	if n == 1:
		for elt in ls:
			yield elt
		return None

	for first in ls:
		for end in list_combos(ls, n-1):
			yield first + end

def get_candidates(n):
	if n < 1:
		return None
	if n == 1:
		yield "2"
		yield "3"
		yield "5"
		yield "7"
		return None

	digits = ["1","3","7","9"]
	for n in list_combos(digits, n):
		yield n

def is_smallest_rotation(num):
	n = len(num)
	for c in range(1,n):
		r = min(c, n-c) + 1
		for i in range(r):
			a = num[i]
			b = num[(c+i)%n]
			if a > b:
				return False
			if a < b:
				break
	return True

def get_rotations(num):
	ret = []
	for i in range(len(num)):
		n = num[i:]+num[:i]
		if n not in ret:
			ret.append(n)
	return ret

limit = 6
smallest = []
primes = []
for d in range(1,limit+1):
	for n in get_candidates(d):
		if is_smallest_rotation(n):
			smallest.append(n)
			circular = True
			rot = get_rotations(n)
			for p in rot:
				circular &= pt.is_prime_n(int(p))
			if circular:
				for p in rot: 
					primes.append(p)

print(primes)
print(len(primes))