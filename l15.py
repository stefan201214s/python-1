def task1():
    h=float(input("What is the height o fthe cone"))
    r=float(input("What is the radius o fthe cone"))
    p=1/3*3.14*h*r**2
    print("Th evolume of the cone is", p, "units.")

def task2():
    a=10
    b=20
    #op1
    a, b=b, a
    #op2
    temp=a
    a=b
    b=temp

def task3():
    names=["stef", "armon" , "karampalasis" , "alex", "marcel"]
    notes=[10, 18, 14, 5, 4]
    names=""
    meileur_notes=0
    for i in range(len(notes)):
        if notes[i] >meilleur_note:
            meilleur_note=notes[i]
            name=names[i]
    
    print('la meilleure c est ' ,meilleur_note, 'et c est a' ,name)
def task4():
    gameOn=True
    puzzle="5618"
    while gameOn:
        vache=0
        toro=0
        ans=input("give me your answer")
        for i in range(len(ans)):
            if ans[i]== puzzle[i]:
                toro+=1
            elif ans[i] in puzzle:
                vache+=1
        if toro == 4:
            gameOn=False
            print("Well done. The number was", puzzle)
        else :
            print("toro: " + str(toro))
            print("vache: " + str(vache))