import socket
import threading

HOST = '10.6.2.240'  # change to '' to accept from any interface
PORT = 12345        # non-privileged port

def process_message(msg: str) -> str:
    """Example processing: convert to uppercase."""
    return msg.upper()

def handle_client(conn: socket.socket, addr, count : int):
    """Receive messages on a client socket, process them, and send responses."""
    with conn:
        print(f"[{addr}] Connection established -> Client {count}")
        while True:

            # Block-1
            data = conn.recv(1024)
            if not data:
                break
            text = data.decode('utf-8').rstrip()
            print(f"[{addr}] Received from Client-{count}: {text!r}")
            response = process_message(text)
            conn.sendall(response.encode('utf-8'))
            print(f"[{addr}] Replied to Client-{count}: {response!r}")

            # Block-2
            data = conn.recv(1024)
            if not data:
                break
            text = data.decode('utf-8').rstrip()
            print(f"[{addr}] Received from Client-{count}: {text!r}")
            response = process_message(text)
            conn.sendall(response.encode('utf-8'))
            print(f"[{addr}] Replied to Client-{count}: {response!r}")

        print(f"[{addr}] Connection closed -> Client {count}")

def run_server():
    count = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            count += 1
            
            # Create a new thread to handle each client
            thread = threading.Thread(target=handle_client, args=(conn, addr, count), daemon=True)
            thread.start()

if __name__ == "__main__":
    run_server()