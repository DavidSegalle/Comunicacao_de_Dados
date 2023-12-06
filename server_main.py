import socket

class Server:

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
            
    

if __name__ == "__main__":
    a = Server()
    a.mainLoop()