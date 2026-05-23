import csv


def openCsv():
    file = open("oscar_age_female.csv")
    data1 = file.read()
    file.seek(0)
    data2 = csv.reader(file)
    #print(data1)
    print(data2)
    for row in data2:
        print(row)
openCsv()

def oldest():
    file = open("oscar_age_female.csv")
    data = csv.reader(file)
    oldest_age = 0
    for row in data:
        if row[2]!="Age":
            age=int(row[2])
            if age>oldest_age:
                oldest_age=age
                name = row
    print(oldest_age)
    print(name)

    
oldest()

def youngest():
    file = open("oscar_age_female.csv")
    data = csv.reader(file)
    youngest_age = 1000
    name =""
    for row in data:
        if row[2]!="Age":
            age=int(row[2])
            if age<youngest_age:
                youngest_age=age
                name = row
    print(youngest_age)
    print(name)

youngest()

def year_finder():
    file = open("oscar_age_female.csv")
    data = csv.reader(file)
    year = int(input("what year do you want to find? "))
    for i in data:
        if i[1]=="year":
            if int(i[1])==year:
                print(i)

year_finder()