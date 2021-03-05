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
    def checkRadioCommand(self, m, rmsg):
        if m.command().strip()=='SignIN':
            r = self.Radios.checkIP(m.sourceIP, return_type=Radio.object)
            r.SignIn(m.extra(0))
            print("CheckRadioCommand: %s" % (r.RadioIDtext(0)))
            signmsg = "%s signed in for %s." % (r.RadioIDtext(0), m.extra(0))
            print(signmsg)
            rmsg.set_extra(rmsg.extra(0) + " " + signmsg)
        return rmsg

    def checkRadioRegisteration(self, msg, rmsg, timeval):
        r = self.Radios.checkIP(msg.sourceIP, return_type=Radio.object)
        print("%s: msg: %s  recived from %s return port %s" % (timeval, msg.command(), msg.sourceIP, msg.sourcePort))
        if r==None:
            r = Radio(RadioIP=msg.sourceIP, RadioIDtext=msg.RadioID(0))
            self.Radios.append(r)

            print("Radio %s with IP address %s add to List of Active Radios" % (r.RadioIDtext(0), r.RadioIP(0)))
            rmsg.set_extra(rmsg.extra(0) + " Added to list of Active Radios")
        if r.SignedIn()==False:
            print("Radio %s not sign in with user!")
            rmsg.set_extra(rmsg.extra(0) + " Please Sign radio in!")
        
        return rmsg
    def run_server(self):
        """Start and run Server """
        self.Radios = Radios()
        self.ServerSocket.bind((self.IP, self.Port))
        print("   DMR Server listening on IP: %s Port:%s" % (self.IP, self.Port))
        while(self.Run):
            msgAndAddress = self.ServerSocket.recvfrom(self.DataGramSize)
            try:
                timeval = datetime.datetime.now()
                returnmsg = Message()
                msg = msgAndAddress[0].decode()
                m = Message(msgAndAddress)
            

                returnmsg = self.checkRadioRegisteration(m, returnmsg, timeval)
                returnmsg = self.checkRadioCommand(m, returnmsg)
                # Closing message if nothing to do!!
                if returnmsg.extra()==None:
                    returnmsg.set_extra("Hello Client!")
                self.ServerSocket.sendto(returnmsg.encoded, msgAndAddress[1])
                print("Sent: %s" % (returnmsg))
            except Exception:
                self.ServerSocket.sendto("Error!!".encode(), msgAndAddress[1])
                raise

    def exit_now(self):
        sys.exit(1)
        
    def print_help(self):
        print('      DMR help ...')
        print('    --------------------------------------------------------------------------------------')
        for i in self.menu_items:
            i.print_help()
        print('    --------------------------------------------------------------------------------------')

    
if __name__ == "__main__":
    #S = DMRServer(IP="192.168.1.17", Port=4007)
    S = DMRServer(IP="192.168.1.17", Port=4007)
    S.run_server()
    
    #L = Login(login='halc')
    #L.Login()
    #ski_db = database(owner='main.py - __main__')
    #Main = Menu('Main Menu', db_handle=None)
    #Main.menu_display = Main.print_help    
    #Main.add_item('Test', 'Testing ...', instructor_menu)
    #Main.Menu()
