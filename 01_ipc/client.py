import socket

HOST = "127.0.0.1"
PORT = 4568

def sendable_data(data):
    return str(data).encode("utf-8")


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Client connected to the server using the host %s and port %d" % (HOST, PORT))
        # ---------------
        a,b = input("Enter 2 numbers: ").split()
        s.sendall(sendable_data(a))
        s.sendall(sendable_data(b))

        data = s.recv(1024)
    print(f'Addition of 2 numbers: {data.decode("utf-8")}')
