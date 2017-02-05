#!/usr/bin/python
import socket
import sys
import ssl
 
##### DEFINING THE ARGUMENTS 
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) == 4:
    sys.argv[1] == "-s"
    PORT = 27994
    HOST = sys.argv[2] 
    NEU_ID = sys.argv[3]
    ssl_sock = ssl.wrap_socket(sock)
    sock = ssl_sock
     
elif len(sys.argv) == 5:
    sys.argv[1] == "-p" 
    PORT = sys.argv[2]
    HOST = str(sys.argv[3])
    NEU_ID = str(sys.argv[4])

elif len(sys.argv) == 6:
    sys.argv[1] == "-p"
    sys.argv[3] == "-s"
    PORT = sys.argv[2]
    HOST = str(sys.argv[4])
    NEU_ID = str(sys.argv[5])
    ssl_sock = ssl.wrap_socket(sock)
    sock = ssl_sock

else:
   PORT = 27993
   HOST = str(sys.argv[1])
   NEU_ID = str(sys.argv[2])

    
##### CREATING CLIENT SOCKET WITH TCP & IPV4 CAPABILITY
try:

#    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sock.connect((HOST, int(PORT)))

#except socket.gaierror:
 #   print "Name Error"

    message = "cs5700spring2017" + " " + "HELLO" + " " + NEU_ID + "\n"

    while True:
   
        sock.send(message)
        expression = sock.recv(65535)
   # print expression


##### FUNCTION TO CONVERT SERVER'S STATUS MESSAGE INTO A LIST[], PARSE ELEMENTS AND PERFORM CALCULATION 

        def parse(expression):

            expression.split()
       #print expression.split()

            if len(expression.split()) in (3,5):

                if expression.split()[2] == "BYE":
           #print exp.split()[2]
                    return "SUCCESS"

                number1 = int(expression.split()[2])
                number2 = int(expression.split()[4])
                math_operator = expression.split()[3]

                return {'+': number1 + number2, '-': number1 - number2, '/': number1 / number2, '*': number1 * number2}.get(math_operator, "NOT VALID")

            else:

                return "ERROR"

##### CALL THE FUNCTION TO SEND THE SOLUTION BACK TO THE SERVER

        reply = parse(expression)
    #print reply

        message = "cs5700spring2017" + " " + str(reply) + "\n"
    #print message

        if reply == "SUCCESS":
                print (expression.split()[1])
                break

        elif reply == "ERROR":
                print "SOMETHING WENT WRONG."
                break

except (socket.gaierror, ssl.SSLError, socket.error):
    print "check Host Name or PORT Number or NEU_ID"

sock.close()
