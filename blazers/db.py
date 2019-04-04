import registry

# DB = {
#           'Member': [],
#           'Book': [],
#           'Movie': []
# }

DB = {t[1]:[] for t in registry.TYPES}

def new(objtype, **kwargs):
    objclass = objtype
    if not isinstance(objtype, type):
        objclass = registry.lookup(objtype).loadclass()

    return objclass(**kwargs)

def find(objtype, **kwargs):
    objs = DB.get(objtype)
    if objs:
        matching_objs = []
        for obj in objs:
            matching_attrs = 0
            for attr, value in kwargs.items():
                if getattr(obj, attr) == value:
                    matching_attrs += 1
            if matching_attrs == len(kwargs):
                matching_objs.append(obj)
        return matching_objs

def display():
    print '---- Blazers Library Inventory ----\n'
    for itemtype, items in DB.items():
        if items:
            print '*** %ss ***'%itemtype
            print '-'*30
            for item in items:
                print item
            print '\n'