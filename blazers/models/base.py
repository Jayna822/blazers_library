import sys
sys.path.append('..')

import blazers.db

class LibraryObject(object):

    def __repr__(self):
        return self.__class__.__name__

    def write(self):
        clsName = self.__class__.__name__
        if clsName not in blazers.db.DB:
            raise Exception('Object cannot be written into database')
        blazers.db.DB[self.__class__.__name__].append(self)
        print blazers.db.DB
        return self