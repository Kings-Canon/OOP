#This project is based on a law firm. I am going to create a Class to actualize this
class Advocate:
    raise_bonus  = 1.45

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@aocllp.com"
    
    #Method that returns the fullname of the advocate
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    #Method that calculates the pay after the raise bonus
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_bonus)
    
    #Using a classmethod to instantiate the strings to objects of the Advocate class
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))
    
    
adv1 = Advocate("Elton", "Alwanga", 80000)
adv2 = Advocate("David", "Ogara", 75000)
adv3 = Advocate("Kings", "Canon", 70000)

#Let's say we have strings representing advocate details and we want to instantiate them as objects of the class
adv4_str = "Sandra-Ataka-65000"
adv5_str = "David-Masinde-50000"

adv4 = Advocate.from_string(adv4_str)
adv5 = Advocate.from_string(adv5_str)

print(adv4.fullname())
print(adv4.pay)
adv4.apply_raise()
print(adv4.pay)

print(adv5.fullname())
print(adv5.pay)
adv5.apply_raise()
print(adv5.pay)
