count = 0
word = "обконч тебя сто хуе 𓂺"
for i in word:
	print(i * 5)
	if i == "о":
		count += 1
	print(count)
	
word = "𓂺"
print(word * 100)
