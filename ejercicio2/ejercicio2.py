def lista(x, y):
	a=x
	b=y
	while a <= b:
		print a,
		a=a+1
def pares(x, y):
	a=x
	b=y
	while a <= b:
		if a % 2 ==0:
			print a,
			a=a+1
		else :
			a=a+1	
l=input ("ingrese el primer numero")
m=input ("ingrese el segundo numero")
lista(l, m)
print " "
print " "
pares(l, m)