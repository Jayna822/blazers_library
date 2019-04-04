import unittest
import datetime

import blazers.db

from blazers.managers import membermgr, itemmgr


class MemberTest(unittest.TestCase):

    def setUp(self):
        super(MemberTest, self).setUp()

        self.member = membermgr.create(emailaddress='test@test.com')
        for i in range(15):
            itemmgr.create('Book',
                           title='Book_%d'%i,
                           author='Author_%d'%i)

        self.books = blazers.db.find('Book')

    def test_member(self):
        self.assertEqual(self.member.emailaddress, 'test@test.com')
        self.assertEqual(blazers.db.find('Member'), [self.member])

        with self.assertRaises(Exception):
            membermgr.create(emailaddress='test@test.com')

    def test_checkout(self):
        self.member.checkout(self.books[0])
        self.assertEqual(self.member.items, [self.books[0]])
        with self.assertRaises(Exception):
            self.member.checkout(self.books[0])
        self.member.checkout(self.books[1])
        self.assertEqual(self.member.items, [self.books[0], self.books[1]])

        other_member = membermgr.create('other.member@test.com')
        with self.assertRaises(Exception):
            other_member.checkout(self.books[0])
            other_member.checkout(self.books[1])

    def test_checkout_limit(self):
        for i in range(9):
            self.member.checkout(self.books[i])

        self.assertRaises(Exception, self.member.checkout(self.books[i+1]))

    def test_return(self):
        self.member.checkout(self.books[0])
        self.assertEqual(self.member.items, [self.books[0]])
        self.member.return_(self.books[0])
        self.assertEqual(self.member.items, [])
        with self.assertRaises(Exception):
            self.member.return_(self.books[0])
        self.member.checkout(self.books[0])
        with self.assertRaises(Exception):
            self.member.return_(self.books[1])

        other_member = membermgr.create('other.member@test.com')
        with self.assertRaises(Exception):
            other_member.return_(self.books[0])


    def test_fines(self):
        days_checked_out = self.books[0].checkOutDayLimit() + 1
        self.member.checkout(self.books[0], date=datetime.datetime.today() - datetime.timedelta(days=days_checked_out))
        self.member.return_(self.books[0])
        self.assertEqual(self.member.fines, self.books[0].finePerDay())
        self.member.pay_fines()
        self.assertEqual(self.member.fines, 0)

        days_to_cause_lost_privileges = self.member.max_fines() / self.books[0].finePerDay() + 1
        days_checked_out = self.books[0].checkOutDayLimit() + days_to_cause_lost_privileges
        self.member.checkout(self.books[0], date=datetime.datetime.today() - datetime.timedelta(days=days_checked_out))
        self.member.return_(self.books[0])
        self.assertEqual(self.member.fines, days_to_cause_lost_privileges*self.books[0].finePerDay())
        with self.assertRaises(Exception):
            self.member.checkout(self.books[1])
        self.member.pay_fines()
        self.member.checkout(self.books[0])
        self.assertEqual(self.member.items, [self.books[0]])

