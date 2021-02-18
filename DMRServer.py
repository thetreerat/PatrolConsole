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
        self._Name=Name
        self._IP=IP
        self._Location=None
        self._ID=ID
        if SignedIn==None:
            self._SignedIn=False
        else:
            self._SignedIn=SignedIn

    def ID(self, pad=0):
        if pad==0:
            return self._ID
        if self._ID==None:
            return " ".ljust(pad, " ")
        else:
            return self._ID.ljust(pad, " ")

    def IP(self, pad=0):
        if pad==0:
            return self._IP
        if self._IP==None:
            return " ".ljust(pad, " ")
        else:
            return self._IP.ljust(pad, " ")

    def Location(self, pad=0):
        if pad==0:
            return self._Location
        if self._Location==None:
            return " ".ljust(pad, " ")
        else:
            return self._Location.ljust(pad, " ")

    def Name(self, pad=0):
        if pad==0:
            return self._Name
        if self._Name==None:
            return "".ljust(pad, " ")
        else:
            return self._Name.ljust(pad, " ")    

    def set_IP(self, IP):
        self._IP = IP

    def set_ID(self, ID):
        self._ID = ID

    def set_Name(self, Name):
        self._Name = Name

    def SignIn(self):
        self.SignedIn = datetime.datetime.now()

    def SignedIn(self, pad=0):
        if pad==0: 
            if self._SignedIn==False:
                return 0
            else:
                return self._SignedIn

        if _SignedIn==False:
            return "No".ljust(pad)
        else:
            return self._SignedIn 

    def print_self(self):
        if self.Name==None:
            Name = "".ljust(25, " ")
        else:
            Name = ""
        print("Name: %s  IP: %s ID: %s SignedIn: %s" % (self.Name(25), 
                                                        self.IP(15),
                                                        self.ID(25),
                                                        self.SignedIn(15)))
    
    
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
                 IP=None,
                 Port=None):
        self.IP = IP
        self.Port = Port
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
        R = Radios()
        self.ServerSocket.bind((self.IP, self.Port))
        print("   DMR Server listening on IP: %s Port:%s" % (self.IP, self.Port))
        while(self.Run):
            msgAndAddress = self.ServerSocket.recvfrom(self.DataGramSize)
            timeval = datetime.datetime.now()
            msg = msgAndAddress[0].decode()
            r = R.checkIP(msgAndAddress[1][0], Radio.object)
            if not r:
                r = Radio(IP=msgAndAddress[1][0], Name="UDP Client")
                r.print_self()
                print("Added Radio to Active List")
            if not r.SignIn:
                    r.print_self()
                    print("Radio not Assigned to user")
            
            print("%s: msg: %s  recived from %s" % (timeval, msg, r.IP))
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
