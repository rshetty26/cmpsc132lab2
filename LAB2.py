# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random
import math

# -------- SECTION 1
class Pantry:
    """"
        >>> sara_pantry = Pantry()                
        >>> sara_pantry.stock_pantry('Bread', 2)
        'Pantry Stock for Bread: 2'
        >>> sara_pantry.stock_pantry('Cookies', 6) 
        'Pantry Stock for Cookies: 6'
        >>> sara_pantry.stock_pantry('Chocolate', 4) 
        'Pantry Stock for Chocolate: 4'
        >>> sara_pantry.stock_pantry('Pasta', 3)     
        'Pantry Stock for Pasta: 3'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2, 'Cookies': 6, 'Chocolate': 4, 'Pasta': 3}
        >>> sara_pantry.get_item('Pasta', 2)     
        'You have 1 of Pasta left'
        >>> sara_pantry.get_item('Pasta', 6) 
        'Add Pasta to your shopping list!'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2, 'Cookies': 6, 'Chocolate': 4, 'Pasta': 0}
        >>> ben_pantry = Pantry()                    
        >>> ben_pantry.stock_pantry('Cereal', 2)
        'Pantry Stock for Cereal: 2'
        >>> ben_pantry.stock_pantry('Noodles', 5) 
        'Pantry Stock for Noodles: 5'
        >>> ben_pantry.stock_pantry('Cookies', 9) 
        'Pantry Stock for Cookies: 9'
        >>> ben_pantry.stock_pantry('Cookies', 8) 
        'Pantry Stock for Cookies: 17'
        >>> ben_pantry.get_item('Pasta', 2)       
        "You don't have Pasta"
        >>> ben_pantry.get_item('Cookies', 2.5) 
        'You have 14.5 of Cookies left'
        >>> ben_pantry + sara_pantry
        I am a Pantry object, my current stock is {'Cereal': 2, 'Noodles': 5, 'Cookies': 20.5, 'Bread': 2, 'Chocolate': 4}
        >>> ben_pantry              
        I am a Pantry object, my current stock is {'Cereal': 0, 'Noodles': 0, 'Cookies': 0}
        >>> sara_pantry              
        I am a Pantry object, my current stock is {'Bread': 0, 'Cookies': 0, 'Chocolate': 0, 'Pasta': 0}
    """

    def __init__(self):
        self.items = {}
    
    def __repr__(self):
        #--- YOUR CODE STARTS HERE
        return "I am a Pantry object, my current stock is " + str(self.items)
        pass

    def stock_pantry(self, item, qty):
        #--- YOUR CODE STARTS HERE
        if item in self.items:
                self.items[item] = self.items[item] + qty
        else:
            self.items[item] = qty
        return "Pantry Stock for " + str(item) + ": " + str(self.items[item])
        pass


    def get_item(self, item, qty):
        #--- YOUR CODE STARTS HERE
        if item in self.items:
            if qty <= self.items[item]:
                self.items[item] = self.items[item] - qty
                return "You have " + str(self.items[item]) + " of " + item + " left"
            else:
                self.items[item] = 0
                return "Add "+ item + " to your shopping list!"
        else:
            return "You don't have " + str(item)
        pass
    
    def __add__(self, other):
        #--- YOUR CODE STARTS HERE
        newpantry = Pantry()
        
        for item in self.items:
            if self.items[item] > 0:
                newpantry.stock_pantry(item, self.items[item])
                self.items[item] = 0
        for item in other.items:
            if other.items[item] > 0:
                if item in newpantry.items:
                    newpantry.items[item] = newpantry.items[item] + other.items[item]
                else:
                    newpantry.stock_pantry(item, other.items[item])
                other.items[item] = 0
        
        return newpantry
        pass


# -------- SECTION 2

class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10'
        >>> east_machine.cancelTransaction()
        'Take your $10 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''

    def __init__(self):
        #--- YOUR CODE STARTS HERE
        self.product = {156:[1.5, 3], 254:[2.0, 3], 384:[2.5, 3], 879:[3.0, 3]}
        self.balance = 0
        pass

    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE
        if item not in self.product:
            return "Invalid item"
        if not self.isStocked:
            return "Machine out of stock"
        if self.product[item][1] == 0:
            return "Item out of stock"
        if self.product[item][1] < qty:
            return "Current " + str(item) + " stock: " + str(self.product[item][1]) + ", try again"
        if (self.product[item][0]*qty) > self.balance:
            return "Please deposit $" + str((self.product[item][0]*qty) - self.balance )
        if (self.product[item][0]*qty) == self.balance:
            self.product[item][1] = self.product[item][1] - qty
            self.balance = 0
            return "Item dispensed"
        if (self.product[item][0]*qty) < self.balance:
            self.product[item][1] = self.product[item][1] - qty
            difference = self.balance - (self.product[item][0]*qty)
            self.balance = 0
            return "Item dispensed, take your $" + str(difference) + " back"
        pass
        
    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        self.balance = self.balance + amount
        if self.isStocked:
            return "Balance: $" + str(self.balance)
        else:
            return "Machine out of stock. Take your $" + str(self.balance) + " back"
        pass

    def _restock(self, item, stock):
        #--- YOUR CODE STARTS HERE
        if item not in self.product:
            return "Invalid item"
        else: 
            self.product[item][1] = self.product[item][1] + stock
            return "Current item stock: " + str(self.product[item][1])
        pass

    #--- YOUR CODE STARTS HERE
    @property
    def isStocked(self):
        machineStock = False
        for x in self.product:
            if self.product[x][1] > 0:
                machineStock = True
        return machineStock
        pass
        
    #--- YOUR CODE STARTS HERE
    @property
    def getStock(self):
        return self.product
        pass

    def cancelTransaction(self):
        #--- YOUR CODE STARTS HERE
        if self.balance > 0:
            amount = str(self.balance)
            self.balance = 0
            return "Take your $" + amount + " back"
        pass
       



# -------- SECTION 3

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __mul__(self, other):
        if isinstance(other, int):
            x1 = self.x*other
            y1 = self.y*other
            return Point2D(x1, y1)
        else:
            return None


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = line1*4
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
        >>> Point2D(9,5) in line7
        True
        >>> Point2D(89,5) in line7
        False
        >>> (9,5) in line7
        False
    '''
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self.points = [point1, point2]
        pass

    #--- YOUR CODE STARTS HERE
    @property
    def getDistance(self):
        return round(((self.points[0].x - self.points[1].x)**2 + (self.points[0].y - self.points[1].y)**2)**(0.5), 3)
        pass
       
    @property
    def getSlope(self):
        if self.points[1].x - self.points[0].x == 0:
            return float("inf")
        else:
            return round((self.points[1].y - self.points[0].y) / (self.points[1].x - self.points[0].x), 3)
        pass


    #--- YOUR CODE CONTINUES HERE

    def __str__(self):
        if self.getSlope == float("inf"):
            return "Undefined"
        else:
            b = round(self.points[1].y - (self.getSlope*self.points[1].x), 3)
            if self.getSlope == 0:
                return "y = " + str(b)
            if b == 0:
                return "y = " + str(self.getSlope) + "x"
            return "y = " + str(self.getSlope) + "x + " + str(b)
    
    def __repr__(self):
        return self.__str__()


    def __eq__(self, other):
        if isinstance(other, Line):
            if (self.points[0] == other.points[0] and self.points[1] == other.points[1]) or (self.points[0] == other.points[1] and self.points[1] == other.points[0]):
                return True
            else:
                return False
        else:
            return False
    
    def __mul__(self, other):
        if isinstance(other, int):
            one = self.points[0]*other
            two = self.points[1]*other
            return Line(one, two)
        else:
            return None

    def __contains__(self, other):
        if isinstance(other, Point2D):
            if other.y == self.getSlope*other.x + self.points[1].y - (self.getSlope*self.points[1].x):
                if other.y <= self.points[1].y and other.y >= self.points[0].y and other.x <= self.points[1].x and other.x >= self.points[0].x:
                    return True
            else:
                return False
        else:
            return False


if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(Pantry, globals(), name='LAB2',verbose=True) # replace Pantry with the class name you want to test