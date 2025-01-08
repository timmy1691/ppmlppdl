import socket

global id ;

class Node():
    def __init__(self,nodeID,  host, port):
        self.host = host
        self.port = port
        self.id = nodeID
        self.tasks = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))

    def sendData(self):
        pass

    def receiveData(self):
        pass

    