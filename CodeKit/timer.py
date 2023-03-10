import time


def timer(func):
    """
    timer will calculate the run time of the decorated function and print run time in the Console.
    :param func: decorated function
    """
    def trigger(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print("Run time -> %ss" % (end - start))

        return result

    return trigger
