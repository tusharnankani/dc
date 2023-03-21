import socket

HOST = '127.0.0.1'
PORT = 2004

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Client connected to the server using the host %s and port %d" % (HOST, PORT))

        res = s.recv(1024)
        while True:
            Input = input('Enter your message: ')
            s.send(str.encode(Input))
            res = s.recv(1024)
            print(res.decode('utf-8'))