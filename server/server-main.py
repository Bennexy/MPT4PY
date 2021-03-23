import socket

HOST = "192.168.0.164"
PORT = 5555


print("starting up")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)

        conn.sendall(data)
except KeyboardInterrupt:
    print("shutting down")
    s.clone()