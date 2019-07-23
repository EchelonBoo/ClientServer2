#CLIENT 2

#Group C
#Bethany Hanrahan - K00230399
#David Chiemeka - K00228312

import socket															#this allows you to use python's socket library
import time																#this allows you to use python's time library

Client = socket.socket() 												#create a socket object and let it equal the the varable Client
Client.connect((socket.gethostbyname(socket.gethostname()), 13232))		#get the IP address for the host and set the port number

numbers = input("Please enter 4 numbers, one after the other: ")		#get the user to enter 4 numbers and save them in the variable numbers

Client.send(numbers.encode())											#send the user's input to the server to check if it is a power of 2

for i in range(4):														#for each number in a range of 4 numbers
	print('Answer is: ', Client.recv(1024).decode())					#print to the user the recieved answer 
	time.sleep(3)														#wait three seconds and repeat the loop