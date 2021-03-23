import socket
from multiprocessing import cpu_count

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

        conn.sendall(bytes(HOST, 'utf-8'), bytes(cpu_count(), 'utf-8'))
        s.close()
        break
except KeyboardInterrupt:
    print("shutting down")
    s.close()