#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import sys
import re

def client(x,func_name):
	func_servers = {'A':12348,'B':12348,'C':12348,'D':12348,'E':12348}
	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = func_servers[func_name]                # Reserve a port for your service.

	s.connect((host, port))
	s.send(func_name+str(x))
	#try:
	ret = float(s.recv(1024))
	s.send("Value received")
	#except:
	#	print "Error"
	s.close()                     # Close the socket when done
	return ret


def A(x):
	return client(x,'A')

def B(x):
	return client(x,'B')

def C(x):
	return client(x,'D')

def D(x):
	return client(x,'D')

def E(x):
	return client(x,'E')

def main():
	f = open('input.txt','r')
	x_line = f.readline()
	x = float(re.match('x = (\w+)',x_line).group(1))
	for line in f:
		expression = line.replace(" ","")
		print line + " = "+str(eval(expression)).strip('\n')
	return




if __name__ == "__main__":
	main()