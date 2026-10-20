import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# creating a socket which is basically an endpoint for communication. AF_INET is the address family for IPv4 and SOCK_STREAM 
# means it is a TCP socket, basically Create a TCP socket that works with IPv4.

server_socket.bind(("127.0.0.1", 5000))


server_socket.listen()

print("Call of SSH listening on 127.0.0.1:5000...")

input("Press Enter to stop server...")

# 127.0.0.1:5000 specifically means only accept connections reaching port 5000 through loopback. Later 192.168.1.11:5000 lets us 
# expose it through your Wi-Fi address, and 0.0.0.0:5000 can mean listening on port 5000 across suitable local IPv4 interfaces.