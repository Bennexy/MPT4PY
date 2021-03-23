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
        payload = {"host" : HOST, "cpu-count": cpu_count()}
        conn.sendall(str.encode(str(payload)))
        s.close()
        print("sent data")
        break
except KeyboardInterrupt:
    print("shutting down")
    s.close()