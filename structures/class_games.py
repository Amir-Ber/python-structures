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






# DataBase class as provided
class DataBase:
    def __init__(self, data):
        self.__data = data

    def get(self, id):
        print(' -- DB Access for:', id)
        return self.__data[id]

    def update(self, id, field, value):
        print(' -- DB Update for:', id)
        self.__data[id][field] = value


# Initialize DB
db = DataBase(
    {
        1: { "price": 13, "age": 100 },
        2: { "price": 43, "height": 200 },
        3: { "age": 2, "name": "David", "price": 21 },
        4: { "age": 77, "name": "Haim", "price": 20 }
    }
)

# Fetch a record
record_data = db.get(2)

# Wrap in Functionality
f = Functionality(**record_data)

# Test dot-notation
print(f.price)           # 43
print(f.height)          # 200

# Update fields
f.price = 999
print(f.price)           # 999
print(f["price"])        # 999

# Test protected attribute
f.age = 50
print(f.age)             # 50

# Test private attribute
f.set_password("secret123")
print(f.get_password())  # secret123

# Test iteration
for key in f:
    print(f"Key: {key} → Value: {f[key]}")

# Test __dict__
print(f.__dict__)

