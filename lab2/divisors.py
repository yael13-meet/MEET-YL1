def divisors(n):
	#print "Enter a number"
	#n = int (raw_input())
	for i in range(n):
		x = i+1
		if n%x==0:
			print x

divisors(5)
