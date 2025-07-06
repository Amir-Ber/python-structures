import time

class CacheBusyException(Exception):
    pass


class Functionality:
    def __init__(self, **kwargs):
        super().__setattr__('_data', dict(kwargs))
        super().__setattr__('_age', None)
        super().__setattr__('_Functionality__password', None)

    # ---------------- Attribute Setting ----------------

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            self._data[name] = value

    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"No such attribute: {name}")

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __repr__(self):
        return f"Functionality({self._data})"

    # ---------------- Protected Attribute ----------------

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self._age = value

    # ---------------- Private Attribute ----------------

    def set_password(self, pwd):
        if not isinstance(pwd, str):
            raise TypeError("Password must be a string.")
        self.__password = pwd

    def get_password(self):
        return self.__password

    # ---------------- Decorator ----------------

    @staticmethod
    def timing_decorator(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"Function {func.__name__} took {end - start:.6f} seconds")
            return result
        return wrapper

    # ---------------- Iteration ----------------

    def __iter__(self):
        """
        Allows iteration over keys in _data.
        """
        return iter(self._data)

    # ---------------- Custom __dict__ ----------------

    @property
    def __dict__(self):
        """
        Combine real attributes and _data into one dict-like view.
        """
        # Real attributes:
        attrs = {k: v for k, v in super().__getattribute__('__dict__').items() if k != '_data'}

        # Combine with _data:
        return {**attrs, **self._data}
