import sys
sys.path.append('..')


def loadModule(name):
    if isinstance(name, basestring):
        mod = __import__(name.strip())
        for part in name.split('.')[1:]:
            mod = getattr(mod, part)
        return mod


def loadClass(moduleName, className):
    try:
        return getattr(loadModule(moduleName), className)
    except Exception as e:
        raise