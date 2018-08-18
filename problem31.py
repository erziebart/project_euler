target = 200
denoms = [1,2,5,10,20,50,100,200]

counts = [0 for x in range(target+1)]
counts[0] = 1
for coin in denoms:
	for idx in range(coin,target+1):
		counts[idx] += counts[idx-coin]
print(counts[-1])