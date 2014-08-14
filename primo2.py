import sys
def gcd(a,b):
	(a,b) = (max(a,b),min(a,b))
	return a if b==0 else gcd(b, a%b)

rel = gcd(int(sys.argv[1]),int(sys.argv[2]))
print "Son realtivamente primos" if rel==1 else "No son realtivamente primos" 