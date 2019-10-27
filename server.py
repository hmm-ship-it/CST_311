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

#print_lock = threading.Lock()
clients_message = list()
clients = list()


# thread fuction
def threaded(c):
    print('enter thread')
    # lock acquired by client
    #print_lock.acquire()
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
        #print( "Received:", data, flush=True)
        new_message = ""

        new_message = data + " received"

        if data not in clients:
            print("data is!!!" + str(data), flush=True)
            clients_message.append(data)
            clients.append(c)
            #print(len(clients), flush=True)

            #    c.send(new_message.encode())

            # close thread

            # connection closed

        #print_lock.release()
        print("unlock", flush=True)
    c.close()


def Main():
    global clients
    serverPort = 12000
    servername = '127.0.0.1'
    threads_list = []

    # Create a TCP socket
    # Notice the use of SOCK_STREAM for TCP packets
    serverSocket = socket(AF_INET,SOCK_STREAM)

    # Assign IP address and port number to socket
    serverSocket.bind((servername,serverPort))
    serverSocket.listen(1)

    print ('The server is ready to receive')

    while len(clients) < 2:

        connectionSocket, addr = serverSocket.accept()
        print('Connected to :', addr[0], ':', addr[1])

        t1 = threading.Thread(target=threaded, args=(connectionSocket,))
        threads_list.append(t1)
        t1.start()
        print (threading.currentThread().getName(), 'Starting')
        print('after the thread is started \n\n' + str(len(clients)) + " Length of clients")


        if len(clients) == 2:
            print("waiting")
            #t1.join
            ack_message = clients_message[0] + "received before " + clients_message[1]
            for c in clients:
                c.send(ack_message.encode())
            break


    serverSocket.close()


if __name__ == '__main__':
     Main()
