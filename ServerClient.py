import Node

class ServerClient(Node):
    def __init__(self, host, port):
        super(ServerClient, self).__init__(host, port)
        self.isServer = True

