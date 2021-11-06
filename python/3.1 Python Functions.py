



class Printer:

    def __init__(self, s):
        self.str01 = s

    def __call__(self):
         return self.str01.upper()


s1 = Printer('hello') # Defining object of class Printer
# Calling object s1
s2=s1()   # Hello
print(s2)
