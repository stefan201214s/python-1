def rec1(a):
    print(a)
    if a>0:
        rec1(a-1)
rec1(10)
def rec2(a):
    if a<=0:
        pass
    else:
        print(a-1)
        rec2(a-1)
rec2(11)





def fib(i):
    if i == 1:
        return 1
    if i == 0:
        return 0
    return fib(i-1)+fib(i-2)

print(fib(7))


def fib2(i):
    if i == 1:
        print(1)
        return 1
    elif i == 0:
        print(0)
        return 0
    else:
        r=fib2(i-1)+fib2(i-2)
        print(r)
        return r
fib2(7)