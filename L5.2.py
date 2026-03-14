import random

def task1():
    ll2=[]
    for i in range(3):
        temp=[]
        for j in range(3):
            num=random.randint(0,9)
            temp.append(num)
        ll2.append(temp)
    return ll2

print(task1())
def task2():
    matrix=task1()
    for i in matrix:
        print(i)


task2()