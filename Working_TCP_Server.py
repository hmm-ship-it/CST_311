from socket import *
from _thread import *
import threading

def tcp_connection_thread(c):
     print('tcp_function_started')
     while True:
          sentence = connectionSocket.recv(1024).decode()
          capitalizedSentence = sentence.upper()
          connectionSocket.send(capitalizedSentence.encode())
          connectionSocket.close()
          
def Main():
     threads_list = []
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
          t1.start
          print('tcp_thread_started')
          clients_count = clients_count +1

          data = connectionSocket.recv(1024).decode()
          new_message = ""
          new_message = data + " received"
          if data not in clients:
            #print("data is!!!" + str(data), flush=True)
            clients_message.append(data)
            clients.append(connectionSocket)
          

          if clients_count == 2:
            print("waiting")
            print(clients_message[0], "received before", clients_message[1])
            for c in clients:
                c.send("ACK".encode())
                           
if __name__ == '__main__':
     Main()
