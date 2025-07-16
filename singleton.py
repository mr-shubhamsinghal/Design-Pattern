# Singleton Pattern (Creational Design Pattern)

class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class Hello(metaclass=Singleton):
    def __init__(self, value):
        self.value = value


h1 = Hello(1)
h2 = Hello(2)

print(id(h1))  # Should be the same for both h1 and h2
print(h1.value)  # Should be 1, because the Singleton instance is reused
print(id(h2))  # Should be the same as h1's id
print(h2.value)  # Should be 1, not 2, because they are the same instance


### Singleton standalone class implementation

# class Hello:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super(Hello, cls).__new__(cls)
#         return cls._instance

#     def __init__(self, value):
#         if not hasattr(self, 'value'):
#             self.value = value

# h1 = Hello(1)
# h2 = Hello(2)

# print(id(h1))
# print(h1.value)
# print(id(h2))
# print(h2.value)
