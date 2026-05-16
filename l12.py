def openFile():
    file = open("test.txt","r")
    data = file.read()
    print(data)
    file.close()
openFile()
def writeReadFile():
    file = open("test.txt","a+")
    file.write("helle le frere de stef")
    file.seek(0)
    data = file.read()
    print(data)
    file.close()
#openFile()
#writeReadFile()


def readLines():
    file = open("test.txt","r")
    data1 = file.read()
    file.seek(0)
    data2 = file.readlines()
    file.seek(0)
    data3 = file.readlines()
    print(data1)
    print(data2)
    print(data3)
readLines()

def Rline():
    file = open("test.txt","r")
    data = file.readlines()
    for line in data:
        print(line)
Rline()