#!/usr/bin/python           # This is server.py file
import math

def func_A(recv):
	return float(recv[1:])**2

def func_B(recv):
	return (float(recv[1:])*10)

def func_C(recv):
	return (float(recv[1:])+20)

def func_D(recv):
	return math.log(float(recv[1:]),10)

def func_E(recv):
	return math.sqrt(float(recv[1:]))

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12348             # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
ret_func = {'A':func_A,'B':func_B,'C':func_C,'D':func_D,'E':func_E}
s.listen(5)                 # Now wait for client connection.
while True:
	c, addr = s.accept()     # Establish connection with client.
	print 'Got connection from', addr
	#c.send('Thank you for connecting')
	recv = c.recv(1024)
	print recv
	if recv[0] in ('A','B','C','D','E'):
		ret_value = str(ret_func[recv[0]](recv))
		print ret_value
		c.send(ret_value)
	else:
		c.send("Please choose a correct option")
	print c.recv(1024)
	c.close()                # Close the connection