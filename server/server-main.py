import socket

HOST = "127.0.0.1"
PORT = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print('Connected by', addr)
try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
except KeyboardInterrupt:
    print("shutting down")
    s.clone()