#SERVER 2

#Group C
#Bethany Hanrahan - K00230399
#David Chiemeka - K00228312

import socket 														#this allows you to use python's socket library
import time 														#this allows you to use python's time library
			
host = socket.gethostbyname(socket.gethostname()) 					#this gets the ip address of the network you are on and sets it as the host
port = 13232 														#this is set by the programmer, it is the port number we will be using to connect the client and server
			
print('The host IP is:', host) 										#prints the host to the user
print('The port number is:', port) 									#prints the port number to the user
			
def power_Func(x):  												#this declares a python function that will pass in a number and check if it is a power of 2
	if x == 2:	    												#if the number entered is 2, return true, it is a power of 2
		return True			
	elif x > 2:														#if the number is bigger than 2
		x /= 2														#divide it by two and then use recursion to keep dividing it by two
		return power_Func(x)										#if after being divided recursively it equals to two then its a power of 2
	else:			
		return False 												#if its not a power of two return false
		
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server2:  #create a socket object and specify that we're using IPv4 and TCP
	server2.bind((host, port))										#this associates the socket with the specific host address and port num
	server2.listen()												#this lets the server accept connections, the server is listening for a connection
	connection, address = server2.accept() 							#this creates a new socket object and allows a connection and address to be passed to it from the client
	with connection:		
		print('Connetion address', address) 						#prints back to the user on the server window, the connection address used when connected to the client
		info = connection.recv(1024) 								#this reads the data from the client and saves it in the info variable
		data = info.decode().split(" ")								#take everything recieved by the server from the client and split is at a space and save it as data
		for i in data:												#for each item in data
			connection.sendall(str(power_Func(int(i))).encode())	#check each number entered on the client side and send to the clientnt whether they are true or false
			time.sleep(3)											#this closes the window after 3 seconds