"""Collection of useful decorators.
"""
from typing import Callable, Any, Optional


__all__ = ['classgetter']


class classgetter(classmethod):
    """Class attribute getter, similar to a `property`.

    Parameters
    ----------
    func : callable(type) -> any
        Callable to be used for getting an attribute value.

    Notes
    -----
    Cannot have a setter, deleter, or custom docstring like a `property`
    due to the implementation of the descriptor model.

    References
    ----------
    .. [1] https://docs.python.org/howto/descriptor.html

    Examples
    --------
    Class getters can be defined inline:

    >>> class Foo(object):
            def get_bar(cls): return 42
            bar = classgetter(get_bar)
    >>> Foo.bar
    42
    >>> Foo().bar
    42

    or with a decorator:
    
    >>> class Foo(object):
            bar = 'SPAM'
            @classgetter
            def baz(cls):
                return cls.bar + '!'
    >>> Foo.baz
    'SPAM!'
    >>> Foo().baz
    'SPAM!'

    """
    def __init__(self, func: Callable[[type], Any]):
        # do this to make the signature less vague
        # as it would default to `classgetter(self, /, *args, **kwargs)`
        super().__init__(func)
    
    def __get__(self, obj: object, objtype: Optional[type] = None) -> Any:
        """Immediately call the class method and return its value.

        Parameters
        ----------
        obj : object
            Object calling this descriptor.
        objtype : type, optional
            Type of the object calling this descriptor.
            If `None`, defaults to `type(obj)`.

        Returns
        -------
        value : any
            Value returned by passing `objtype` as a parameter
            to the class method.
        """
        getter = super().__get__(obj, objtype)
        return getter()
