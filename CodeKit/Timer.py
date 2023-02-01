import time


def Timer(func):
    def trigger(*args):
        start = time.time()

        result = func(*args)

        end = time.time()

        print("Run time -> %ss" % (end - start))

        return result

    return trigger
