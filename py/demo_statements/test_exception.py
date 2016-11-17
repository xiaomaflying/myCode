#encoding=utf-8


def test1():
    u"""异常的通用写法."""
    raise Exception
    raise Exception, "This is a Exception"
    raise Exception("This is a Exception")


def test2():
    u"""常用内置的Exception介绍以及异常捕捉."""
    import exceptions
    print dir(exceptions)

    # raise KeyError
    d = {}
    d['key']

    # raise AttributeError
    d.keys
    d.not_found

    # Catch IndexError
    try:
        l = []
        l[0]
    except IndexError as e:
        print 'I catch the IndexError Exception'
        print e.message

    # 所有的异常都是Exception的子类，可以通过捕捉Exception来捕捉所有异常情况
    # catch Exception as e


def test3():
    u"""多个异常捕捉语句.

    1. 多个异常，第一个捕捉异常之后就不再继续捕捉；
    2. finally，不管是否捕捉到异常，一定会执行，即使有捕捉异常里面有return语句；
    3. 捕捉异常处理之后，如果还想把原有异常抛出，用不带参数的raise即可。
    """
    try:
        x = input("Enter the first number: ")
        y = input("Enter the second number: ")
        print x/y
    except ZeroDivisionError:
        print 'The second number could not be zero!'
    except TypeError:
        print 'Your input may be not a integer!'
    except Exception:
        # raise the origin Exception
        print 'Other exception happened!'
        # return 0
        raise
    else:
        print 'Your input is right!'
    finally:
        # use finally. Though there is a return sentence
        print 'Finally this sentence must be executed!'


if __name__ == '__main__':
    print test3()
