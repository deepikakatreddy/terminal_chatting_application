# chat_server.py
import socket
import threading

# Function to handle client connections
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                print(f"[{addr}] {msg}")
                broadcast(msg, client_socket)
            else:
                connected = False
        except:
            connected = False

    client_socket.close()

# Function to broadcast messages to all clients
def broadcast(msg, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(msg.encode('utf-8'))
            except:
                clients.remove(client)

# Main function to start the server
def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

# Server setup
SERVER = "127.0.0.1"
PORT = 5555
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

print("[STARTING] Server is starting...")
start_server()
