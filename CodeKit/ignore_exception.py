def ignore_exception(func):
    """
    ignore_exception will only print the exception information when the decorated function raise an exception.
    :param func: decorated function
    """
    def trigger(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as exception:
            print(exception)
        else:
            return result
    return trigger

