p = 5
n = 6*9**5

nums = []
for num in range(2,n):
	tot = 0
	for digit in str(num):
		tot += int(digit)**p
	if tot == num:
		nums.append(num)

print(nums)
print(sum(nums))