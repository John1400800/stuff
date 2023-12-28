# decorator
def decorator(func):

    def inner():
        print('start decorator...')
        func()
        print('finish decorator...')

    return inner
