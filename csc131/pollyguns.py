for turtle import Turtle

def regular_pol(t: Turtle, length: int, num_sides=4):
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
    king = Turtle()
    square(king, 300)

if __name__=='__main__':
    main()
