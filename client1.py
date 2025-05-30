import socket

HOST = '10.6.2.240' # Server IP
PORT = 12345 # Port no. in Server

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Block-1
        message = input("Enter the message:")
        message = f"c1m1 {message}"
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)

        # Block-2
        message = input("Enter the message:")
        message = f"c1m2 {message}"
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)

        print(f"Server responded: {data.decode('utf-8')}")

if __name__ == "__main__":
    run_client()