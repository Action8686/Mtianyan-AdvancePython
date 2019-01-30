# 我们去检查某个类是否有某种方法
import abc
from collections.abc import Sized


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(["bobby1", "bobby2"])
print(len(com))

# 判断类是否有一个属性，某个对象是否有这个函数。
print(hasattr(com, "__len__"))


class A:
    pass


class B:
    pass


# 我们在某些情况之下希望判定某个对象的类型
# Sized = _alias(collections.abc.Sized, ())
# python3.7/_collections_abc.py __subclasshook__ _check_methods(C, "__len__")
print("com is Sized: ", isinstance(com, Sized))

b = B()
print(isinstance(b, A))
# print(len(com))

# 我们需要强制某个子类必须实现某些方法
# 实现了一个web框架，集成cache(redis, cache, memory_cache)


class CacheBase(metaclass=abc.ABCMeta):
    """需要设计一个抽象基类， 指定子类必须实现某些方法,如何去模拟一个抽象基类"""
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class CacheBaseCustom:
    """调用是才会抛出异常"""

    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    """Class RedisCache must implement all abstract methods"""

    def set(self, key, value):
        pass

    def get(self, key):
        pass


"""
TypeError: Can't instantiate abstract class 
RedisCache with abstract methods get
"""
redis_cache = RedisCache()  # 初始化时就会抛异常
redis_cache.set("key", "value")
