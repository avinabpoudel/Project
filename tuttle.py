import turtle
t = turtle.Turtle()
s = turtle.Screen()

colors = ['red', 'green' ,'purple', 'yellow' ,'orange','blue' ]

s.bgcolor('black')
t.speed('fastest')
t.hideturtle()

while True:
    for x in range(200):
        t.pencolor(colors[x%len(colors)])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(59)
    t.right(239)

    for x in range (200,0,-1):
        t.pencolor('black')
        t.width(x/100 + 7)
        t.forward(x)
        t.right(59)


#Activity no 2

# turtle.Screen().bgcolor("Orange")
# board = turtle.Turtle()

# board.forward(100)
# board.left(120)
# board.forward(100)
# board.left(120)
# board.forward(100)

# board.penup()
# board.right(150)
# board.forward(50)

# board.pendown()
# board.right(90)
# board.forward(100)

# board.right(120)
# board.forward(100)
# board.right(120)
# board.forward(100)


# board.forward(100)
# board.left(120)
# board.forward(100)
# board.left(120)
# board.forward(100)

# board.left(30)
# board.forward(140)
# board.left(90)
# board.forward(100)
# board.left(90)
# board.forward(140)

# board.penup()
# board.left(90)
# board.forward(70)
# board.left(90)
# board.forward(70)

# board.pendown()
# board.forward(70)
# board.penup()

# board.left(180)
# board.forward(70)
# board.right(90)
# board.pendown()
# board.forward(40)
# board.right(90)
# board.forward(70)



# turtle.done()