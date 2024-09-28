import socket
import threading

client_socket = None # a globlal client so we can initioalise and work with later

def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected to the server")

    threading.Thread(target=receive_messages).start() #this method helps us receive message form server thread without blocking any other incomming or out going

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Message receive: {message}")
        except:
            break


def on_message_received(message):  
    pass

def send_message(message):
    if client_socket:
        client_socket.send(message.encode())