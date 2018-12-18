def comparison(firstArg, secondArg, thirdArg):
	if int(firstArg) == int(secondArg):
		return True
	elif int(secondArg) == int(thirdArg):
		return True
	elif int(firstArg) == int(thirdArg):
		return True
	else:
		return False


print(comparison(3,2,3))


