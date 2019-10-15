"""
Tim Hanneman
Federico Rubino

Assignment 2

ServerTCP.py
"""



from socket import *
serverPort = 12000
servername = '127.0.0.1'

# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET,SOCK_STREAM)

# Assign IP address and port number to socket
serverSocket.bind((servername,serverPort))
serverSocket.listen(1)

print ('The server is ready to receive')

while True:

     connectionSocket, addr = serverSocket.accept()

     sentence = connectionSocket.recv(1024).decode()


     # this checks for different client messages
     print (sentence)
     new_message = ""

     if 'X' in sentence:
          new_message = sentence + " received before Y:Tim"
     else:
          new_message = sentence + " received before X:Federico"

     connectionSocket.send(new_message.encode())



#     capitalizedSentence = sentence.upper()

#     connectionSocket.send(capitalizedSentence.encode())

     connectionSocket.close()
