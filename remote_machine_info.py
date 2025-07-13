import socket


def get_remote_machine_info():
    remote_host = "www.pljkjlthon.org"
    try:
        print(f"IP address of {remote_host} is {socket.gethostbyname(remote_host)}")
    except socket.error as err_msg:
        print(err_msg)


if __name__ == "__main__":
    get_remote_machine_info()
