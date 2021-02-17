# Author: Harold Clark
# Copyright Harold Clark 2019
#
import sys
import os
import psycopg2
import hashlib

class database(object):
    """database class object for a postgres database"""
    def __init__(self, user='postgres',
                 host='127.0.0.1',
                 port='5432',
                 database='skischool',
                 password=None,
                 owner='Unknown',
                 debug=True):
        """init database object """
        self.cur = None
        self.set_password(password)
        self.user = user
        self.host = host
        self.port = port
        self.database = database
        self.db = None
        self.owner = owner
        self.debug = debug
        if self.debug:
            print('Database object created for %s' % (self.owner))
        
    def __del__(self):
        if self.db!=None:
            if self.db.closed==0:
                self.close()
        if self.debug:
            print('Database close for owner: %s' % (self.owner))
    
    def __str__(self):
        return """DATABASE - owner: %s, debug: %s, user: %s,
           host: %s, database: %s, port: %s, password: %s""" % (self.owner,
                                                                str(self.debug),
                                                                self.user,
                                                                self.host,
                                                                self.database,
                                                                self.port,
                                                                self.password())

    def  __repr__(self):
        return """DATABASE - owner: %s, debug: %s, user: %s,
           host: %s, database: %s, port: %s, password: %s,
           pythonID: %s""" % (self.owner,
                                                                str(self.debug),
                                                                self.user,
                                                                self.host,
                                                                self.database,
                                                                self.port,
                                                                self.password(),
                                                                id(self))
    
    def call_ski_proc(self, proc, params):
        self.connect()
        
        self.cur.callproc(proc, params)
        results = self.cur.fetchall()
        self.close()        
        return results

    def close(self):
        """commit data and cloase the database connection"""
        self.db.commit()
        self.cur.close()
        self.db.close()
        print('Close database connnect for owner %s' % (self.owner))
            
    def connect(self):
        """ """
        try:
            if self._password==None:
                self.db = psycopg2.connect(user=self.user,
                                           port=self.port,
                                           host=self.host,
                                           database=self.database)
            else:
                self.db = psycopg2.connect(user=self.user,
                                           port=self.port,
                                           host=self.host,
                                           database=self.database,
                                           password=self._password)
        except psycopg2.OperationalError as e:
            print("""database errror: %s """ % (e))
            return 0
        except Exception as e:
            print ("Unexpected error: %s" % e)
            raw_input('Resume:')
            
        self.cur = self.db.cursor()
            
    def fetchdata(self, proc, params):
        if self.cur==None:
            self.connect()
        try:
            self.db.rollback()
            self.cur.callproc(proc, params)
            results = self.cur.fetchall()
            self.db.commit()
            return results
        
        except psycopg2.ProgrammingError as e:
            raw_input(e)
            return []

        except Exception as e:
            print ("Unexpected error: %s" % e)
            raw_input('Resume:')
            return []
        
    def password(self):
        if self._password==None:
            return ''
        else:
            return hashlib.md5(self._password).hexdigest()
    
    def set_password(self, password):
        self._password = password
    
    def compare_password(self, hash_value, clear_password):
        hashed_password = hashlib.md5(clear_password).hexdigest()
        if hash_value==hashed_password:
            return True
        else:
            if self.debug:
                print(hashed_password)
                print(hash_value)
            return False
        
if __name__ == '__main__':    
    db_handle = database(owner='database.py - __Main__', debug=True)
    print(db_handle)    
    value = db_handle.compare_password(db_handle.password(), 'Test')
    print(value)
