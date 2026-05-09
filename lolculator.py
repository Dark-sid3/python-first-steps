numb1 = int(input("Введите первое число:"))
lol = input("+ или -?")
numb2 = int(input("Введите второе число:"))

if lol == "+":
	print(numb1 + numb2)
elif lol == "-":
	print(numb1 - numb2)
else:
	print("Штирлиц стрелял вслепую. Слепая убегала скачками. Всех качков застрелили, в живых осталась лишь слепая.")
