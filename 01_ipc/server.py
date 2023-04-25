import socket

HOST = "127.0.0.1"
PORT = 4568


def sendable_data(data):
    return str(data).encode("utf-8")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Server binded to the host %s and port %d" %(HOST,PORT))
    s.listen()
    # --------------------- wait for client
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        print(conn)
        data = conn.recv(1024)
        data2 = conn.recv(1024)
        print("Data 1 received from client:",data.decode("utf-8"))
        print("Data 2 received from client:",data2.decode("utf-8"))

        a = int(data.decode("utf-8"))
        b = int(data2.decode("utf-8"))
        conn.sendall(sendable_data(a + b))
