import socket
import threading
import time


class ChatServer:
    def __init__(self, host, port, server_name):
        self.clients = {}  # Store clients with their usernames
        self.server_name = server_name
        self.host = host
        self.port = port
        self.running = True

    def broadcast_presence(self):
        """Broadcasts server name and address for network discovery."""
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        broadcast_message = f"SERVER:{self.server_name}:{self.host}:{self.port}"
        while self.running:
            udp_sock.sendto(broadcast_message.encode(), ('<broadcast>', 37020))
            time.sleep(2)

    def handle_client(self, client_socket):
        """Handles messaging, DM, and online user listing for each client."""
        # First message should be the username
        username = client_socket.recv(1024).decode()
        self.clients[client_socket] = username
        print(f"[CONNECTION] {username} has joined the server.")

        while self.running:
            try:
                message = client_socket.recv(1024).decode()
                if message.startswith("/dm"):
                    self.handle_dm(client_socket, username, message)
                elif message == "/ou":
                    self.list_online_users(client_socket)
                else:
                    print(f"[MESSAGE] {username}: {message}")
                    self.broadcast(f"{username}: {message}", client_socket)
            except:
                print(f"[DISCONNECTED] {username} has left.")
                self.clients.pop(client_socket, None)
                break

    def handle_dm(self, sender_socket, sender_username, message):
        """Handles direct messaging between users."""
        try:
            _, recipient_username, dm_message = message.split(' ', 2)
            recipient_socket = None
            for client, username in self.clients.items():
                if username == recipient_username:
                    recipient_socket = client
                    break

            if recipient_socket:
                dm_message_formatted = f"[DM from {sender_username}] {dm_message}"
                recipient_socket.send(dm_message_formatted.encode())
                sender_socket.send(f"[DM to {recipient_username}] {dm_message}".encode())
            else:
                sender_socket.send(f"[ERROR] User '{recipient_username}' not found.".encode())
        except ValueError:
            sender_socket.send("[ERROR] Invalid DM format. Use: /dm <username> <message>".encode())

    def list_online_users(self, client_socket):
        """Sends the list of online users to the requesting client."""
        user_list = "\n".join(self.clients.values())
        client_socket.send(f"[ONLINE USERS]\n{user_list}".encode())

    def broadcast(self, message, sender_socket):
        """Broadcast message to all connected clients."""
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message.encode())
                except:
                    self.clients.pop(client, None)

    def start(self):
        """Starts the chat server."""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen()
        print(f"Server '{self.server_name}' running on {self.host}:{self.port}...")

        # Start broadcasting for discovery
        broadcast_thread = threading.Thread(target=self.broadcast_presence)
        broadcast_thread.start()

        while self.running:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def stop(self):
        self.running = False


# Start the server with a name
if __name__ == "__main__":
    host = socket.gethostbyname(socket.gethostname())
    port = 12345
    server_name = input("Enter the server name: ")
    chat_server = ChatServer(host, port, server_name)
    try:
        chat_server.start()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        chat_server.stop()




