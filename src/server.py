import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# creating a socket which is basically an endpoint for communication. AF_INET is the address family for IPv4 and SOCK_STREAM 
# means it is a TCP socket, basically Create a TCP socket that works with IPv4.

# server_socket.bind(("127.0.0.1", 5000))
server_socket.bind(("192.168.1.11", 5000)) #this is ip of another device in the same network, were trying same lan connection.


server_socket.listen()

print("Call of SSH listening on 192.168.1.11:5000...")

connection, address = server_socket.accept()

print("Peer connected!")
print("Peer address:", address)

# print(connection.recv(1024))  # Receive data from the client, up to 1024 bytes

data = connection.recv(1024)  # Receive data from the client, up to 1024 bytes
message = data.decode('utf-8')  # Decode the bytes to a string using UTF-8 encoding
print("peer:", message)  # Print the received message

reply = "hello from server!"
connection.send(reply.encode('utf-8'))  # Send a reply back to the client, encoding the string to bytes using UTF-8


# 127.0.0.1:5000 specifically means only accept connections reaching port 5000 through loopback. Later 192.168.1.11:5000 lets us 
# expose it through your Wi-Fi address, and 0.0.0.0:5000 can mean listening on port 5000 across suitable local IPv4 interfaces.


