#This project is based on a law firm. I am going to create a Class to actualize this
class Advocate:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@aocllp.com"
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
adv1 = Advocate("Elton", "Alwanga", 80000)
adv2 = Advocate("David", "Ogara", 75000)
adv3 = Advocate("Kings", "Canon", 70000)


print(adv1.first)
print(adv1.last)
print(adv1.email.lower())
print(adv1.pay)

print(adv2.first)
print(adv2.last)
print(adv2.email.lower())
print(adv2.pay)

print(adv3.first)
print(adv3.last)
print(adv3.email.lower())
print(adv3.pay)

print(adv1.fullname())
print(adv2.fullname())
print(adv3.fullname())
