import utils


TYPES = (
    # ( 1,            'Library',                      'blazers.models.library'),
    ( 2,            'Member',                      'blazers.models.members'),
    ( 3,            'Book',                         'blazers.models.items'),
    ( 4,            'Movie',                        'blazers.models.items')

)

class TypeInfo(object):

    TYPEMAP = {}

    def __init__(self, typeid, clsname, modname):
        self.typeid = typeid
        self.clsname = clsname
        self.modname = modname
        self.loadedclass = None

    def loadclass(self):
        if not self.loadedclass:
            cls = utils.loadClass(self.modname, self.clsname)
            # cls.TYPE_ID = self.typeid
            self.loadedclass = cls
        return self.loadedclass

    @classmethod
    def _add(cls, typeinfos):
        zipper = [(typeinfo.typeid, typeinfo) for typeinfo in typeinfos]
        zipper = zipper + [(typeinfo.clsname, typeinfo) for typeinfo in typeinfos]
        cls.TYPEMAP.update(dict(zipper))


MISSING_TYPE = TypeInfo(0, 'UNKNOWN', 'UNKNOWN')

def types():
    return [TypeInfo(*x) for x in TYPES]


def exists(typeid):
    return TypeInfo.TYPEMAP.get(typeid) is not None


def lookup(typeid, failIfMissing=True):
    found = TypeInfo.TYPEMAP.get(typeid, MISSING_TYPE)
    if found is MISSING_TYPE and failIfMissing:
        raise ImportError('typeid {} not registered'.format(typeid))
    return found


# initialize registry on module load
TypeInfo._add(types())