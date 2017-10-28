'''
    * TCP/IP Client Server
'''
import socket
import Constants

# creating TCP/IP Socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind mySocket to a port
# You can't bind to port numbers lower than 1024 as a unprivileged user.
address = ('localhost', Constants.PORT)
mySocket.bind(address)


# Putting mySocket into server mode. BUT it does not wait
mySocket.listen(1)


print('waiting for connection')
# The connection is actually a different socket on another port
# (assigned by the kernel)
# It's like scanf, But for connections
connection, clientAddress = mySocket.accept()

while True:
    print("\nI've got a connection")
    # recv(bufsize); maximum amount of data to be received at once
    data = connection.recv(100)
    print(data)

    # Send the databack
    if data:
        print("Hello Client, Address is ", clientAddress)
        # connection.sendall(data)
    else:
        print("No Data")
        break

# connection.close()
