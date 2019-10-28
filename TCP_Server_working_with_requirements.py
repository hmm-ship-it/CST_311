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

# method that establsihes the ability to keep multiple
# threads open at once
def tcp_connection_thread(c):
    print('tcp_function_started')
    while True:
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()
"""
 Main method that does all the heavy lifting of this program
 It creates the different threads for the clients and stores all the
 relavant information into lists
 The server will stay open indefinitly until two clients have
 successfuly connected to it
 The server sends the messages received from the clients in uppercase
 as well as transforms the message to uppercase. It also sends an ACK
"""
def Main():
    threads_list = list()
    thread_state = True
    clients_count = 0
    clients = list()
    clients_message = list()

    serverPort = 12000
    servername = '127.0.0.1'
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((servername,serverPort))
    print('The server is ready to receive')

    while clients_count < 2:
        serverSocket.listen(1)
        connectionSocket, addr = serverSocket.accept()
        print('Connected to :', addr[0], ':', addr[1])

        t1 = threading.Thread(target=tcp_connection_thread, args=(connectionSocket,))
        #threads_list.append(t1)
        t1.start()
        print('tcp_thread_started')
        clients_count = clients_count + 1

        data = connectionSocket.recv(1024).decode()
        new_message = ""
        new_message = data + " received"
        if data not in clients:
            #print("data is!!!" + str(data), flush=True)
            clients_message.append(data)
            clients.append(connectionSocket)


        if clients_count == 2:
            print("waiting")
            message = clients_message[0].upper() + " received before "+ clients_message[1].upper()
            print ( clients_message[0] + " received before "+ clients_message[1])
            for c in clients:
                c.send("ACK".encode())
                # the sleep helps the clients receive the msg better
                time.sleep(1)
                c.send(message.encode())
            print("Sent acknowledgment to both X and Y ")
    serverSocket.close()

if __name__ == '__main__':
    Main()
