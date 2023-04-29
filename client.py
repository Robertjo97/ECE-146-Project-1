import socket
import sys

sock = socket.socket()

address = str(sys.argv[1])
port = int(sys.argv[2])

sock.connect((address, port))

print (sock.recv(1024).decode())

#sock.close()

'''while True:
	print("Press f to disconnect")
	choice = input()
	if choice == 'f':
		sock.close()
		break'''
