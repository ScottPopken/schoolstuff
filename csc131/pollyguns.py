import turtle

def regular_pol(t: Turtle, n: int, length: int, shape)->None:
    for count in range(n):
        shape(t, length)
        t.left(360 / n)

def square(t: Turtle, length: int):
    """
    draw a square with  a giv len
    :param t: an instance of a Turtle
    :param length: the length of a side
    :return:
    """
    for count in range(4):
        t.forward(length)
        t.left(90)
def hexagon(t: Turtle, length: int):
    """
        draw a square with  a giv len
        :param t: an instance of a Turtle
        :param length: the length of a side
        :return:
        """
    for count in range(6):
        t.forward(length)
        t.left(60)
def taranle(t: Turtle, length: int):
    """
           draw a square with  a giv len
           :param t: an instance of a Turtle
           :param length: the length of a side
           :return:
           """
    for count in range(3):
        t.forward(length)
        t.left(120)
def oxcgon(t: Turtle, length: int):
    """
               draw a square with  a giv len
               :param t: an instance of a Turtle
               :param length: the length of a side
               :return:
               """
    for count in range(8):
        t.forward(length)
        t.left(45)
def main ():
    Turtle = turtle
    king = Turtle()
    screen = Screen()
    regular_pol(king, n = 10, length=50, shape=square)
    square(king, 300)

if __name__=='__main__':
    main()
