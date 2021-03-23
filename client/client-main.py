import socket, sys
sys.path.append(".")
from time import sleep
from src.module import Logger

HOST = "192.168.0.164"
PORT = 5555

try:
    print("starting up")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("sending data")
    sleep(1)
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    Logger(data.decode()).server_response(HOST)
    print('Received', repr(data.decode()))
    s.close()
except KeyboardInterrupt:
    s.close()