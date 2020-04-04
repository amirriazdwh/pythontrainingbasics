class car:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    _age_=10
    def showName(self):
        print(self.fname+"  "+self.lname)

    # fuel capacity of the car
    def SetAge(self, age):
        self._age_ =age

    def GetAge(self):
        return self._age_

vCar = car("Amir","Riaz")
vCar.showName()
vCar.SetAge(40)
print(vCar.GetAge())
print(vCar.fname)
print(vCar.lname)


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)