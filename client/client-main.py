import socket, sys, ast
sys.path.append(".")
from time import sleep
from src.module import Logger

HOST = "192.168.0.164"
PORT = 5555


class ClientSocket:
    socket.setdefaulttimeout(10)

    def __init__(self, sock=None):
        if sock == None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))
        print("connected to", host)

    def send(self, payload_in):
        payload = []
        if str.encode(str(payload_in)).__sizeof__() > 970:
            payload = self.split_payload(payload_in)
        else:
            payload.append(str.encode(str(payload_in)))

    @staticmethod
    def split_payload(payload_in):
        payload_out = []
        string = ""
        for char in str(payload_in):
            if str.encode(string + str(char)).__sizeof__() <= 970:
                string += str(char)
            else:
                payload_out.append(str.encode(string))
                string = str(char)
        
        
        return payload_out


try:
    print("starting up")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("sending data")
    sleep(1)
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    data = data.decode()
    data = ast.literal_eval(data)
    Logger(data).server_response(HOST)
    print('Received', data)
    s.close()
except KeyboardInterrupt:
    s.close()
