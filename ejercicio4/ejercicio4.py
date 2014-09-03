def ValorCadena(x, y):
	a=len(x)
	b=len(y)
	if a > b:
		print x
	else:
		if a==b:
			print x + y
		else:
			print y
e=raw_input("ingrese la primera palabra")
f=raw_input("ingrese la segunda palabra")
ValorCadena(e, f)
