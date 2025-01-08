import Node
import helperFunctions as hf

class NodeClient(Node):
    def __init__(self, nodeID, host, port):
        super(NodeClient, self).__init__(nodeID, host, port)

    def sendData(self, target):
        pass


    def ReceiveData(self, target):
        pass

    def localDatasource(self, database=None , path = None):
        hasDatasource = False
        if database is not None:
            pass

        
        if path is not None:
            pathExists = hf.checkPath(path)
            if pathExists:
                hasDatasource = True


        if not hasDatasource:
            assert "No data source provided, please provide a datasource"



    
        

