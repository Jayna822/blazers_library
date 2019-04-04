
class MyProperty(object):

    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def getter(self, fget):
        return type(self)(fget, self.fset)

    def setter(self, fset):
        return type(self)(self.fget, fset)


class StringProperty(MyProperty):

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        if value and type(value) != str:
            raise ValueError("%s must be a string"%(self.fset.__name__))
        self.fset(obj, value)

class YearProperty(MyProperty):

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        if value:
            if type(value) != int:
                raise ValueError("%s must be a integer"%(self.fset.__name__))
            if value < 0:
                raise ValueError("%s must be positive"%(self.fset.__name__))
            self.fset(obj, value)