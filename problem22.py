with open("p022_names.txt") as file:
	ls = file.read().split(",")

names = [name.strip("\"") for name in ls]
names.sort()

total = 0
pos = 0
for name in names:
	pos += 1
	value = sum([ord(letter)-64 for letter in name])
	score = pos*value
	total += score

print(total)