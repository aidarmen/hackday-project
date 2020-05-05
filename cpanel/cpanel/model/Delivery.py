import datetime
import time

class Delivery():
    def __init__(self, products,managerId,managerName):
            self.delivererName = ""
            self.delivererId = ""
            self.inProcess = "notTaken"
            self.timeCreated = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            self.products = products
            self.managerId = managerId
            self.managerName = managerName
    
    def to_dict(self):
        # [START_EXCLUDE] 
        dest = { 
            u'delivererName': self.delivererName,
            u'delivererId': self.delivererId,
            u'inProcess': self.inProcess,
            u'timeCreated': self.timeCreated,
            u'products': self.products,
            u'managerId': self.managerId,
            u'managerName': self.managerName
        }
        return dest