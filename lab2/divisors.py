
def divisors(n):
#print "Enter a number"
	#n = int (raw_input())
	for i in range(n):
		x = i+1
		if n%x==0:
			print x


if __name__=="__main__":
	print "Enter a number"
	n=int(raw_input())
	divisors(n)


