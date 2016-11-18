import functools

def deco(f):
    print 'deco f', id(f)
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        '''wrapper doc'''
        print 'wrapper f', id(f)
        result = 'new result'
        result = 0
        if result == 0:
            return 'illegal'
        else:
            wrapper.result = result
            r = f(*args, **kwargs)
            return r

    return wrapper

@deco
def process(**kwargs):
    '''process doc'''
    print 'process', id(process)
    return 'in process'

print 'main process', id(process)
print process()
