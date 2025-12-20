
def task1():
    nums=[1,1,1,2,2,2,1,1,3,3,4,5,4,5,6,7,6,7]
    new_nums=[]
    for num in nums:
        if num not in new_nums:
                new_nums.append(num)
        print(nums)
        print(new_nums)
task1()
def task2():
    nums=[]
    for i in range(10):
        num=int(input("Give me num : "))
        nums.append(num)
    pair=0
    impair=0
    positive=0
    negative=0
    zero=0
    for nbr in nums:
        if nbr > 0:
            positive+=1
        if nbr < 0:
            negative += 1
        if nbr == 0:
            zero += 1
        if i%2 == 0:
            pair+= 1
        if i%2==1 : 
            impair+=1
    
    print("pair: ",pair)
    print("impair:",impair)
    print(" negative:",negative)
    print("zero", zero)
    print("positive", positive)
task2()