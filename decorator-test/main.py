
def decorator(a_func):
    def warp(*args):
        print("before")
        a_func(*args)
        print("after")
    return warp




@decorator
def func(*args):
    print("function div")
    num = 1
    print(args)
    for i in args:
        print(i)
        num *= i
    print(num)

@decorator
def func2(*args):
    print("function div")
    num = 1
    print(args)
    for i in args:
        print(i)
        num *= i
    print(num)


func2(1,5)
