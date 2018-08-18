import heapq as h

record = (1,1)
n = int(1E6)

def set_record(r,d):
	global record, found
	rr, rd = record
	if r <= n:
		if rd < d:
			record = (r,d)
		return 1
	return 0

def collatz_tree_trickle(root, depth, ls):
	if root%6 == 4:
		r = (root-1)//3
		d = depth + 1
		if r > 1:
			ret = set_record(r,d)
			h.heappush(ls,(r,d))
			return ret + collatz_tree_trickle(r,d,ls)
	return 0

def collatz_tree_expand(root, depth, ls):
	r = 2*root
	d = depth + 1
	ret = set_record(r,d)
	h.heappush(ls,(r,d))
	return ret + collatz_tree_trickle(r,d,ls)

def collatz_steps(n, cache, limit):
	steps = 1
	while n != 1:
		if n in cache:
			return cache[n] + steps

		if n%2 == 0:
			n //= 2
		else:
			n = 3*n + 1
		steps += 1

		if steps > limit:
			return None
	return steps

# generate a list of lower depth values
ls = [(1,1)]
found = 1
k = 90000
while found < k:
	r,d = h.heappop(ls)
	ret = collatz_tree_expand(r, d, ls)
	#print(r,d,ret)
	found += ret
	#print(r,d)

#print(ls)
print(record)
print(found)

#print(collatz_steps(934299))

# create a cache using the list
dic = dict()
for r,d in ls:
	dic[r] = d
#print(dic)

# try to find as many values a possible
not_found = []
limit = 500
for i in range(1,n):
	ret = collatz_steps(i, dic, limit)
	if not ret:
		not_found.append(i)
	else:
		set_record(i,ret)

print(not_found)
#print(len(not_found))
print(record)

#print(collatz_steps(910107, dict(), 500))