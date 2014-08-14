#Saber si un numero es o no primo
import sys
def primo(n):
	count = 0
	end = False
	for num in range(1,n+1):
		if n%num==0:
			count+=1
		if end > 2:
			end = True	
	print "Es primo" if count==2 and not end else "No es primo"		

n=input("Type a number: ")
primo(n)	