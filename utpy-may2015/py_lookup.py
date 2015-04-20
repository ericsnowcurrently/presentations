import inspect


def _PyType_Lookup(cls, name):
    # See Objects/typeobject.c.
    value = inspect._check_class(cls, name)
    if value is inspect._sentinel:
        raise AttributeError(name)
    return value


def type_lookup(obj, name, default=None, *, cls=None):
    if cls is None:
        cls = type(obj)
    try:
        return _PyType_Lookup(cls, name)
    except AttributeError:
        return default


def _obj_dict(obj, cls):
    descr = type_lookup(obj, '__dict__', cls=cls)
    if descr is None:
        return None
    getter = type_lookup(descr, '__get__')
    if getter is None:
        return None
    return getter(descr, obj, cls)


def _PyObject_GenericGetAttr(obj, name):
    # See Objects/object.c.
    cls = type(obj)  # not obj.__class__
    getter = None

    # Handle data descriptors first.
    descr = type_lookup(obj, name, cls=cls)
    if descr is not None:
        getter = type_lookup(descr, '__get__')
        if getter is not None and type_lookup(descr, '__set__') is not None:
            return getter(descr, obj, cls)

    # Try the object __dict__ next.
    ns = _obj_dict(obj, cls)
    if ns is not None:
        try:
            return ns[name]
        except KeyError:
            pass

    # Fall back to non-data descriptors.
    if getter is not None:
        return getter(descr, obj, cls)

    # __getattr__ is tried elsewhere if it exists.

    raise AttributeError("'{}' object has no attribute '{}'"
                         .format(cls.__name__, name))


def lookup(obj, name):
    try:
        return _PyObject_GenericGetAttr(obj, name)
    except AttributeError:
        # Finally, try __getattr__ (see slot_tp_getattr_hook in typeobject.c).
        cls = type(obj)
        getattr = type_lookup(obj, '__getattr__', cls=cls)
        if getattr is None:
            raise
        return getattr(obj, name)


if __name__ == '__main__':
    expected = object()
    eggs = property(lambda self: expected)

    class Spam:
        eggs = eggs
        #@property
        #def eggs(self):
        #    return expected

    spam = Spam()

    print('validating...')
    assert spam.eggs is expected
    assert lookup(spam, 'eggs') is expected
    assert type_lookup(spam, 'eggs') is eggs
