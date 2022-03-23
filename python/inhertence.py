class Employee ( object ) :
    def __new__ ( cls , *args , **kwargs ) :
        if not hasattr ( cls , '_inst' ) :
            print ( cls )
            cls._inst = super ( Employee , cls ).__new__ ( cls )
            # if Python3 is written the same way as Python2 like below, it will throw error "TypeError: object()
            # takes no parameters"
            # cls._inst = super(Employee, cls).__new__(cls, *args,**kwargs)
        return cls._inst

