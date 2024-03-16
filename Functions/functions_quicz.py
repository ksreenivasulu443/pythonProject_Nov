def fun1(num):
    print(num)
    return num + 25

print(fun1(5))
print(num)

def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)