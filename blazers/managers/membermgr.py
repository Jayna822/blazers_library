import sys
sys.path.append('..')

import blazers.db

def create(emailaddress, **kwargs):

    if lookup(emailaddress):
        raise ValueError(
            "Cannot create new User account because the supplied login {} is already in use".format(emailaddress))


    member = blazers.db.new('Member',
                          emailaddress=emailaddress,
                          **kwargs)
    member.write()
    return member

def lookup(emailaddress, raiseifmissing=False):
    emailaddress = emailaddress.strip().lower()

    member = blazers.db.find('Member', emailaddress=emailaddress)

    if not member and raiseifmissing:
        raise Exception('No member found with email address %s.'%emailaddress)

    if member:
        return member[0]