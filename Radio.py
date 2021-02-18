# Copyright Harold Clark 2021
#
#from login import Login
#from database import database
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
    
    

if __name__ == "__main__":
	r = (IP="192.168.0.12", Port=4007)
	print(r)