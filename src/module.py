import os, sys, datetime
sys.path.append(".")


class Logger:
    def __init__(self, message):
        self.message = message

    def server_response(self, host):
        with open(os.path.join("logs", "server_response"), "a") as logfile:
            logfile.write(str(datetime.datetime.now()) + " " + host + " " + self.message + "\n")
        print("done")


Logger("test").server_response("127.0.0.1")