import socket
import json
from settings import *

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(30)  # Set a timeout of 5 seconds
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        self.local_data = {
            'id' : "",
            'player' : {
                'pos' : (1500,1500),
                'hp' : 100,
                'angle': 90,
            },
            'bullet' : []
        }
        self.server_data = {}

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            print("connected to server")
        except socket.timeout:
            print("Connection timed out.")
        except Exception as e:
            print(f"Connection failed: {e}")

    def fetch_data(self):
        try:
            self.client.send(json.dumps(self.local_data).encode())
            self.server_data = json.loads(self.client.recv(MAX_DATA_SIZE).decode())
        except socket.timeout:
            print("Send/receive operation timed out.")
        except socket.error as e:
            print(f"Socket error: {e}")        
            
    def listen(self):
        return self.client.recv(MAX_DATA_SIZE).decode()
    
    def shut_down(self):
        try:
            self.client.shutdown(socket.SHUT_RDWR)  # Use SHUT_RDWR for proper shutdown
            self.client.close()
        except Exception as e:
            print(f"Error during shutdown: {e}")


net = Network()
net.data = {
    'id' : 'tuyenlt',
    'player': {
        'pos' : (200, 300),
        'hp' : 100,
    },
    'bullets' : [[(200,100), (300,400)]]
}
net.fetch_data()
print(net.server_data)
net.data = {
    'id' : 'hmm',
    'player': {
        'pos' : (200, 300),
        'hp' : 100,
    },
    'bullets' : [[(200,100), (300,400)]]
}
net.fetch_data()
print(net.server_data)
net.shut_down()