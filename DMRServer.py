# Copyright Harold Clark 2021
#
#from menu import Menu
#from login import Login
#from database import database
from Radio import Radio
from Radios import Radios
from DMRmessage import Message
import socket
import datetime

    
class  DMRServer(object):
    """DMR Server Class"""
    def __init__(self,
                 IP=None,
                 Port=None):
        self.IP = IP
        self.Port = Port
        self.Run = True
        self.ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.DataGramSize = 1024
        self.Radios = Radios()
        
    def checkIPinList(self, msgAndAddress):
        r = self.Radios.checkIP(msgAndAddress[1][0], Radio.object)  
        if not r:
            r = Radio()

        
    def hold_stuff(self):
            hello = "Hello %s" % (cleintIP)
            encodedMsg = hello.encode()
            socketforClient.send(encodedMsg)

    def sendName(self):
        pass        
        
    def run_server(self):
        """Start and run Server """
        self.Radios = Radios()
        self.ServerSocket.bind((self.IP, self.Port))
        print("   DMR Server listening on IP: %s Port:%s" % (self.IP, self.Port))
        while(self.Run):
            msgAndAddress = self.ServerSocket.recvfrom(self.DataGramSize)
            timeval = datetime.datetime.now()
            msg = msgAndAddress[0].decode()

            m = Message(msgAndAddress)

            print("%s: msg: %s  recived from %s" % (timeval, m.command(), r.IP))
            returnmsg = "Hello Client!"
            self.ServerSocket.sendto(returnmsg.encode(), msgAndAddress[1])
            print("Sent: %s" % (returnmsg))

    def exit_now(self):
        sys.exit(1)
        
    def print_help(self):
        print('      DMR help ...')
        print('    --------------------------------------------------------------------------------------')
        for i in self.menu_items:
            i.print_help()
        print('    --------------------------------------------------------------------------------------')

    
if __name__ == "__main__":
    S = DMRServer(IP="192.168.1.17", Port=4007)
    S.run_server()
    
    #L = Login(login='halc')
    #L.Login()
    #ski_db = database(owner='main.py - __main__')
    #Main = Menu('Main Menu', db_handle=None)
    #Main.menu_display = Main.print_help    
    #Main.add_item('Test', 'Testing ...', instructor_menu)
    #Main.Menu()
