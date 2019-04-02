import datetime

from .base import LibraryObject
from .properties import StringProperty


class Member(LibraryObject):

    def __init__(self, emailaddress):
        self._emailaddress = emailaddress
        self._items = []
        self.fines = 0.0

    def __repr__(self):
        return '%s: %s'%(self.__class__.__name__, self._emailaddress)

    def __str__(self):
        return '%s: %s'%(self.__class__.__name__, self._emailaddress) + \
               '\nChecked Out: ' + ','.join([item.title for item in self._items]) + \
               '\nFines: $%.2f'%self._fines

    @classmethod
    def checkout_limit(self):
        """
        The maximum number of items a member can have checked out at one time.
        :return:
        """
        return 10

    @classmethod
    def max_fines(self):
        """
        The maximum amount of fines a member can have before losing checkout privileges.
        :return:
        """
        return 10.00

    @StringProperty
    def emailaddress(self):
        return self._emailaddress

    @emailaddress.setter
    def emailaddress(self, value):
        self._emailaddress = value

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

    @property
    def fines(self):
        return self._fines

    @fines.setter
    def fines(self, value):
        self._fines = value

    def checkout(self, item, date=None):
        if item.checkedOutTo:
            raise Exception('This item is already checked out by %s'%str(item.checkedOutTo))
        if self.fines >= self.max_fines():
            raise Exception('Member fines ($%.2f) are too high to check out any items.'%self.fines)
        if len(self._items) >= self.checkout_limit():
            raise Exception('You already have %d items checked out.' % self.checkout_limit())
        self._items.append(item)
        item.checkedOutTo = self
        item.checkedOutDate = date if date else datetime.datetime.today()

    def return_(self, item):
        if item in self._items:
            self._items.remove(item)
            item.checkedOutTo = None
            item.checkedOutDate = None
            if item.fine:
                print 'This item is past due. A fine of $%.2f will be applied to your account.'%item.fine
                self.fines += item.fine
                item.reset()
        else:
            raise Exception('You don\'t have this item checked out.')

    def pay_fines(self):
        self.fines = 0.0
        print 'Thank you for paying off your fines!'

    def renew(self, item):
        pass
