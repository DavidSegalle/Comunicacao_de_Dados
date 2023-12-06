import socket
import cipher as ci

class Server:

    def __init__(self):
        self.ss = socket.socket()
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 51234
        self.ss.bind((self.IP, self.PORT))
        self.ss.listen()
        print(f'Server started at {self.IP} on port {self.PORT}.\n' \
              + 'Waiting for connection…')
        (self.cs, self.addr) = self.ss.accept()
        print(f'Connected to {self.addr[0]} on port {self.addr[1]}.')
        self.running = True

    def __del__(self):
        self.ss.close()
        print('Connection ended.')

    def receive_message(self):
        data = self.cs.recv(1024)
        return ci.receive_signal(data)

    '''
    def __init__(self):
        self.listensocket = socket.socket()
        self.port = 8000
        self.maxConnections = 999
        self.IP = socket.gethostname()

        self.listensocket.bind(('ubuntu-vaio', self.port))

        self.listensocket.listen(self.maxConnections)
        print("Server started at " + self.IP + " on port " + str(self.port))

        (self.clientsocket, self.address) = self.listensocket.accept()

        print("New connection made")

        self.running = True

    def mainLoop(self):
        while(self.running):
            message = self.clientsocket.recv(1024).decode()
            print(message)
    '''


if __name__ == "__main__":
    a = Server()
    a.mainLoop()
