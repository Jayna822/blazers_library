import uuid
import datetime

from .base import LibraryObject
from .properties import StringProperty, YearProperty


class Item(LibraryObject):

    def __init__(self, title, year=None):
        self._id = str(uuid.uuid4())

        self.title = title
        self.year = year
        self._checkedOutTo = None
        self._checkedOutDate = None

    def __repr__(self):
        status = 'Checked out to %s'%self._checkedOutTo if self._checkedOutTo else 'Available'
        return '%s: %s, %s'%(self.__class__.__name__, self.title, status)

    @StringProperty
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @YearProperty
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def checkedOutTo(self):
        return self._checkedOutTo

    @checkedOutTo.setter
    def checkedOutTo(self, value):
        self._checkedOutTo = value

    @property
    def checkedOutDate(self):
        return self._checkedOutDate

    @checkedOutDate.setter
    def checkedOutDate(self, value):
        if value:
            if not type(value) == datetime.datetime:
                raise ValueError('CheckedOutDate must be a date')
            self._checkedOutDate = value

    @property
    def dueDate(self):
        if self.checkedOutDate:
            return self.checkedOutDate + datetime.timedelta(days=self.checkOutDayLimit())

    @property
    def daysCheckedOut(self):
        if self.checkedOutDate:
            return (datetime.datetime.today() - self.checkedOutDate).days

    @property
    def daysPastDue(self):
        if self.dueDate:
            if datetime.datetime.today() > self.dueDate:
                return (datetime.datetime.today() - self.dueDate).days

    @property
    def fine(self):
        if self.daysPastDue:
            return self.daysPastDue * self.finePerDay()

    def reset(self):
        # If I were using DAG, I would only need to reset the first two
        # But I'm not using DAG, so I gotta reset everything
        # Sorry
        self.checkedOutTo = None
        self.checkedOutDate = None
        self._dueDate = None
        self._daysCheckedOut = None
        self._daysPastDue = None
        self._fine = None




class Book(Item):

    def __init__(self, title, author, year=None):
        super(Book, self).__init__(title, year)
        self.author = author

    @StringProperty
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @classmethod
    def finePerDay(self):
        return 0.25

    @classmethod
    def checkOutDayLimit(self):
        return 21

class Movie(Item):

    @classmethod
    def finePerDay(self):
        return 1.00

    @classmethod
    def checkOutDayLimit(self):
        return 7