# Copyright Harold Clark 2021
#
#from login import Login
#from database import database
import datetime

class Radio(object):
    """Radio Class Object """
    def __init__(self,
                 RadioIDtext=None,
                 RadioName=None,
                 RadioIP=None,
                 SignedIn=None):
        self._Name=RadioName
        self._IP=RadioIP
        self._Location=None
        self._RadioID=RadioIDtext
        print("RadioIDText value: %s" % (RadioIDtext))
        if SignedIn==None:
            self._SignedIn=False
        else:
            self._SignedIn=SignedIn

    def __str__(self):
        return "Radio ID: %s Radio Name: %s Radio IP: %s" % (self.RadioIDtext(15), 
        	                                                 self.RadioName(15), 
        	                                                 self.RadioIP(15))
        
    def __repr__(self):
        return "Radios - pythonID: %s" % (id(self))

    def RadioIDtext(self, pad=None):
        if pad==None:
            return self._RadioID
        if self._RadioID==None:
            return " ".ljust(pad, " ")
        else:
            return "test" #self._RadioID #.ljust(pad, " ")

    def RadioIP(self, pad=None):
        if pad==None:
            return self._IP
        if self._IP==None:
            return " ".ljust(pad, " ")
        else:
            return self._IP.ljust(pad, " ")

    def RadioLocation(self, pad=None):
        if pad==None:
            return self._Location
        if self._Location==None:
            return " ".ljust(pad, " ")
        else:
            return self._Location.ljust(pad, " ")

    def RadioName(self, pad=None):
        if pad==None:
            return self._Name
        if self._Name==None:

            return "".ljust(pad, " ")
        else:
            return self._Name.ljust(pad, " ")    

    def set_IP(self, RadioIP):
        self._IP = IP

    def set_ID(self, RadioID):
        self._ID = ID

    def set_location(self, Radiolocation):
        self._Location = location

    def set_Name(self, RadioName):
        self._Name = RadioName

    def SignIn(self, RadioName):
        #print("sign in!")
        self._SignedIn = datetime.datetime.now()
        self.set_Name(RadioName=RadioName)

    def print_self(self):
        print("Name: %s  IP: %s ID: %s SignedIn: %s" % (self.Name(15), 
                                                        self.IP(15),
                                                        self.ID(15),
                                                        self.SignedIn(15)))

    def SignedIn(self, pad=0):
        if pad==0: 
            if self._SignedIn==False:
                return 0
            else:
                return self._SignedIn

        if self._SignedIn==False:
            return "No".ljust(pad)
        else:
            return self._SignedIn.strftime("%X").ljust(pad, " ") 

    
        
    
if __name__ == "__main__":
    #print('test')
    r = Radio(IP="12.12.0.12")
    # r.print_self()
    r.set_Name("Hill Cheif")
    r.set_ID("PL001")
    r1 = Radio(IP="12.12.0.124")
    r1.set_ID("SS001")
    r1.set_Name("SSS Super 1")
    #h = r.Name()
    #print(h)
    r.SignIn()
	#print("Hello World")
	#print(r1)
	#r.print_self()
    r.print_self()
    #print(r.Name(0))