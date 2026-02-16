import socket
import os
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001
BUFFER_SIZE = 4096
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_HOST, SERVER_PORT))
try:
    filename = input("Enter file name to send: ")
    if not os.path.exists(filename):
        print("File does not exist!")
        client.close()
        exit()
    filesize = os.path.getsize(filename)
    client.send(filename.encode())
    client.send(str(filesize).encode())
    print(f"Sending {filename} ({filesize} bytes)")
    sent_size = 0
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            client.sendall(bytes_read)
            sent_size += len(bytes_read)
            progress = (sent_size / filesize) * 100
            print(f"Progress: {progress:.2f}%", end="\r")
    print("\nFile sent successfully!")
except Exception as e:
    print("Error:", e)
finally:
    client.close()