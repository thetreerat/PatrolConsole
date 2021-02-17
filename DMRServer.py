# Copyright Harold Clark 2021
#
#from menu import Menu
#from login import Login
#from database import database
import socket
import datetime

class Radio(object):
    """Radio Class Object """
    def __init__(self,
                 ID=None,
                 Name=None,
                 IP=None,
                 SignedIn=None):
        self.Name=Name
        self.IP=IP
        self.Location=None
        self.ID=ID
        if SignedIn==None:
            self.SignedIn=False
        else:
            SignedIn=RadioSignedIn
    def SignIn(self):
        self.SignedIn = datetime.datetime.now()
    
    
class Radios(object):
    """Class of a list of radios """
    Radio.index = 1
    Radio.object = 2
    Radio.IP = 3
    Radio.Name = 4

    
    def __init__(self):
        self.Radios = []

    def __str__(self):
        return "Radios" % ()
        
    def __repr__(self):
        return "Radios - pythonID: %s" % (id(self))
    
    def __len__(self):
        return len(self.Radios)
    
    def append(self, Radio):
        self.Radios.append(Radio)
        self.sort()
        
    def clear(self):
        self.Radios = []
    
    def checkIP(self, RIP, return_type=Radio.object):
        i=0
        for o in self.Radios:
            if o.IP==RIP:
                if return_type==Radio.index:
                    return i
                elif return_type==Radio.object:
                    return o
                elif return_type==Radio.IP:
                    return o.IP
                elif return_type==Radio.Name:
                    return o.Name
            i += 1

    def checkID(self, RID, return_type=Radio.object):
        i = 0
        for o in self.Radios:
            if o.ID==RID:
                if return_type==Radio.index:
                    return i
                elif return_type==Radio.object:
                    return o
                elif return_type==Radio.IP:
                    return o.IP
                elif return_type==Radio.Name:
                    return o.Name
            i += 1
        return None
    
class  DMRServer(object):
    """DMR Server Class"""
    def __init__(self,
                 DMRIP=None,
                 DMRPort=None):
        self.IP = DMRIP
        self.Port = DMRPort
        self.Run = True
        self.ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.DataGramSize = 1024
        self.Radios = Radios()
        
        
    def hold_stuff(self):
            hello = "Hello %s" % (cleintIP)
            encodedMsg = hello.encode()
            socketforClient.send(encodedMsg)

    def sendName(self):
        pass        
        
    def run_server(self):
        """Start and run Server """
        self.ServerSocket.bind(self.IP, self.Port)
        print("   DMR Server listening on IP: %s Port:%s" % (self.IP, self.Port))
        while(self.Run):
            msgAndAddress = self.ServerSocket.recvfrom(self.DataGramSize)
            timeval = datetime.datetime.now()
            msg = msgAndAddress[0].decode()
            i = 0
            for m in msgAndAddress:
                print("msgAndAddress[%s]: %s" % (i, m))
                i =+ 1
            clientIP = "0.0.0.0"
            print("%s: msg: %s  recived from %s" % (timeval, msg, msgAndAddress[1]))
            self.ServerSocket.sendto("Hello Client!".encode(), msgAndAddress[1])
            
    def exit_now(self):
        sys.exit(1)
        
    def print_help(self):
        print('      DMR help ...')
        print('    --------------------------------------------------------------------------------------')
        for i in self.menu_items:
            i.print_help()
        print('    --------------------------------------------------------------------------------------')

    
if __name__ == "__main__":
    S = DMRServer(LocolIP="192.168.1.17", LocalPort="4007")
    S.run_server()
    #L = Login(login='halc')
    #L.Login()
    #ski_db = database(owner='main.py - __main__')
    #Main = Menu('Main Menu', db_handle=None)
    #Main.menu_display = Main.print_help    
    #Main.add_item('Test', 'Testing ...', instructor_menu)
    #Main.Menu()