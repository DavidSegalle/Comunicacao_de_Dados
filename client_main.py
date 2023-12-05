import socket

class Client:

    def __init__(self):
        self.s = socket.socket()

        self.hostname = "ubuntu-vaio"
        self.port = 8000

        self.s.connect((self.hostname, self.port))
    
    def mainLoop(self):
        while(True):
            x = input("Enter message: ")
            self.s.send(x.encode())
            
    

if __name__ == "__main__":
    a = Client()
    a.mainLoop()