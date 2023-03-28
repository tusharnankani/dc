import socket

s = socket.socket()
print ("socket successfully created")

port = 12345

s.bind(('', port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening")

connections = []

while True:

    c, addr = s.accept()
    print ('Got connection from', addr )
    c.send('Thank you for connecting with the server'.encode())
    
    connections.append((c, addr))
    msg = c.recv(1024).decode()
    
    for (c, addr) in connections:
    	c.send(f"Message from {addr}: {msg}".encode())
    
    if len(connections) > 2:
    	break
    
for (c, addr) in connections:
    print(f"Closing ({addr})")
    c.close()

s.close()
