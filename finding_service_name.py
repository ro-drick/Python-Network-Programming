import socket


def find_service_name():
    protocol_name = "tcp"
    for port in (80, 53, 25):
        service_name = socket.getservbyport(port, protocol_name)
        print(f"port: {port}, Service Name: {service_name}")


if __name__ == "__main__":
    find_service_name()
