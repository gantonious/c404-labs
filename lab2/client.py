import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("www.google.com", 80))

request = "GET / HTTP/1.0\r\n\r\n"
client_socket.send(request)

response = bytearray()
while True:
    part = client_socket.recv(1024)
    if part:
        response.extend(part)
    else:
        break

print(response)