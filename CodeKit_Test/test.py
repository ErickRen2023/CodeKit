from CodeKit import timer, builder, to_string, ignore_exception, retry, deduplicate


@timer
def time_test(args):
    for i in range(args):
        print(str(i))


time_test(args=999)


@builder
@to_string
class TestClass(object):
    def __init__(self, name, age, school):
        pass


test_class = TestClass(name="ErickRen", age=19, school="TYUT")
print([attr for attr in dir(test_class) if not attr.startswith('__')])
print(test_class)


@ignore_exception
@retry(10, ZeroDivisionError, 0.5)
def exception_test(var: int):
    print("function run.")
    result = 1 / var
    print("raise exception")
    return result


exception_test(0)


test_num = [1, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
test_letter = ["a", "a", "b", "c", "d", "d", "d", 1, 1, 2]
print(deduplicate(test_num, reverse=True))
print(deduplicate(test_letter, reverse=True))
