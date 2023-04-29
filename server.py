import socket
import sys
import threading

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created")

port = int(sys.argv[1])

sock.bind(('', port))
print("socket bound to port: ",port)


sock.listen(5)
print("listening for incoming connectections...")

client_count = 0

while True:
    print("Current client count: ",client_count)
    (client, address) = sock.accept()
    print("Client ", address, "has connected")
    client_count = client_count + 1
    client.send("Hello client".encode())
    client.close()
    break
