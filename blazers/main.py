import datetime

from managers import membermgr, itemmgr
from bootstrap import bootstrap

# from models.members import Member
# from models.items import Book, Movie


def main():

    bootstrap()

    m1 = membermgr.create('jayna822@gmail.com')
    m2 = membermgr.create('another_email@gmail.com')
    # m3 = membermgr.create('jayna822@gmail.com')

    b1 = itemmgr.create('Book',
                        title='Harry Potter',
                        author='JK Rowling',
                        year=1997)
    b2 = itemmgr.create('Book',
                        title='To Kill a Mockingbird',
                        author='Harper Lee',
                        year=1962)

    m1.checkout(b1, date=datetime.datetime(2019,1,1))
    m1.return_(b1)
    print m1
    m1.pay_fines()
    m1.checkout(b1)

    # m1 = Member('jayna822@gmail.com')
    # m1.write()
    #
    # m2 = Member('someone_else@gmail.com')
    # m2.write()
    #
    # b1 = Book('Harry Potter', 'JK Rowling')
    # b2 = Book('To Kill a Mockingbird', 'Harper Lee')
    # b1.write()
    # b2.write()
    #
    # m1.checkout(b1)
    # m1.checkout(b2)
    # print m1
    #
    # m1.return_(b1)
    # print m1
    #
    # m2.checkout(b1)


if __name__ == '__main__':
    main()
