import random

def task1():
    nums=[]
    while True:
        num=random.randrange(1,100)
        nums.append(num)
        if len(nums)>=10:
            break

    return nums
    


nums=task1()

def task2(nums):
    evenl=[]
    for i in nums:
        if i % 2 == 0:
            evenl.append(i)
    return evenl
print(task2(nums))
task2(nums)

def task3(nums):
    evenl=[]
    for i in nums:
        if i % 2 == 0:
            yield i
for i in task3(nums):
    print (i)







