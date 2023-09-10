import socket
import json

def load_config(config_file):
    try:
        with open(config_file, 'r') as f:
            config_data = json.load(f)
        return config_data
    except FileNotFoundError:
        print(f"Error: Config file '{config_file}' not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in config file '{config_file}'.")
        exit(1)

def server_program():
    config = load_config('config.json')
    host = config['server_ip']
    port = config['server_port']

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print(f"Server listening on {host}:{port}")

    while True:
        try:
            client_socket, address = server_socket.accept()
            print(f"Connection from {address}")
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Received data: {data}")
            client_socket.send(data.encode())
            client_socket.close()
        except KeyboardInterrupt:
            print("\nServer is shutting down...")
            break

    server_socket.close()

if __name__ == '__main__':
    server_program()

