while True:
	loh = int(input("Вводи разные числа, чтобы приблизиться к нужному: "))
	
	if loh > 5:
	   print("Меньше")
	elif loh < 5:
	   print("Больше")
	elif loh == 5:
	   print("Угадал")
	   break
