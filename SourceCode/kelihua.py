def add(x,y):
    return x + y

def new_add(x):
    def foo(y):
        return x + y
    print(id(foo))
    return foo

# foo = new_add(1)(3)
# print(foo)

foo1 = new_add(4)
print(foo1(7))

print(id(foo1))