from functools import wraps

def oauth(view):
    @wraps(view)
    def wrapper(self, request, **kwargs):
        return view(self, request, **kwargs)
    return wrapper
