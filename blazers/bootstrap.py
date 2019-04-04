from managers import membermgr, itemmgr

def bootstrap():
    member_args = ('emailaddress', 'first_name', 'last_name')
    members = [
        ('jim.martin@address.com', 'Jim', 'Martin'),
        ('jane.jones@address.com', 'Jane', 'Jones')
    ]

    for member in members:
        membermgr.create(**dict(zip(member_args, member)))

    book_args = ('title', 'author')
    books = [
        ('Harry Potter', 'JK Rowling'),
        ('To Kill a Mockingbird', 'Harper Lee'),
        ('1984', 'George Orwell'),
        ('War and Peace', 'Leo Tolstoy'),
        ('Frankenstein', 'Mary Shelley')
    ]

    for book in books:
        kwargs = dict(zip(book_args, book))
        kwargs['itemtype'] = 'Book'
        itemmgr.create(**kwargs)


def main():
    bootstrap()

if __name__ == '__main__':
    main()