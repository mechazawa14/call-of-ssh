import socket 

client  = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

# client.bind(("127.0.0.1", 0))  # Bind to any available port actually useless as os chooses a random port for us, but we can use it to see what port was chos
# bind line is only used for servers generally not clients 
# The only time you bind a client is if you have 2 WiFi cards and you want to force it to use a specific one, or firewall rules. 

client.connect(("127.0.0.1", 5000))

print("Connected to server at 127.0.0.1:5000")
client.send(b"call of ssh is successfully underway!")
