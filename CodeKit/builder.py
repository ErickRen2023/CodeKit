def builder(cls):
    """
    Builder decorator will add all defined parameters in the constructor to the class's attributes.
    Builder's __init__ will run after the class's __init__ function.
    :param cls: origin class
    """
    origin_init = cls.__init__
    attributes = list()

    # Delete the original __init__'s first parameter: self
    if hasattr(origin_init, "__code__"):
        attributes = origin_init.__code__.co_varnames[1:]

    # Rewrite the __init__
    def __init__(self, **kwargs):
        for attr in attributes:
            try:
                self.__dict__[attr] = kwargs[attr]
            except KeyError:
                raise TypeError("__init__() missing 1 required positional argument: '%s'" % attr)

        # Verify and run the original __init__
        if hasattr(origin_init, "__code__"):
            origin_init(self, **kwargs)
        else:
            origin_init(self)

    # Overwrite the original __init__
    cls.__init__ = __init__
    return cls

