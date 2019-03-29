from .properties import StringProperty, YearProperty

class Item(object):

    def __init__(self, title, year=None):
        self.title = title
        self.year = year

    def __str__(self):
        return '%s: %s'%(self.__class__.__name__, self.title)

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


class Movie(Item):
    pass