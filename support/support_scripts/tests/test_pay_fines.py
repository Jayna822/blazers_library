import unittest

from blazers.managers import membermgr
from blazers.support import pay_fines


class PayFinesTest(unittest.TestCase):

    def test_pay_fines(self):
        member1 = membermgr.create('some_address@test.com')
        member2 = membermgr.create('some.other.address@test.com')
        member3 = membermgr.create('bad.member@test.com')

        member1.fines = 10
        member2.fines = 5
        member3.fines = 12

        pay_fines.main()

        self.assertEqual(member1.fines, 0)
        self.assertEqual(member2.fines, 0)
        self.assertEqual(member3.fines, 0)