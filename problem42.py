triangles = [1]

with open('p042_words.txt') as file:
	ls = file.read().split(",")

words = [word.strip("\"") for word in ls]

count  = 0
for word in words:
	s = sum([ord(letter)-64 for letter in word])
	while s > triangles[-1]:
		n = len(triangles)+1
		triangles.append(n*(n+1)//2)
	if s in triangles:
		count += 1

print(triangles)
print(count)