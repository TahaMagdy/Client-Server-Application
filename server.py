'''
    * TCP/IP Client Server
'''
import socket

# creating TCP/IP Socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind mySocket to a port
# You can't bind to port numbers lower than 1024 as a unprivileged user.
address = ('localhost', 1052)
mySocket.bind(address)


# Putting mySocket into server mode. BUT it does not wait
mySocket.listen(1)


while True:
    print('waiting for connection')
    # The connection is actually a different socket on another port
    # (assigned by the kernel)
    connection, clientAddress = mySocket.accept()
