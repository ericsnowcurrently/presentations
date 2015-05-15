from abc import ABCMeta, abstractmethod


__all__ = ['Descriptor', 'NonDataDescriptor', 'DataDescriptor',
           'lazy', 'Lazy',
           'Attr',
           'rawattr', 'classattr', 'classonly',
           'nondata', 'classresolved', 'classunresolved',
           ]


class _ObjectWrapper:

    def __init__(self, obj, doc=None):
        if doc is None:
            doc = getattr(obj, '__doc__', None)
        self.obj = obj
        self.__doc__ = doc
        # XXX Other attrs?
        # See PEP 252: "Specification of the attribute descriptor API"
        # __name__, __objclass__

    def __repr__(self):
        return '{}({!r})'.format(self.__class__.__name__, self.obj)


class Descriptor(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, other):
        # See object.__getattribute__() (PyObject_GenericGetAttr()) and
        # type.__getattribute__() (type_getattro()).
        return hasattr(other, '__get__')

    @abstractmethod
    def __get__(self, obj, cls):
        """Return the value resolved for an attribute.

        If looked up on the class, None will be passed for obj.

        """


class NonDataDescriptor(Descriptor):

    @classmethod
    def __subclasshook__(cls, other):
        if not super(NonDataDescriptor, cls).__subclasshook__(other):
            return False
        return  not hasattr(other, '__set__')


NonDataDescriptor.register(classmethod)
NonDataDescriptor.register(staticmethod)
NonDataDescriptor.register(type(lambda:''))


class DataDescriptor(Descriptor):

    @classmethod
    def __subclasshook__(cls, other):
        # Also see PyDescr_IsData().
        if not super(DataDescriptor, cls).__subclasshook__(other):
            return False
        return hasattr(other, '__set__')

    @abstractmethod
    def __set__(self, obj, value):
        """Perform the operation of setting an attribute value."""

    # A data descriptor may also have a __delete__() method.


DataDescriptor.register(property)


class Lazy(NonDataDescriptor):
    """A late-bound class "property"."""
    # XXX Make an instance version?  Double-duty?

    def __init__(self, func, name=None):
        if name is None:
            name = func.__name__
        self.func = func
        self.__name__ = name

    def __get__(self, obj, cls):
        # Replaces itself on the class.
        #name = inspect.find_bound_class_name(self.func, cls)
        value = self.func(cls)
        setattr(cls, self.name, value)
        return value


def lazy(*args, **kwargs):
    """A decorator for late-"bound" properties."""
    if not args:
        # Handle the decorator factory case.
        return lambda f: lazy(f, **kwargs)
    kwargs.setdefault('name')
    # XXX Distinguish between lazy class attrs and lazy instance attrs.
    return Lazy(*args, **kwargs)


class Attr(NonDataDescriptor):
    """Marks an attr as defined on an instance.

    This is useful when subclassing an abstract base class where an
    abstract property is defined on the instance.

    Not meant for use as a decorator.

    """

    def __init__(self, name=None, doc=None):
        self.name = name
        self.doc = doc

    def __repr__(self):
        return '{}(name={!r}, doc={!r})'.format(self.__class__.__name__,
                                                self.name, self.doc)

    def __get__(self, obj, cls):
        if self.name is None:
            # XXX Dig up the attr name?
            pass
        if obj is None:
            return self
        raise AttributeError(self.name)


class _NonDataWrapper(_ObjectWrapper, NonDataDescriptor):

    def __get__(self, obj, cls):
        if hasattr(self.obj, '__get__'):
            return self.obj.__get__(obj, cls)
        else:
            return self.obj


class rawattr(_NonDataWrapper):
    """Mark an attribute as a raw, class-level value.

    The descriptor protocol will not be invoked on the value, even if it
    implements __get__().  Hence this is a nearly identical replacement
    for the built-in staticmethod().  Note that staticmethod also
    supports wrapping any value, not just functions.

    To force invocation of the full descriptor protocol, bind it
    unwrapped to the class (like normal).

    If a value is bound to the same name on an instance, the instance
    value will resolve (when looked up on the instance).

    May be used as a decorator.

    Example:

    >>> class Spam(object):
    ...     @rawattr
    ...     @property
    ...     def eggs(self):
    ...         return None
    >>> assert isinstance(Spam.eggs, property)
    >>> spam = Spam()
    >>> assert isinstance(spam.eggs, property)

    """
    def __get__(self, obj, cls):
        return self.obj


class classattr(_NonDataWrapper):
    """Mark an attribute as a class-level attribute.

    This is nearly identical to simply binding the object to the class
    unwrapped.  The difference is that data descriptors are treated as
    non-data descriptors and any descriptor is only resolved against the
    class.

    If a value is bound to the same name on an instance, the instance
    value will resolve (when looked up on the instance).

    May be used as a decorator, but for functions you probably should
    use classmethod or classresolved instead.

    """
    def __get__(self, obj, cls):
        return super(classattr, self).__get__(None, cls)


class classonly(classattr):
    """Mark a class attribute as class-only.

    Descriptors are resolved normally against the class.  Data
    descriptors are treated as non-data descriptors.  Non-descriptors
    are also resolved normally against the class.  None of them are
    resolved against instances (raising AttributeError instead).
    However, this is a non-data descriptor.  So if the name is also
    bound on an instance, that instance value will resolve (rather than
    the AttributeError).

    For functions, this is equivalent to classmethod, but resolves only
    on the class.

    Though a similar effect can be achieved through metaclasses, no
    metaclasses are involved for classonly().

    May be used as a decorator.

    """
    # XXX Do these still show up in dir(instance)?

    def __init__(self, obj, _functype=type(lambda:'')):
        # XXX Broaden the scope?
        if isinstance(obj, _functype):
            obj = classmethod(obj)
        super(classonly, self).__init__(obj)

    def __get__(self, obj, cls):
        if obj is None:
            return super(classonly, self).__get__(None, cls)
        else:
            # XXX Dig up the attr name?
            raise AttributeError


class _DescriptorWrapper(_ObjectWrapper):

    def __init__(self, obj, *args, **kwargs):
        if not isinstance(obj, Descriptor):
            raise TypeError('obj must be a descriptor, got {!r}'.format(obj))
        super(_DescriptorWrapper, self).__init__(obj, *args, **kwargs)


class nondata(_DescriptorWrapper, _NonDataWrapper):
    """Turns data descriptors into non-data descriptors.

    This is nearly identical to simply binding the object to the class
    unwrapped.  The difference is that data descriptors are treated as
    non-data descriptors.  So, if a value is bound to the same name on
    an instance, the instance value will resolve (when looked up on the
    instance).

    Non-data descriptors will work as though unwrapped.

    May be used as a decorator.

    Example (a non-data property):

    >>> class Spam(object):
    ...     @nondata
    ...     @property
    ...     def eggs(self):
    ...         return None
    >>> spam = Spam()
    >>> spam.eggs is None
    True
    >>> spam.eggs = 5
    >>> spam.eggs
    5

    """


class classresolved(nondata):
    """Cause a descriptor to resolve the class as the object.

    For wrapped functions, this is equivalent to the built-in
    classmethod().

    If a value is bound to the same name on an instance, the instance
    value will resolve (when looked up on the instance).

    May be used as a decorator, but you may just want classmethod.

    Example (a class-level property):

    >>> class Spam(object):
    ...     @classresolved
    ...     @property
    ...     def eggs(self):
    ...         return 3
    >>> Spam.eggs
    3
    >>> spam = Spam()
    >>> spam.eggs
    3
    >>> spam.eggs = 5
    >>> spam.eggs
    5
    >>> Spam.eggs
    3

    """
    def __get__(self, obj, cls):
        return super(classresolved, self).__get__(cls, type(cls))


# XXX Make a data descriptor version?
class classunresolved(_DescriptorWrapper, _NonDataWrapper):
    """Cause a descriptor to resolve only on instances (opposite of classonly).

    On classes the descriptor object will be returned unresolved.

    For some descriptors (like the built-in property()) this is a
    no-op.

    May be used as a decorator.
    """
    def __get__(self, obj, cls):
        if obj is None:
            # Return self rather than resolving the attribute
            return self
        else:
            return self.obj.__get__(obj, cls)
