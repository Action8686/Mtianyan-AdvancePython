class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a fish")


class Duck(object):
    def say(self):
        print("i am a duck")


animal = Cat
animal().say()

# java 多态class Animal，class Cat 继承 Animal 重载say方法。
animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


class Person(object):
    def __getitem__(self, item):
        return "mtianyan"


"""没有终止条件异常，死循环"""
# person = Person()
# for p in person:
#     print(p)


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        print("item:", item)
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


class Job(object):
    def __init__(self, job_list):
        self.job = job_list

    def __iter__(self):
        return self


a = ["mtianyan1", "mtianyan2"]
b = ["mtianyan2", "mtianyan"]
name_tuple = ["mtianyan3", "mtianyan4"]

name_set = set()
name_set.add("mtianyan5")
name_set.add("mtianyan6")

""" Extend list by appending elements from the iterable. """
a.extend(b)  # 调用extend方法将两个列表连成一个 tuple set 都是可迭代的，所以都可以被传入
a.extend(name_tuple)
a.extend(name_set)  # set无序 extend会调用__iter__ 或 __getitem__
print(a)


company = Company(["tom", "bob", "jane"])
a.extend(company)
print(a)

# TODO: Job iter 可迭代对象
job = Job(["Soft", "Hard", "Pm"])
for j in job:
    print(j)

# 我们只需要实现某种相关类型相关的方法
# 就可以使我们的自定义类如同list等一样可以切片，迭代等。
