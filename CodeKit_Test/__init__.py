from CodeKit import Timer


@Timer
def TimerTest(args):
    for i in range(args):
        print(str(i))


TimerTest(99999)
