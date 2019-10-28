"""
Tim Hanneman
Federico Rubino

Programming Assignment #2
TCP Server
Using Multithreading

Why we use multithreading:
--------------------------
The reason is straightforward, we don’t want only a single client
to connect to our TCP server at a particular time but many clients
simultaneously, in this case two. We want our program to support multiple
clients at the same time. For this reason, we must use threads on the
server side, so that whenever a client request comes, a separate thread
can be assigned for handling each request.
This program is built specifically to handle two clients at once, but thanks
to multithreading it could handle more.

"""

#Imports that support tcp sockets, multithreading and pausing
from socket import *
from _thread import *
import threading
import time

#Variable Declarations (What! is this C or something???)
clients_message = list()
clients = list()

# threaded fuction
#Function that establishes the ability to keep multiple
#threads open at once
def threaded(c):

    global clients

    while True:
        # data received from client
        data = c.recv(1024).decode()
        
        if not data:
            print('Disconnecting with client')
            break
        
        new_message = ""
        new_message = data + " received"
        
        if data not in clients:
            clients_message.append(data)
            clients.append(c)
            
        #Threaded connection stays open until messages sent
        if len(clients) == 3:
            c.close()

"""
 Main method that does all the heavy lifting of this program
 It creates the different threads for the clients and stores all the
 relavant information.
 The server will stay open indefinitly until two clients have
 successfuly connected to it
 The server sends the messages received from the clients in uppercase
 as well as transforms the message to uppercase. It also sends an ACK
"""
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
        print (threading.currentThread().getName(), ': is Starting ')


        if len(clients) == 2:
            print("waiting")
            message = clients_message[0].upper() + " received before " + clients_message[1].upper()
            print(clients_message[0] + " received before " + clients_message[1])
            for c in clients:
                ack = "ACK"
                c.send(ack.encode())
                time.sleep(1)
                c.send(message.encode())
                print("Sent acknowledgement to both X and Y")
            #This increases the list size by one to ensure threads close
            clients.append(message)
            break

    serverSocket.close()


if __name__ == '__main__':
     Main()
