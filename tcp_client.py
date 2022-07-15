import socket

target_host = "www.google.com"
target_port = 80
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client :

    client.connect((target_host, target_port))

    client.send(b"GET / HTTP/1.1 \r\nHost: google.com\r\n\r\n")

    print(client.recv(4096).decode())
