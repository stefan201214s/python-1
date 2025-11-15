def task1():
    firstList=[]
    print(firstList)
    firstList.append(97)
    print(firstList)
    firstList.append("hello")
    print(firstList)
task1()

def task2():

    names = ["Amelie","Julianna","Emilia","Luna","laura",]
    print("First personne",names[0])
    print(" last personne",names[4])
    print(" last personne",names[len(names)-1])
    print(" last personne",names[-1])
    print("promo")
    print(names[0:3])
    print(names[:3])
    print("peno")
    print(names[3:5])
    print(names[3:])

def task3():
    list_1 = [2,8,6,21,8,6,2,98,3]
    print(list_1)
    list_1.insert(2,9)
    print(list_1)
    list_1.insert(20,9)
    print(list_1)
    list_1.pop(4)
    print(list_1)
    list_1.remove(98)
    print(list_1)
task3()
