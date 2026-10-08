from socket import socket
import time
import urllib.parse
import webbrowser
import socket
def main():
    get_local_ip()
    ip = get_local_ip()
    print(f"Your local IP address is: {ip}")
    
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))  # just to resolve local IP
        return s.getsockname()[0]
    finally:
        s.close()


if __name__ == "__main__":
    main()