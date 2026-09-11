def outer_func(func):
    def _():
        func()
        print(_)
    return _

@outer_func
def say_hello():
    print("hello")

say_hello()

f = outer_func(say_hello)
f() 
