from collections import OrderedDict
import random
import sys
import matplotlib.pyplot as plt
import numpy as np

def fifo(accesses,nPages):
	cacheData=OrderedDict()
	
	hit=0
	for access in accesses:
		for p in [k for (k,v) in cacheData.items()]:
			print(p,end=' ')
		print('| '+access+(' Hit' if access in cacheData else ' Miss'))
		
		if(access in cacheData):
			hit+=1
			continue
		elif(len(cacheData)==nPages):
			cacheData.popitem(last=False)
		
		cacheData[access]=0
		
	nAccess=len(accesses)
	print(nAccess-hit)
	return hit/nAccess
	
def lru(accesses,nPages):
	cacheData=OrderedDict()
	
	hit=0
	for access in accesses:
	
		for p in [k for (k,v) in cacheData.items()]:
			print(p,end=' ')
		print('| '+access+(' Hit' if access in cacheData else ' Miss'))
		
		
		if(access in cacheData):
			hit+=1
			cacheData.pop(access)
			cacheData[access]= 0
		elif(len(cacheData)==nPages):
			cacheData.popitem(last=False)
		
		cacheData[access]= 0
	nAccess=len(accesses)
	print(nAccess-hit)
	return hit/nAccess
'''		
if(len(sys.argv)==1):
	exit(-1)

dataSize=int(sys.argv[1])
def run():
	data=[random.randint(1,dataSize) for i in range(1,dataSize + 1)]
	#data=[4,3,2,1,4,3,5,4,3,2,1,5]
	data=[fifo(data,pageSize) for pageSize in range(1, dataSize + 1)]
	return data

nRuns=100
runs=[]
for i in range(0,nRuns):
	runs.append(run())
	
avgRun=[]
for i in range(0,dataSize):
	avgRun.append(0)
	for j in range(0,nRuns):
		avgRun[ilru]+=runs[j][i]
	avgRun[i]/=nRuns
'''
data=[ 'A', 'B', 'C', 'D', 'A', 'B', 'E', 'A', 'B', 'C', 'D', 'E']

print(fifo(data,3))
print(lru(data,3))

#plt.plot(avgRun)
#plt.ylim([0,1])
#plt.show()

	
