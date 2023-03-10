def to_string(cls):
    """
    to_string will overwrite the __str__ function and format all attributes.
    :param cls: origin class
    """

    def __str__(self):
        # Get the attributes
        attributes = [attribute for attribute in dir(self) if not attribute.startswith("_")]
        # Format attributes
        result = "{"
        for i in attributes:
            result += i
            result += "="
            result += str(getattr(self, i))
            if i != attributes[-1]:
                result += ", "

        result += "}"
        return result

    # Overwrite the __str__ magic method.
    cls.__str__ = __str__
    return cls
