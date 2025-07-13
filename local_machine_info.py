import socket


def print_machine_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Host name is: {hostname}")
    print(f"IP address is: {ip_address}")


if __name__ == "__main__":
    print_machine_info()
