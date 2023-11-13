print("running network.py...")

import socket




class Network:
    def __init__(self):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server="192.168.0.107"
        self.port=5555
        self.addr=(self.server,self.port)
        self.pos=self.connect()
        
    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            r=self.client.recv(2048).decode()
            print(r)
            return r
        
        except:
            pass
    def send (self,data):
        try:
            print(f"sending data... {data}")
            self.client.send(str.encode(data))
            r=self.client.recv(2048).decode()
            print(f"recieved data... {r}")
            return r
        except socket.error as e:
            print(e)


    
