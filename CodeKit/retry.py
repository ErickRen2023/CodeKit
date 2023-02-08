import time


def retry(retry_times, exception=Exception, interval=0.2):
    """
    retry will automatically run the decorated function when the function raise exception.
    :param retry_times: Retry max times.
    :param exception: Exception  listened for.
    :param interval: Interval time.
    """
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            count = 0
            while True:
                # noinspection PyBroadException
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    count += 1
                    if count >= retry_times:
                        raise
                    time.sleep(interval)
        return wrapper
    return out_wrapper
