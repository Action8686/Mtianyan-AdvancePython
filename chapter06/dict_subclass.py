# 不建议继承list和dict
from collections import defaultdict
from collections import UserDict


class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)
my_dict["one"] = 1
print(my_dict)


class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)
# my_dict["one"] = 1
print(my_dict)


my_dict = defaultdict(dict)
my_value = my_dict["bobby"]
pass
