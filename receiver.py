#RISHAB KSHATRI PES2UG19CS327
#GOURAV ARAVINDA PES2UG19CS130
#SRIVATSAN NARENDIRAN PES2UG19CS408
#TEJAS REDDY PES2UG19CS308
#receiver code to stream the data

import socket
#host on what we run
HOST = 'localhost'
PORT = 6100
#port no on which we run


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connecting the host to the port
s.connect((HOST, PORT))
#starting while loop to get data iteratively and print the stream of data
while True:
    data = s.recv(1024)
    print (repr(data))

s.close()
#CODE TO PRINT THE STREAM ON THE TERMINAL

