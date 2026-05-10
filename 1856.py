print("Вычислите пароль с помощью кода 1856. Выход — \"exit\".")

while True:
	numbers = [1, 1, 1, 1, True, "Hi", 4, 5, "lol", 6, 7, 8, 8, 8, 8, 8, 9]
	numbers[4] = 2
	numbers[5] = 3
	numbers[8] = 6
	
	us_inp = input("")
	
	if us_inp == "exit":
		print("Выход из системы.")
		break
	
	try:
		n = int(us_inp)
		print(numbers.count(n))
	
	except ValueError:
		print("Введите число, пожалуйста.")
