# Copyright Harold Clark 2021
#
#from login import Login
#from database import database
from Radio import Radio
import datetime

class Radios(object):
    """Class of a list of radios """
    Radio.index = 1
    Radio.object = 2
    Radio.IP = 3
    Radio.Name = 4

    
    def __init__(self):
        self.Radios = []

    def __str__(self):
        return "Radios: %s" % (len(self.Radios))
        
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
        for radio in self.Radios:
            if radio.RadioIP()==RIP:
                if return_type==Radio.index:
                    return i
                elif return_type==Radio.object:
                    return radio
                elif return_type==Radio.IP:
                    return radio.IP
                elif return_type==Radio.Name:
                    return radio.RadioName
            i += 1
        return None

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

    def sort(self):
        self.Radios = sorted(self.Radios, key=self.sort_key_Radio_ID)

    def sort_key_Radio_ID(self, i):
        return i._RadioID

if __name__ == "__main__":
    R = Radios()
    r = Radio(RadioID='PR0001', RadioIP='192.168.1.17')
    i =0
    while i<4:
        if R.checkIP(r.RadioIP())==None:
            R.append(r)
        i += 1
    print(len(R))
    print("Done")