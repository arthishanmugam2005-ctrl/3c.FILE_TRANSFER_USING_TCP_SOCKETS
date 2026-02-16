import socket
import os
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001
BUFFER_SIZE = 4096 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_HOST, SERVER_PORT))
server.listen(1)
print("Server listening on port", SERVER_PORT)
conn, addr = server.accept()
print("Connected from:", addr)
try:
    filename = conn.recv(BUFFER_SIZE).decode()
    filesize = int(conn.recv(BUFFER_SIZE).decode())
    print(f"Receiving file: {filename}")
    print(f"File size: {filesize} bytes")
    received_size = 0
    with open("received_" + filename, "wb") as f:
        while received_size < filesize:
            bytes_read = conn.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            received_size += len(bytes_read)
            progress = (received_size / filesize) * 100
            print(f"Progress: {progress:.2f}%", end="\r")
    print("\nFile received successfully!")
except Exception as e:
    print("Error:", e)
finally:
    conn.close()
    server.close()
