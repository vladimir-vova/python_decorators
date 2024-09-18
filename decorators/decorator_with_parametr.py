from builtins import isinstance


def type_id(type_):
    def concat(function):
        def wrapped(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError
            print('Decorator')
            return function(*args)
        return wrapped
    return concat


@type_id(str)
def text(a, b):
    return a + b

if __name__ == '__main__':
    print(text('1', '2'))