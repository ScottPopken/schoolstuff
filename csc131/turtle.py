import turtle

def drawSquare(t, x, y, lenght):
    t.up()
    t.goto(x,y )
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(lenght)
        t.lest(90)

def main():
    wn = turtle.screen()
    king = turtle.Turtle()
    drawSquare(king,0, 0, 250)
    #king.forward(150)
   # king.left(90)
    #king.forward(75)
    wn.exitonclick()

if __name__=='__main__':
    main()