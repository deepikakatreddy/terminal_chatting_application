# chat_client.py
import socket
import threading

# Function to handle receiving messages from the server
def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg:
                print(msg)
        except:
            print("[ERROR] An error occurred.")
            client.close()
            break

# Function to handle sending messages to the server
def send_messages():
    while True:
        msg = input()
        client.send(msg.encode('utf-8'))

# Client setup
SERVER = "127.0.0.1"
PORT = 5555
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print("[CONNECTED] Connected to the server.")

# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
