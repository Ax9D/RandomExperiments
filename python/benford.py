import math
n=20000
i=1
p=1
c=0
while(i<n):
	p<<=1
	d=math.floor(p/10**(math.floor(math.log10(p))))
	
	if(d==1):
		c+=1
	
	i+=1
	
print(c/n)
	
