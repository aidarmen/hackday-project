import datetime
import time

class User():
    def __init__(self,email, name,password,phone,uid,position):
            self.name = name
            self.email = email
            self.phone = phone
            self.password = password
            self.position = position
            self.uid = uid

    
    def to_dict(self):
        # [START_EXCLUDE] 
        dest = { 
            u'name': self.name,
            u'email': self.email,
            u'phone': self.phone,
            u'password': self.password,
            u'position': self.position,
            u'uid': self.uid,
            
        }
        return dest