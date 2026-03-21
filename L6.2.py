import random
def task1():
    mat=[]
    for i in range(5):
        temp=[]
        for i in range(12):
            temp.append(random.randint(1500, 5000))
        mat.append(temp)
    return mat
matrix=task1()
for i in matrix:
    print(i)

def task2(mat):
    total = []
    for i in mat:
        total.append(sum(i))
    return total
print(task2(matrix))
salaire=task2(matrix)
def task3(salaire):
    taxe=[]
    for i in salaire:
        if i<30000:
            num=(i-10000)*0.15
            taxe.append(num)
            if i<10000:
                taxe.append(0)
        else:
            taxe.append((i-15000)*0.25)
    return taxe
print(task3(salaire))
import random
def task4():
    tableau=[]
    for i in range(30):
        li=[random.randint(-5,30) for i in range(24)]
        tableau.append(li)
    for j in tableau:
        print(j)
    avg=[]
    for i in range(30):
        avg.append(sum(tableau[i])/24)
    print(avg)

task4()
