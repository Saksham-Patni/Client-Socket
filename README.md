# Client-Socket
Licensed under the [MIT License](LICENSE)
Client Socket to Solve Simple Mathematical Equations

The program can be initiated be the following command with specific arguments
./client <-p PORT> -s [HOST] [ID]


This is a client program which communicates with the server using IPv4 TCP socket. Once connected the server identifies the client and shoots thousands of simple mathematical expressions. The client program returns the solution and waits for server's response with either another expression or a BYE message with a secret flag. 


The client program is implemented as follows:
1. Import socket modules.
2. Create an IPV4 TCP socket.
3. Get the server's IP.
4. Connect the socket with server IP and port number
5. Once connected, send HELLO message to the server using that socket.
6. Lisen for the server's response.

Parsed the response into seperate elements. Compare elements with their index and performed mathematical operation of '+', '-', '/', '*' respectively. Used defensive coding to check for valid operation.  

The calculated expression is sent back to the server in a particular format, wait untill the server sends BYE with asecret flag.

Once recieved, the socket is closed. Otherwise carried out the same operation.

=============================================

Testing:

The code is verified step by step:
1. Sending the HELLO message
2. Receiving the STATUS expression
3. Returning the SOLUTION
4. Receiving another STATUS or BYE message

==============================================   

