import socket

HOST = '192.168.1.161'
PORT = 12345

s = socket.socket()
s.connect((HOST, PORT))

while True:
	res = s.recv(1024).decode()
	if res is None:
	    continue
	print(res)
	s.sendall(input("Enter Message: ").encode("utf-8"))

s.close()