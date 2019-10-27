"""
Tim Hanneman
Federico Rubino

Assignment 2

ServerTCP.py
"""


# import socket
from socket import *


# import thread module
from _thread import *
import threading

print_lock = threading.Lock()
clients_message = list()
clients = list()

# thread fuction
def threaded(c):
    global clients

# TODO: I should keep this in a while loop until both clients have been
# received
# I should make a list of the clients to send the messages back at once
    while True:
        # data received from client
        data = c.recv(1024).decode()
        if not data:
            print('Disconnecting with client')

            # lock released on exit
            break

        # reverse the given string from client
        # data = data[::-1]
        print( "Received:", data)
        new_message = ""

        new_message = data + " received"

        if data not in clients:
            clients_message.append(data)
            clients.append(c)

            #    c.send(new_message.encode())

            # close thread

            # connection closed

        print_lock.release()
    c.close()


def Main():
    global clients

    serverPort = 12000
    servername = '127.0.0.1'

    # Create a TCP socket
    # Notice the use of SOCK_STREAM for TCP packets
    serverSocket = socket(AF_INET,SOCK_STREAM)

    # Assign IP address and port number to socket
    serverSocket.bind((servername,serverPort))
    serverSocket.listen(1)

    print ('The server is ready to receive')

    while len(clients) < 2:

        connectionSocket, addr = serverSocket.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        start_new_thread(threaded, (connectionSocket,))

        if len(clients) == 2:
            print(clients_message[0], "received before", clients_message[1])
            for c in clients:
                c.send("ACK".encode())
            break


    serverSocket.close()


if __name__ == '__main__':
     Main()
