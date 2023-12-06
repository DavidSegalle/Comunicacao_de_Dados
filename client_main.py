import socket
import cipher as ci
from typing import List

class Client:

    # Por enquanto, estamos recebendo o IP do host na construtora.
    # O cliente eh criado em client_data_screen, veja se consegue
    # mudar la pra pegar o IP pela GUI.
    def __init__(self, host: str):
        self.cs = socket.socket()
        self.HOST = socket.gethostbyname(host)
        self.PORT = 51234
        self.cs.connect((self.HOST, self.PORT))
        print(f'Connected to {self.HOST} on port {self.PORT}.')

    def __del__(self):
        self.cs.close()
        print('Connection ended.')

    def send_message(self, signal: List[int]):
        self.cs.sendall(ci.send_signal(signal))

    '''
    def __init__(self):
        self.s = socket.socket()
        self.hostname = "ubuntu-vaio"
        self.port = 8000
        self.s.connect((self.hostname, self.port))

    def mainLoop(self):
        while(True):
            x = input("Enter message: ")
            self.s.send(x.encode())
    '''


if __name__ == "__main__":
    a = Client()
    a.mainLoop()
