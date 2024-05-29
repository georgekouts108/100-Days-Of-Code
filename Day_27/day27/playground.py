def print_all(*args):
    for n in args:
        print(n)


def add_nums(*args):
    return sum([arg for arg in args])


def add_nums2(*args):
    return sum([arg for arg in args if str(type(arg)) in ['<class \'int\'>', '<class \'float\'>']])


def foo(**kwargs):
    print(kwargs)


foo(a=5, b=6, c=7)  # kwargs is a dictionary: {'a': 5, 'b': 6, 'c': 7}
