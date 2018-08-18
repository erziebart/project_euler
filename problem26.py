# will run forever if order is not defined
def ord(a,n):
	n %= a
	m = n
	ret = 1
	while m != 1:
		m *= n
		m %= a
		ret += 1
	return ret

cap = 1000
record = 0
r_order = 0
for a in range(2,cap):
	if a%2 != 0 and a%5 != 0:
		order = ord(a,10)
		if order > r_order:
			record = a
			r_order = order

print(record, r_order)