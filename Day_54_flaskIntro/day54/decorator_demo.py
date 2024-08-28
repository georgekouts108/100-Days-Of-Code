from time import sleep

def delay_decorator(function):
    def wrapper_function():
        sleep(3)
        function()

    return wrapper_function


@delay_decorator  # whenever you call this method, it will be passed into 'delay_decorator'
def say_hello():
    print("Hello there!")


@delay_decorator
def say_bye():
    print("Bye!")


def say_greeting():
    print("How are you? :)")

say_bye()