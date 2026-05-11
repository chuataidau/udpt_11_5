import socket
import threading

HOST = '0.0.0.0'
PORT = 8080

def handle_client(conn, addr):
    print(f"Client connected: {addr}")

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            print(f"Received from {addr}: {data}")

            parts = data.strip().split()

            if len(parts) == 3:
                command, a, b = parts
                a, b = int(a), int(b)

                if command == "ADD":
                    result = a + b
                    response = f"RESULT {result}"
                else:
                    response = "ERROR Unknown command"
            else:
                response = "ERROR Invalid format"

            conn.send(response.encode())

        except:
            break

    print(f"Client disconnected: {addr}")
    conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Server running on port {PORT}...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    main()