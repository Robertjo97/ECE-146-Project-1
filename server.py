import threading
import socket
import sys

address = ''
port = int(sys.argv[1])

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((address, port))
server_sock.listen()

clients = []
names = []

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast(name.encode('ascii')+' has left the chat'.encode('ascii'))
            names.remove(name)
            break

def receive():
    while True:
        client, address = server_sock.accept()
        print(str(address), 'has connected')

        client.send('NICK'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        names.append(name)
        clients.append(client)

        print('Name of client is',name)
        broadcast(name.encode('ascii')+' has joined the chat'.encode('ascii'))
        client.send('Connection successful'.encode('ascii'))

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

receive()
