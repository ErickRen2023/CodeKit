import time


def timer(func):
    """
    Timer will calculate the run time of the decorated function and print run time in the Console.
    :param func: decorated function
    """
    def trigger(*args):
        start = time.time()

        result = func(*args)

        end = time.time()
        print("Run time -> %ss" % (end - start))

        return result

    return trigger
