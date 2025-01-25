"""
 super() -> same as super(__class__, <first argument>)
        super(type) -> unbound super object
        super(type, obj) -> bound super object; requires isinstance(obj, type)
        super(type, type2) -> bound super object; requires issubclass(type2, type)
"""


class Person :
    def __init__ ( self , first , last ) :
        self.firstname = first
        self.lastname = last

    def Name ( self ) :
        return self.firstname + " " + self.lastname


class Employee ( Person ) :
    def __init__ ( self , first , last , staffnum ) :
        #        super ( ).__init__ ( first , last )
        super ( Employee , self ).__init__ ( first , last )
        self.staffnumber = staffnum

    def GetEmployee ( self ) :
        return self.Name ( ) + ", " + self.staffnumber

    def Name ( self ) :
        return self.firstname + " " + self.lastname + " " + self.staffnumber


x = Person ( "Marge" , "Simpson" )
y = Employee ( "Homer" , "Simpson" , "1007" )

print ( x.Name ( ) )
print ( y.GetEmployee ( ) )
print ( y.Name ( ) )


# Python example to check if a class is
# subclass of another

class Base ( object ) :
    pass  # Empty Class


class Derived ( Base ) :
    pass  # Empty Class


# Driver Code
print ( issubclass ( Derived , Base ) )
print ( issubclass ( Base , Derived ) )

d = Derived ( )
b = Base ( )

# b is not an instance of Derived
print ( "This is an instance of Derived Class %s" % isinstance ( b , Derived ) )

# But d is an instance of Base
print ( isinstance ( d , Base ) )


class Employee :
    """Common base class for all employees"""
    # static variable
    empCount = 0

    def __init__ ( self , name , salary ) :
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod
    def displayCount ( self ) :
        print ( "Total Employee %d" % Employee.empCount )

    @classmethod
    def displayEmployee ( self ) :
        print ( "Name : " , self.name , ", Salary: " , self.salary )


emp1 = Employee ( "amir riaz" , 40 )
print ( emp1.empCount )
emp2 = Employee ( "Kashif riaz" , 30 )
print ( emp1.empCount )

print ( Employee.empCount )


class MyClass :
    def f_instance ( self ) :
        pass

    @classmethod
    def f_class ( cls ) :
        pass

    @staticmethod
    def f_static ( ) :
        pass

    """
    Instance methods are bound to the instance of a class (not the class itself)
    Class methods are bound to the class, not instances
    Static methods are no bound either to the class or its instances
    """


class A :
    def __init__ ( self , name ) :
        self.name = name

    def message ( self , source ) :
        print ( f"From: {source}, class: A, object: {self.name}" )


class B ( A ) :
    def __init__ ( self , name ) :
        self.name = name

    def message ( self , source ) :
        print ( f"From: {source}, class: B, object: {self.name}" )


class C ( A ) :
    def __init__ ( self , name ) :
        self.name = name

    def message ( self , source ) :
        print ( f"From: {source}, class: C, object: {self.name}" )


class D ( B , C ) :
    def __init__ ( self , name ) :
        self.name = name

    def message ( self , source ) :
        print ( f"From: {source}, class: D, object: {self.name}" )


a = A ( "a" )
b = B ( "b" )
c = C ( "c" )
d = D ( "d" )

print ( D.__mro__ )

"""
MRO rules. 
1.   always start from the left side class
2.   build graph
3.   in graph remove the classes who subtype comes to right.   

in case of a diamond  and for classes.    A, B, C , D    D is subtype of both B and C
our graph is with B coming first :
D->B->A->object->C->A->object.  
D->B->C->A

(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

means if method is found is B it will be execute,   if not
it will be looked in C if not found it will be look in A
"""
