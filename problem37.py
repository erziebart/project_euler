import divisors as pt;

limit = 6;

left = set();
right = set();

lstart = ['3','7']
rstart = ['2','3','5','7']
append = ['1','2','3','5','7','9']

# append on left
for i in range(limit-1):
	lnext = []
	for num in lstart:
		for digit in append:
			prime = digit + num;
			p = int(prime);
			if pt.is_prime_n(p):
				left.add(p);
				lnext.append(prime);
	lstart = lnext;

# append on right
for i in range(limit-1):
	rnext = []
	for num in rstart:
		for digit in append:
			prime = num + digit;
			p = int(prime);
			if pt.is_prime_n(p):
				right.add(p);
				rnext.append(prime);
	rstart = rnext;

res = left.intersection(right)
print(res);
print(sum(res));