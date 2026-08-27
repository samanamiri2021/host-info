import socket

print("Hostname:", socket.gethostname())
print("Local IP:", socket.gethostbyname(socket.gethostname()))
