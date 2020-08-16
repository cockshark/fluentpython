class MyMeta(type):
    def __init__(self, name, bases, dic):
        super().__init__(name, bases, dic)
        print("====》Mymeta.__init__")
        print(self.__name__)
        print(dic)
        print(self.yaml_tag)

    def __new__(cls, *args, **kwargs):
        print('=======>mymeta.__new__')
        print(cls.__name__)
        return type.__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print("=======>Mymeta.__call__")
        obj = cls.__new__(cls)
        cls.__init__(cls, *args, **kwargs)
        return obj


class Foo(metaclass=MyMeta):
    yaml_tag = "!Foo"

    def __init__(self, name):
        print("Foo.__init__")
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("Foo.__new__")
        return object.__new__(cls)


foo = Foo("foo")
print(foo, type(foo))

"""
=======>mymeta.__new__
MyMeta
====》Mymeta.__init__
Foo
{'__module__': '__main__', '__qualname__': 'Foo', 'yaml_tag': '!Foo', '__init__': <function Foo.__init__ at 0x0000023CF5D8A310>, '__new__': <function Foo.__new__ at 0x0000023CF5D8A3A0>}
!Foo
=======>Mymeta.__call__
Foo.__new__
Foo.__init__

Process finished with exit code 0

"""
