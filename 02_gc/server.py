import socket
import os
from _thread import *

HOST = '127.0.0.1'
PORT = 2004
ThreadCount = 0


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        print("Recieved message: " + data.decode('utf-8') + " from Thread: " + str(ThreadCount))
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print("Server binded to the host %s and port %d" %(HOST,PORT))
        s.listen(5)

        while True:
            Client, address = s.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(multi_threaded_client, (Client, ))
            ThreadCount += 1
            print('Thread Number: ' + str(ThreadCount))