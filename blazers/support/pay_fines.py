import sys
sys.path.append('..')

import blazers.db

def main():
    members = blazers.db.find('Member')
    for member in members:
        member.pay_fines()

if __name__ == '__main__':
    main()