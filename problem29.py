bases = range(2,101)
expons = range(2,101)

powers = set()
for a in bases:
	for b in expons:
		powers.add(a**b)

print(len(powers))