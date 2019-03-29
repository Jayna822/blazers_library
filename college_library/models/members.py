from .properties import StringProperty

class Member(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._items = []

    def __str__(self):
        return '%s: %s, %s'%(self.__class__.__name__, self._last_name, self._first_name)

    @StringProperty
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @StringProperty
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def items(self):
        return self._items

    def checkout(self, item):
        if len(self._items) < self.checkout_limit():
            self._items.append(item)
        else:
            print('You already have %d items checked out.'%self.checkout_limit())

    def return_(self, item):
        if item in self._items:
            self._items.remove(item)
        else:
            print('You don\'t have this item checked out.')


class Teacher(Member):

    @classmethod
    def checkout_limit(self):
        return 10


class Student(Member):

    @classmethod
    def checkout_limit(self):
        return 5