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

def client_program():
    config = load_config('config.json')
    host = config['server_ip']
    port = config['server_port']

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        try:
            message = input("Enter a message (or 'exit' to quit): ")
            if message == 'exit':
                break
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print(f"Received from server: {data}")
        except KeyboardInterrupt:
            print("\nClient is shutting down...")
            break

    client_socket.close()

if __name__ == '__main__':
    client_program()

