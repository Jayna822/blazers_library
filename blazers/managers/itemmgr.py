import sys
sys.path.append('..')

import blazers.db

def create(itemtype, title, **kwargs):
    item = blazers.db.new(itemtype,
                          title=title,
                          **kwargs)
    item.write()
    return item
