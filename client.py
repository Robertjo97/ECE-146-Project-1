import socket
import threading
import sys

name = input('Enter your name: ')

address = str(sys.argv[1])
port = int(sys.argv[2])

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((address,port))

def receive():
    while True:
        try:
            msg = client_sock.recv(1024).decode('ascii')
            if msg == 'NICK':
                client_sock.send(name.encode('ascii'))
            else:
                print(msg)
        except:
            print('Error')
            client_sock.close()
            break

def write():
    while True:
        message = name+': '+input('')
        client_sock.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()