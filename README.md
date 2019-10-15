# CST_311
Class Projects


Assignment #2
-------------

One server that uses multi threading to allow multiple clients to send messages to it.

Two clients, X and Y, that send messages to the server.


Grading Criteria:

Specifically, your client program should
(1) (10 points) You must use TCP sockets; you will need to establish a connection first, since it is a connection oriented protocol.
(2) (10 points) Clients must initiate the connection by sending their messages to the server.
(3) (10 points) Server receives messages from both clients and establishes which message it received first.
(4) (10 points) Server sends acknowledgements to both clients stating which message was received first.
(5) (10 points) The server must accept connections from both clients first before receiving the messages from either client.
(6) (10 points)The response string from Server to Clients (“X: Alice received before Y: Bob”, or “Y: Bob received before X: Alice”) must be in the order the messages from Client X or Client Y are received and NOT the order in which the clients X and Y connected to the server. 

Note: You will need multithreading and a way to share data between threads to achieve this.

(7) (10 points) Your program should print out the messages sent by the client at both the client and server and vice versa for messages sent by the server.

(8) (10 points) Execute your programs on your mininet virtual machine.
(9) (10 points) At the top of your server code, in a comment explain why you need multithreading to solve this problem.
(10) (10 points) Program must be well documented.

Optional Extra Credit for the future:
(10 points) Clients X and Y can only chat through the server. For example, every message that client X sends to the server, the server relays to client Y and vice versa. 
(5 points) When a client (say X) wants to exit the chat service it sends a “Bye” message. When a server sees a “Bye” message, it relays this message to Y and then terminates the connection to both clients. 
(5 points) Each client (say X) should output the messages sent by it and those received from Y. As this is a chat service the number/content of messages exchanged is not fixed. So your clients should have the capability to accept inputs (which are the content of the messages) from the keyboard. 

#END of Assignment #2
---------------------
