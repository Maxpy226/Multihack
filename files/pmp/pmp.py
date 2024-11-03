import os
import socket
import threading
import time

class ChatClient:
    def __init__(self):
        self.server_address = None
        self.running = True
        self.username = None

    def discover_servers(self):
        """Discover available servers on the network."""
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        udp_sock.bind(("", 37020))
        udp_sock.settimeout(5)

        servers = {}
        print("[DISCOVER] Looking for servers on the network...")
        try:
            start_time = time.time()
            while time.time() - start_time < 5:
                try:
                    data, addr = udp_sock.recvfrom(1024)
                    decoded_message = data.decode()
                    if decoded_message.startswith("SERVER"):
                        _, server_name, host, port = decoded_message.split(":")
                        servers[(host, int(port))] = server_name
                        print(f"Found server: {server_name} at {host}:{port}")
                except socket.timeout:
                    break
        except Exception as e:
            print(f"Error discovering servers: {e}")

        udp_sock.close()
        return servers

    def connect_to_server(self, host, port):
        """Connect to the selected server."""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        self.server_address = (host, port)

        # Input username and send to server
        self.username = input("Enter your username: ")
        os.system("cls")
        client_socket.send(self.username.encode())  # Send username once upon connecting

        threading.Thread(target=self.receive_messages, args=(client_socket,)).start()

        print(f"Connected to server at {host}:{port}. Start chatting!")
        while self.running:
            message = input()
            if message.lower() == 'exit':
                self.running = False
                client_socket.close()
                break
            client_socket.send(message.encode())

    def receive_messages(self, client_socket):
        """Handles receiving messages from the server."""
        while self.running:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"\n{message}")
            except:
                print("Connection lost.")
                self.running = False
                break

if __name__ == "__main__":
    client = ChatClient()
    available_servers = client.discover_servers()

    if available_servers:
        print("Available servers:")
        for i, ((host, port), server_name) in enumerate(available_servers.items(), 1):
            print(f"{i}. {server_name} ({host}:{port})")

        choice = int(input("Select a server to connect to (enter number): "))
        os.system("cls")
        selected_server = list(available_servers.keys())[choice - 1]
        client.connect_to_server(*selected_server)
    else:
        print("No servers found on the network.")



