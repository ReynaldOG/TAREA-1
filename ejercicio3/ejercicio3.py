def palindromo(cad):
	cadena = cad[::-1]
	if cadena== cad:
		return True
	else:
		return False
cad=raw_input("ingrese la palabra")
if palindromo(cad)==True:
	print ("es palindromo")
else:
	print("no es palindromo")