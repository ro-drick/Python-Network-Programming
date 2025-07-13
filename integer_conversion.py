import socket


def convert_integer():
    data = 1234
    print(f"Original: {data}  Converted: {socket.htonl(data)}")
    # 16-bit conversion
    print(f"Original: {data}  Converted: {socket.ntohs(data)}")


if __name__ == "__main__":
    convert_integer()
