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
    

    
adv1 = Advocate("Elton", "Alwanga", 80000)
adv2 = Advocate("David", "Ogara", 75000)
adv3 = Advocate("Kings", "Canon", 70000)


print(adv1.pay)
adv1.apply_raise()
print(adv1.pay)

print(adv2.pay)
adv2.apply_raise()
print(adv2.pay)

print(adv3.pay)
adv3.apply_raise()
print(adv3.pay)