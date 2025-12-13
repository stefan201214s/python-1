familly_names = ["kosondi", "karampalasis"]
names=["luc","alex", " stefan","nicolas", "alexandros", "marcel"]
for familly_names in familly_names:
    for name in names:
        print(name+""+ familly_names)

import turtle
turtle.getscreen()
pen=turtle.Turtle()
pen.color('black')
pen.fillcolor("red")
pen.begin_fill()
for i in range(7):
    pen.forward(100)
    pen.left(90)
for i in range(1):
    pen.right(150)
for i in range(3):
    pen.right(60)
    pen.forward(100)
    pen.right(60)


pen.end_fill()



turtle.exitonclick()