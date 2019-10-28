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

# Imports that support tcp sockets, multithreading and pausing
from socket import *
from _thread import *
import threading
import time

# Variable Declarations (What! is this C or something???)
clients_message = list()
clients = list()
number_of_clients = 0
'''
This last variable is used because question 5 requires both
clients to connect before receiving the messages from client, a
quick if statement took care of it
'''

# threaded fuction
# Function that establishes the ability to keep multiple
# threads open at once
def threaded(c):

    global clients

    while True:
        # data received from client
        # Use this for point 5 if needed
        if number_of_clients == 2:
            data = c.recv(1024).decode()

            if not data:
                print('Disconnecting with client')
                break

            if data not in clients:
                clients_message.append(data)
                clients.append(c)

            # Threaded connection stays open until messages sent
            # This may be redundant code to the 'if not data:' above
            if len(clients) == 3:
                c.close()

        '''
        #If the above is commented out below will work
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
        #Just leave this here
        '''
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
    global number_of_clients
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

    # Will only run for two clients
    while len(clients) < 2:

        connectionSocket, addr = serverSocket.accept()
        number_of_clients += 1
        print('Connected to :', addr[0], ':', addr[1])

        # This is where all the threading happens
        t1 = threading.Thread(target=threaded, args=(connectionSocket,))
        threads_list.append(t1)
        t1.start()
        t1.join(1)
        print(threading.currentThread().getName(), ': is Starting ')

        # This happens when the two clients have made a connection
        # This bit of code deals with sending the
        # messages and tearing down the connection.
        if len(clients) == 2:
            print("waiting")

            # The message that is sent
            message = clients_message[0].upper() + " received before " + clients_message[1].upper()
            print(clients_message[0] + " received before " + clients_message[1])
            # Sends the ACK and message to each client
            for c in clients:
                ack = "ACK"
                c.send(ack.encode())
                time.sleep(1)
                c.send(message.encode())
                print("Sent acknowledgement to both X and Y")
            # This increases the list size by one to ensure threads close
            clients.append(message)
            break

    serverSocket.close()


if __name__ == '__main__':
    Main()

