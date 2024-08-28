class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_logged_in_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_logged_in_decorator  # to make a blog post, you must be logged in
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")
