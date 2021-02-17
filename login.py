# Author: Harold Clark
# Copyright Harold Clark 2021
#
from database import database
from menu import Menu
import getpass

class  Login(object):
    """Login"""
    def __init__(self,
                 login=None,
                 password=None):
        """Create New Instanace of Login"""
        self.login = login
        self.password = password
        self.db_handle = None
    
    def __str__(self):
        return "Login: db: %s" % (self.db_handle.owner)
        
    def __repr__(self):
        return "Login: db: %s, pythonID: %s" % (self.db_handle.owner, id(self))
    
    def Login(self, options=None):
        while not self.db_handle:
            if not self.login:
                self.login = raw_input('Login: ')
            if not self.password:
                self.password = getpass.getpass('Password: ')
            self.set_db_handle()
            #print(self.db_handle.db)
            if not self.db_handle.db:
                print('here')
                self.login = None
                self.password = None
                self.db_handle=None
            
        
    def set_db_handle(self):
        owner = 'Login - %s' % (self.login)
        db_handle = database(owner=owner, user=self.login, password=self.password)
        #print(db_handle)
        self.db_handle = db_handle
        self.db_handle.connect()
        
    def About(self):
        print("""Author         : Harold Clark  email address thetreerat@gmail.com
Class          : Login
Inputs         : None
Returns        : None
Output         : None
Purpose        : This Class is a temlplete file

""")
        


if __name__ == "__main__":
    N = Login()
    N.Login()
    r = N.db_handle.fetchdata('get_employee_certs', [15,])
    print(r[0])
    #N.About()