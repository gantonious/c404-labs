import socket
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(("0.0.0.0", 8000))
server_socket.listen(5)

while True:
    (incomingSocket, address) = server_socket.accept()
    print("Incomming connection from {}".format(address))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("www.google.com", 80))

    incomingSocket.setblocking(0)
    client_socket.setblocking(0)

    if os.fork() != 0:
        while True:
            request = bytearray()
            while True:
                try:
                    part = incomingSocket.recv(1024)
                except IOError, e:
                    if e.errno == socket.errno.EAGAIN:
                        part = None
                    else:
                        raise
                if part:
                    client_socket.sendall(part)
                    request.extend(part)
                else:
                    break
            
            if request:
                print(request)

            response = bytearray()
            while True:
                try:
                    part = client_socket.recv(1024)
                except IOError, e:
                    if e.errno == socket.errno.EAGAIN:
                        part = None
                    else:
                        raise
                if part:
                    incomingSocket.sendall(part)
                    response.extend(part)
                else:
                    break

            if response:
                print(response)