def printer():
    print("Hello mark")

printer()

def printerbis(x):
    print(x)
mot= "nutela"
printerbis(mot)

def estPremier(num):
    premier = True
    for i in range(2, num):
        if num % i ==0:
            premier = False
    if premier:
        print(num, "est un nombre premier")
    else:
        print(num, "n'est pas un nombre premier")

nombre = int(input("choisis un nombre de 1-10"))
estPremier(nombre)
