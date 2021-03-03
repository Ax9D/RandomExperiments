def isPrime(n):
	'''f=0;
	for i in range(1,n):
		if(n%i==0):
			f=f+1;
	return f==1;'''
	if(n<=3):
		return n>1;
	elif(n%2==0 or n%3==0):
		return False;
	i=5;
	while(i*i<=n):
		if(n%i==0 or n%(i+2)==0):
			return False;
		i=i+6;
	return True;

def isPal(n):
	return (str(n)==str(n)[::-1]);
	
	
'''def closestPP(n,k):
	i=1;
	p=0;
	#left
	while(p<k):
		if(isPal(n-i) and isPrime(n-i)):
			p+=1;
		i+=1;
	p=0;
	#right
	j=1;
	while(p<k):
		if(isPal(n+j) and isPrime(n+j)):
			p+=1;
		j+=1;	
		
	print(n-i+1);
	print(n+j-1);
	'''

s=[106,119,113,119,49,74,172,242,216,208,339,264,344,267,743,660,893,892,1007,975,10319,10550,10503,11342,11504,12533,12741,12833,13437,13926,13893,14450,14832,15417,15505,16094,16285,16599,16758,17488];
s1=[93766, 93969, 94440, 94669, 94952, 94865, 95934, 96354, 96443, 96815, 97280, 97604, 97850, 98426];
s2=[ 9916239, 9918082, 9919154, 9921394, 9923213, 9926376, 9927388, 9931494, 9932289, 9935427, 9938304, 9957564, 9965794, 9978842, 9980815, 9981858, 9989997, 100030045, 100049982, 100059926, 100111100, 100131019, 100160922, 100404094, 100656111, 100707036, 100767085, 100887990, 100998966, 101030055, 101060206, 101141058];
def nthPP(n):
	i=1;
	while(n>0):
		if(isPal(i) and isPrime(i)):
			n-=1;
		i+=1;
	return i-1;
	
def nextPalPrime(i):
	i+=1;
	while(not isPal(i) or not isPrime(i)):
		i+=1;
	return i;
		
		
def findAddr(s,offset):
	offset_prime=nthPP(offset-1);
	for i in range(0,len(s)):
		nextPrime=nextPalPrime(offset_prime);
		print(chr(s[i]^nextPrime),end='');
		offset_prime=nextPrime;
	print();
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#findAddr(s,1);
#findAddr(s1,99);
findAddr(s2,765);


