import functools

class AsynTask(object):

    def __init__(self, palentires):
        self.palentire_clses = palentires

    def __call__(self, f):
        print 'common process'
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print 'before request to palentires'
            results = {}
            for cls in self.palentire_clses:
                request = cls(**kwargs)
                r = request.run()
                if r != 0:
                    key = request.__class__.__name__
                    results[key] = r
                else:
                    return 'invalid'
            wrapper.results = results
            return f(*args, **kwargs)
        return wrapper

class PalentireRequest(object):
    def __init__(self, *args, **kwargs):
        pass

    def run(self):
        raise NotImplementedError

class NDRequest(PalentireRequest):
    def run(self):
        return 1

class WDRequest(PalentireRequest):
    def run(self):
        return 1


@AsynTask([NDRequest, WDRequest])
def process(**kwargs):
    return process.results

print process(a=1, b=2)

