import sys
def gcd(a,b):
	(a,b) = (max(a,b),min(a,b))
	print (a,b)
	return a if b==0 else gcd(b, a%b)

print gcd(int(sys.argv[1]),int(sys.argv[2]))