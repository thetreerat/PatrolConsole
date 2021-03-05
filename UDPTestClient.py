# Author: Harold Clark
# Copyright Harold Clark 2021
#
from DMRmessage import Message
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
        sentbytesCount = self.udpCleintSocket.sendto(SendData, self.destination)
        recievedBytes = self.udpCleintSocket.recvfrom(self.getbytes)
        print(recievedBytes)

if __name__ == "__main__":

    #N = UDPClient(IP="10.10.244.30", Port=4007)
    N = UDPClient(IP="192.168.1.17", Port=4007)
    print(N)
    msg = "DoSomeThBill T -HILL.  Hello to you".encode()
    msg2 = "SignIN  Unregistered    Hal C -AP".encode()
    inet = (N.ServerIP, N.ServerPort)
    m = Message((msg,inet))
    m2 = Message((msg2,inet))
    N.CreateSocket()
    N.requestData(m.encoded)
    #N.CreateSocket()
    N.requestData(m2.encoded)
    #N.About()