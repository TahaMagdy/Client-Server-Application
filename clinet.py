'''
    * TCP/IP Client Server
'''
import socket
import Constants

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddress = ('localhost', Constants.PORT)
client.connect(serverAddress)


try:
    while True:
        # Send the message to the server
        message = input("Enter a Message to send to the server, Enter 0 to close\n")
        client.sendall(message.encode())
        print("MESSAGE IS SENT")


except:
    print("Client Exception")

# finally:
#     client.close()
