"""
Tim Hanneman
Federico Rubino

Programming Assignment #2

Client Y: Tim

"""

# In your command prompt, type in hostname and press enter.
# What comes up is your computer's hostname


from socket import *

serverName = 'localhost'

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

sentence = "Client Y: Tim"

clientSocket.send(sentence.encode())

print("Sent to Server:", sentence)
print()

ack = clientSocket.recv(1024)
modifiedSentence = clientSocket.recv(1024)


print('Acknowledgement from Server:', ack.decode())
print('Server message:', modifiedSentence.decode())


clientSocket.close()
