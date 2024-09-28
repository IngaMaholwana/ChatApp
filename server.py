import socket # this creates network connection without it threading is hard
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind('localhost', 12345)
server_socket.listen()

clients = []

def accept_connections():
    """keep track of all the clients """
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)

        print(f"Connection from {client_address}")

        threading.Thread(target=handle_client, args=(client_socket)).start()

def handle_client(client_socket):
    """handles the client socket using bytes"""        
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Received message: {message}")
                broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break       

def broadcast(message, sender_socket):       
    """will send message to all in network connections"""  
    for client in clients:
        if client !=sender_socket:
            try:
                client.send(message.decode())


            except:
                client.remove(client)


def start_server():
    """this defines the accept function in a new thread"""
    server_thread = threading.Thread(target=accept_connections)
    server_thread.daemon=True #this ensures it exists when the server is up and running
    server_thread.start()


if __name__ == "__main__":
    print("server running...")
    start_server()
    while True:
        pass    
