import socket

server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen()
print("Server listening on 127.0.0.1:5000")
input("Press Enter to stop server...")  