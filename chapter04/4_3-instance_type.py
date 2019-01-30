class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B))
print(isinstance(b, A))

print(type(b))
# == 是判断值是否相等
print(type(b) == B)
# is是判断是不是一个对象，即id是否相同
print(type(b) is B)
print(type(b) is A)

print(isinstance(b, A))
