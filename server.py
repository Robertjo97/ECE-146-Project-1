import socket
import threading
import sys

address = ''
port = int(sys.argv[1])

client_list = []
usernames = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created on port', port)
server_socket.bind((address, port))
server_socket.listen()
print("Listening...")

def broadcast(message):
    for client in client_list:
        client.send(message)

def manage(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client_list.index(client)
            username = usernames[index]
            client_list.remove(client)
            usernames.remove(username)
            client.close()
            broadcast(username.encode('utf-8')+' has left the chat'.encode('utf-8'))
            print(username+' has disconnected')
            print("Current client count:",len(client_list))
            break

while True:
    print("Current client count:", len(client_list))
    client, client_address = server_socket.accept()
    
    print("Connection from",client_address)
    client.send('ECE146'.encode('utf-8'))
    username = client.recv(1024).decode('utf-8')
    usernames.append(username)
    client_list.append(client)
    print('Name of client is', username)

    broadcast(username.encode('utf-8')+' has joined the chat.'.encode('utf-8'))
    client.send('Welcome '.encode('utf-8')+username.encode('utf-8')+'!'.encode('utf-8'))

    client_thread = threading.Thread(target=manage,args=(client,))
    client_thread.start()


