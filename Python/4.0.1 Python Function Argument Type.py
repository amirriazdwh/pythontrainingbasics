"""
1.  the argument inside function are called formal arguments
2.   the value which are passed to function are called actual arguments
3.  arguments are passed to functions as reference.  They are not passed by values.
4.  there are four types of function Arguments in python.
    a.  positional argument
    b.  key work
    c.  default
    d.  variable length
"""

# variable passed by position.
def person (fname, lname):
    print("person first name : {0}, second name {1}".format(fname, lname))
person("scott","tiger")

# variable passed by key.
person(fname="scott", lname="tiger")

# variable passed by default values.  the default variable
# are created in static scope.
def person (fname="scott", lname="tiger"):
    print("person first name : {0}, second name {1}".format(fname, lname))

person()

#there are two types of variable length.  *args and **Kargs

# *args method,  uses for list , set , array etc.
def person_var (*vname):
    for names in vname:
        print("person first name : {0}".format(names))

person_var("scott", "tiger", "john","linda")

# passing list to finite arguments
lname =["scott", "tiger"]
person(*lname)

# **kargs used for dictionaries.
dname ={ "fname":"scott", "lname":"tiger"}
print(dname)

def person_dict (**kargs):
    print("person first name : {0}, second name {1}".format(kargs["fname"], kargs["lname"]))
# a dictionary is passed by key method
person_dict(fname="scott", lname="tiger")


def person_dict2 (**vname):
    for names in vname.items():  #key for key #values for values
        print("person first name : {0}".format(names))
person_dict2(fname="scott", lname="tiger")

#there dictionary is being passed to regular funcitons
# here the function argumnet are fname and lname
# this should match exactly in diction as
#dname ={ "fname":"scott", "lname":"tiger"}

person(**dname)

"""
please note that *name is translated by compiler 
list(x for x in name)
then this tuple  is passed to function

in case fnc(*arg) and call is fnc(1,2,3,4)
a generator is being create from (1,2,3,4) tuple and
then that generator is being passed.
"""

