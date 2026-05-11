import socket

HOST = '127.0.0.1'
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server")

while True:
    msg = input("Enter command (e.g., ADD 3 5): ")

    client.send(msg.encode())

    response = client.recv(1024).decode()
    print("Server:", response)