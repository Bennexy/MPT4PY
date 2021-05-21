import socket, time, sys, os
from multiprocessing import cpu_count

HOST = "192.168.1.101"
PORT = 55555

hosts = ["192.168.1.101"]

for host in hosts:
    os.system(f"ssh root@{host} 'cd /opt/MPT4PY && venv/bin/python client/client-main.py'")

print("starting up")
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        print('Connected by', addr)
        try:
            print("try loop")
            while True:
                data = conn.recv(1024)
                print(data.decode())
            #payload = {"host" : HOST, "cpu-count": cpu_count()}
            #conn.sendall(str.encode(str(payload)))
            #print("sent data")
        except KeyboardInterrupt:
            print("exit")
            sys.exit()
        except Exception as e:
            print(e)
            main()
    except KeyboardInterrupt:
        print("shutting down")
        s.close()


main()
