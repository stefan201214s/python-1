
def task1():
    x_pos = int(input("What is the x position?\n"))
    y_pos = int(input(" what is the y position?\n"))
    if x_pos >=0:
        if x_pos >=0:
            print("1")
        else:
            print("2")
    else:
        if y_pos >=0:
            print("3")
        else:
            print("4")

def Pgdc():
    number_1= int(input("what is the lowest number?\n"))
    number_2= int(input("what is the height number?\n"))
    gdc = 1
    for i in range(1,number_1+1):
        if number_1 % i == 0 and number_2 % i == 0:
            gdc = i
    print(gdc)
Pgdc()
