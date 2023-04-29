import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created")

port = 1997

sock.bind(('', port))
print("socket bound to port: ",port)


sock.listen(5)
print("listening for incoming connectections...")

while True:
    (client, address) = sock.accept()
    print("Client ", address, "has connected")
    client.send("Hello client".encode())
    client.close()
    break
