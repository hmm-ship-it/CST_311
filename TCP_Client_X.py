"""
Tim Hanneman
Federico Rubino

Programming Assignment #2

Client X: Federico

"""

# In your command prompt, type in hostname and press enter.
# What comes up is your computer's hostname


from socket import *

serverName = 'localhost'

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

sentence = "Client X: Federico"

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)

print ('From Server:', modifiedSentence.decode())

clientSocket.close()

