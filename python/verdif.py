def verDiff(version1,version2):
	parts1=[int(x) for x in version1.split(".")]
	parts2=[int(x) for x in version2.split(".")]
	l1=len(parts1)
	l2=len(parts2)
	
	i=0
	while(i<l1 and i<l2):
		if(parts1[i] > parts2[i]):
			return 1
		elif(parts1[i] < parts2[i]):
			return -1
		i+=1
		
	while(i<l1):
		if(parts1[i]!=0):
			return 1
		i+=1
		
	while(i<l2):
		if(parts2[i]!=0):
			return -1
		i+=1
	
	return 0

def test(v1,v2):
	res=verDiff(v1,v2)
	if(res==0):
		print(v1,"=",v2)
	elif(res==1):
		print(v1,">",v2)
	else:
		print(v1,"<",v2)
		
test("7.5.2.4","7.5.3")
		
