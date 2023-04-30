import socket
import threading
import sys

username = input('Enter Username: ')

address = str(sys.argv[1])
port = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((address,port))
except:
    print("Error connecting")

def read():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'ECE146':
                client_socket.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error: connection to server lost')
            client_socket.close()
            break

def write():
    while True:
        message = '<'+username+'> '+input('')
        client_socket.send(message.encode('utf-8'))

read_thread = threading.Thread(target=read)
write_thread = threading.Thread(target=write)

read_thread.start()
write_thread.start()