try:
	a=int(input("Enter a number "))
	if a<5:
		raise TypeError
	elif a==5:
		raise NameError
except NameError:
	print("Error...u have chosen no equal to 5")
except TypeError:
	print("Erroe....u have chosen no less than 5")
else:
		print("No Error")
finally:
		print("completed")
