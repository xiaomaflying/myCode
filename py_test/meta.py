
def with_metaclass(meta, *bases):
    class metaclass(type):
        def __new__(cls, name, this_bases, d):
            #print 'in metaclass __new__'
            return meta(name, bases, d)
    return type.__new__(metaclass, 'tmpcls', (), {})


class MethodViewType(type):
    def __new__(cls, name, bases, d):
        rv = type.__new__(cls, name, bases, d)
        #print cls, name, bases, d
        #print 'methods' in d
        #print rv.methods

        if 'methods' not in d:
            methods = set(rv.methods or [])
            for key in d:
                if key in ('get', 'post'):
                    methods.add(key.upper())
            if methods:
                rv.methods = methods
        return rv


class View(object):
    methods = None

    @classmethod
    def as_view(cls, name, *class_args, **class_kwargs):
        print cls

class ChildView(View):
    pass

class MethodView(with_metaclass(MethodViewType, View)):
    pass


class CounterAPI(MethodView):

    def get(self):
        pass

    def post(self):
        pass

class Flask(object):
    def __init__(self, value='default'):
        self.value = value
    def _get_error_handlers(self):
        return self.value
    def _set_error_handlers(self, value):
        self.value = value
    error_handlers = property(_get_error_handlers, _set_error_handlers)
    del _get_error_handlers, _set_error_handlers

app = Flask()
app.error_handlers = 'hello'
print app.error_handlers
