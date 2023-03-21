import socket

HOST = '192.168.1.177'
PORT = 12345

s = socket.socket()
s.connect((HOST, PORT))
res = s.recv(1024).decode()
print(res)

s.sendall(input("Enter Message: ").encode("utf-8"))

s.close()