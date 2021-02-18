# Author: Harold Clark
# Copyright Harold Clark 2019
#
import socket

class  UDPClient(object):
    """UDP Client Class"""
    def __init__(self, IP, Port):
        """Create New Instanace of UDP Client Class"""
        self.ServerIP = IP
        self.ServerPort = Port
        self.destination = (self.ServerIP, self.ServerPort)
        self.getbytes = 1024
        self.udpCleintSocket = None
        
    def __str__(self):
        return "UDPClient: IP: %s PORT: %s" % (self.ServerIP, self.ServerPort)
        
    def __repr__(self):
        return "UDPClient: IP: %s PORT: %s pythonID: %s" % (self.ServerIP, self.ServerPort, id(self))

        
    def About(self):
        print("""Author         : Harold Clark  email address thetreerat@gmail.com
Class          : UDP Client
Inputs         : ServerIP, ServerPort
Returns        : None
Output         : None
Purpose        : This Class is a temlplete file

""")

    def CreateSocket(self):
        if self.udpCleintSocket==None:
            self.udpCleintSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def requestData(self, SendData):
        sentbytesCount = self.udpCleintSocket.sendto(SendData.encode(), self.destination)
        recievedBytes = self.udpCleintSocket.recvfrom(self.getbytes)
        print(recievedBytes)

if __name__ == "__main__":
    N = UDPClient(IP="192.168.1.17", Port=4007)
    print(N)
    N.CreateSocket()
    N.requestData("Test")
    #N.About()