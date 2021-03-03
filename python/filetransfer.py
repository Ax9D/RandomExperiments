'''
UI wrapper around netcat to facilitate file transfer
'''
import os

def receive(fname):
	port=input("Enter port: ")
	os.system("nc -vv -l -p "+port+" > "+fname)
	
def send(fname):
	ip=input("Enter ip to send to: ")
	port=input("Enter port: ")
	os.system("pv "+fname+" | nc -vv -n "+ip+" "+port)

choice=input("Do you want to send or receive? [S=Send, R=Receive] ")
fname=input("Enter file name: ")
if(choice=="R" or choice=="r"):
	receive(fname)
elif(choice=="S" or choice=="s"):
	send(fname)
else:
	print("Baka desu ka?")
