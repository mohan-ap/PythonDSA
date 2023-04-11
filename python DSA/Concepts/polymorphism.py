class SecurityForce():
    def attack(self):
        print("attack")
    def defend(self):
        print("defend")

class Army(SecurityForce):
    def attack(self):
        print("attack using tanks")
    def defend(self):
        print('defend from land')

class Navy(SecurityForce):
    def attack(self):
        print("attack using ships")
    def defend(self):
        print("defend from water")


# def fun(sf):
#     sf.attack()
#     sf.defend()

# a=Army()
# fun(a)
# n=Navy()
# fun(n)


any=[Army(),Navy()]

for i in any:
    i.attack()
    i.defend()