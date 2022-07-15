import socket
import threading

ip = "0.0.0.0"
port = 8080


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(f"[*] listning on {ip} : {port}")
    while True:
        client, address = server.accept()
        print(client, "\n", address)
        print(f"[*] Accepted connection from {address[0]} : {address[1]}")
        client_handler = threading.Thread(target=handle_client, args=[client])
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Recived : {request.decode('utf-8')}")
        sock.send(b'ACK')
if __name__ == "__main__":
    main()