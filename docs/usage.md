## Call in coding

### @timer

timer provide a decorator that can calculate and print the run time of the decorated function.

```python
from CodeKit import timer

@timer
def time_test(args):
    for i in range(args):
        print(str(i))

time_test(args=999)
```


```
...
998
Run time -> 0.004030704498291016s
```

### @builder

builder provide a class decorator that can add all defined parameters to the class's attributes.

```python
from CodeKit import builder

@builder
class TestClass(object):
    def __init__(self, name, age, school):
        pass


test_class = TestClass(name="ErickRen", age=19, school="TYUT")
print([attr for attr in dir(test_class) if not attr.startswith('__')])
```

```
['age', 'name', 'school']
```

### @to_string

to_string provide a decorator that can format all the attributes and overwrite the str function. 

```python
from CodeKit import builder
from CodeKit import to_string

@builder
@to_string
class TestClass(object):
    def __init__(self, name, age, school):
        pass


test_class = TestClass(name="ErickRen", age=19, school="TYUT")
print(test_class)
```

```
{age=19, name=ErickRen, school=TYUT}
```

### @ignore_exception

ignore_exception provide a decorator that can only print the exception information when the decorated function raise exception.

```python
from CodeKit import ignore_exception

@ignore_exception

def exception_test(var: int):
    print("function run.")
    result = 1 / var
    print("raise exception")
    return result

exception_test(0)
```

```
function run.
division by zero
```

@retry

retry will automatically run the decorated function when the function raise exception.

```python
from CodeKit import retry

@retry(10, ZeroDivisionError, 0.5)
def run():
    print("function run.")
    return 1 / 0
```

```
function run.
function run.
function run.
function run.
function run.
function run.
function run.
function run.
function run.
Traceback (most recent call last):
  File "D:\WorkSpace\CodeKit\CodeKit\retry.py", line 32, in <module>
    run()
  File "D:\WorkSpace\CodeKit\CodeKit\retry.py", line 17, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "D:\WorkSpace\CodeKit\CodeKit\retry.py", line 30, in run
    return 1 / 0
           ~~^~~
ZeroDivisionError: division by zero
function run.
```

It can be mixed with ignore_exception.

```python
from CodeKit import ignore_exception, retry

@ignore_exception
@retry(10, ZeroDivisionError, 0.5)
def exception_test(var: int):
    print("function run.")
    result = 1 / var
    print("raise exception")
    return result

exception_test(0)
```

```
function run.
function run.
function run.
function run.
function run.
function run.
function run.
function run.
function run.
function run.
division by zero
```


### deduplicate

Safely remove the duplicate parts in the array.It will not disturb the original sequence of the array.

```python
from CodeKit import deduplicate

test_num = [1, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
test_letter = ["a", "a", "b", "c", "d", "d", "d", 1, 1, 2]
print(deduplicate(test_num, reverse=True))
print(deduplicate(test_letter, reverse=True))
```

```
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[2, 1, 'd', 'c', 'b', 'a']
```