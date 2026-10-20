import socket 

client  = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

# client.bind(("127.0.0.1", 0))  # Bind to any available port actually useless as os chooses a random port for us, but we can use it to see what port was chos
# bind line is only used for servers generally not clients 
# The only time you bind a client is if you have 2 WiFi cards and you want to force it to use a specific one, or firewall rules. 

client.connect(("127.0.0.1", 5000))

print("Connected to server at 127.0.0.1:5000")
client.send(b"hello from client!")  # Send a message to the server, encoding the string to bytes using UTF-8

reply = client.recv(1024)
print("server:", reply.decode('utf-8'))  # Decode the bytes to a string using UTF-8 encoding and print the received message

    
