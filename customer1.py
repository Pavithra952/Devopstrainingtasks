import socket
import json
import threading


def read_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config


def send_message(server_info, message):
    try:
        server_ip = server_info['ip']
        server_port = server_info['port']

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        client_socket.send(message.encode())
        if message.lower() != 'exit':
            response = client_socket.recv(1024).decode()
            print(f"Response from {server_ip}:{server_port}: {response}")

        client_socket.close()
    except Exception as e:
        print(f"Error connecting to {server_ip}:{server_port}: {e}")


def main():
    try:
        config = read_config('config_file.json')

        while True:
            message = input("Enter the broadcast message : ")
            if message.lower() == 'exit':
                send_exit_message(config)
                break

            threads = []
            for server_info in config['servers']:
                thread = threading.Thread(target=send_message, args=(server_info, message))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

    except Exception as e:
        print(f"An error occurred: {e}")


def send_exit_message(config):
    for server_info in config['servers']:
        send_message(server_info, 'exit')


if __name__ == "__main__":
    main()


