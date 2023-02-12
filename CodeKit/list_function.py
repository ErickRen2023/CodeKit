def deduplicate(array, reverse=False):
    """
    Safely remove the duplicate parts in the array.It will not disturb the original sequence of the array.
    :param array: target array
    :param reverse: Reverse or not
    """
    result = list()
    if reverse:
        array = reversed(array)

    for i in array:
        if i in result:
            pass
        else:
            result.append(i)

    return result

