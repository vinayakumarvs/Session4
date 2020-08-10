from decimal import Decimal
import random
import cmath

class Qualean():
    def __init__(self,real_num):
        super().__init__()
        self.im_num = round(Decimal(real_num) * Decimal(random.uniform(-1,1)),10)

        if real_num not in [-1, 0, 1]:
            raise ValueError ("Number not in [-1, 0, 1]")

    def __and__(self, other=None):
        if(bool(self.im_num) is False):
            return False
        elif(other is None):
            return False
        else:      
            return bool(self.im_num and other.im_num)

    def __or__(self, other=None):
        if(bool(self.im_num) is True):
            return True
        elif(other is None):
            return False
        else:      
            return bool(self.im_num or other.im_num)

    def __repr__(self):
        return '{0}'.format (self.im_num)

    def __str__(self):
        return '{0}'.format (self.im_num)

    def __add__ (self, other):
        return self.im_num + other.im_num

    def __eq__ (self, other):
        return self.im_num == other.im_num

    def __float__ (self):
        return float(self.im_num)

    def __ge__ (self, other):
        return self.im_num >= other.im_num

    def __gt__ (self, other):
        return self.im_num > other.im_num

    def __invertsign__ (self):
        return self.im_num * -1

    def __le__ (self, other):
        return self.im_num <= other.im_num

    def __lt__ (self, other):
        return self.im_num < other.im_num

    def __mul__ (self, other):
        return self.im_num * other.im_num

    def __sqrt__ (self):
        return cmath.sqrt(self.im_num)

    def __bool__ (self):
        return self.im_num != 0

    def __decimal__(self):
        return self.im_num
