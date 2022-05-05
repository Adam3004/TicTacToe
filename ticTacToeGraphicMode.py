import time
import turtle

list_of_moves = [' ' for _ in range(9)]

wn = turtle.Screen()
wn.title("Tic Tac Toe")
wn.bgcolor('black')
wn.setup(width=1000, height=800)
wn.tracer(0)
# dict of cords:
list_of_cords = [(-200, 200), (0, 200), (200, 200), (-200, 0), (0, 0), (200, 0), (-200, -200), (0, -200), (200, -200)]
cords = {i: list_of_cords[i - 1] for i in range(1, 10)}

# Entry board
startPen = turtle.Turtle()
startPen.speed(2)
startPen.color('white')
startPen.penup()
startPen.hideturtle()
startPen.goto(0, 270)
startPen.write('Welcome in Tic Tac Toe', align='center', font=("Courier", 50, 'normal'))
startPen.goto(0, 150)
startPen.write('Numbers 1-9 are assigned for ', align='center', font=("Courier", 30, 'normal'))
startPen.goto(0, 100)
startPen.write('x player and letters q-o are ', align='center', font=("Courier", 30, 'normal'))
startPen.goto(0, 50)
startPen.write('assigned for player o', align='center', font=("Courier", 30, 'normal'))
startPen.goto(0, 0)
startPen.write(' ', align='center', font=("Courier", 30, 'normal'))
startPen.goto(0, -50)
startPen.write('Choose player who will', align='center', font=("Courier", 30, 'normal'))
startPen.goto(0, -100)
startPen.write('start and take your', align='center', font=("Courier", 30, 'normal'))
startPen.goto(0, -150)
startPen.write('turns to play', align='center', font=("Courier", 30, 'normal'))
startPen.goto(0, -270)
startPen.write('Have fun!', align='center', font=("Courier", 40, 'normal'))
time.sleep(7)
startPen.clear()

# Quit communicate
startPen.goto(0, -380)
startPen.write('Enter \'b\' to quit', align='center', font=("Courier", 30, 'normal'))

# Board
vertical_line_one = turtle.Turtle()
vertical_line_one.color('white')
vertical_line_one.shape('square')
vertical_line_one.speed(0)
vertical_line_one.penup()
vertical_line_one.goto(-100, 0)
vertical_line_one.shapesize(stretch_wid=30, stretch_len=1)

vertical_line_two = turtle.Turtle()
vertical_line_two.color('white')
vertical_line_two.shape('square')
vertical_line_two.speed(0)
vertical_line_two.penup()
vertical_line_two.goto(100, 0)
vertical_line_two.shapesize(stretch_wid=30, stretch_len=1)

horizontal_line_one = turtle.Turtle()
horizontal_line_one.color('white')
horizontal_line_one.shape('square')
horizontal_line_one.speed(0)
horizontal_line_one.penup()
horizontal_line_one.goto(0, 100)
horizontal_line_one.shapesize(stretch_wid=1, stretch_len=30)

horizontal_line_two = turtle.Turtle()
horizontal_line_two.color('white')
horizontal_line_two.shape('square')
horizontal_line_two.speed(0)
horizontal_line_two.penup()
horizontal_line_two.goto(0, -100)
horizontal_line_two.shapesize(stretch_wid=1, stretch_len=30)


# instructions
def field(x: int, y: int, message: str):
    field_spec = turtle.Turtle()
    field_spec.speed(2)
    field_spec.color('white')
    field_spec.penup()
    field_spec.hideturtle()
    field_spec.goto(x, y)
    field_spec.write(f'{message}', align='center', font=("Courier", 30, 'normal'))


field(-200, 200, '1/q')
field(0, 200, '2/w')
field(200, 200, '3/e')
field(-200, 0, '4/r')
field(0, 0, '5/t')
field(200, 0, '6/y')
field(-200, -200, '7/u')
field(0, -200, '8/i')
field(200, -200, '9/o')


# Shapes
# circle
def circle_creator(cords: tuple):
    x = cords[0]
    y = cords[1]
    circle = turtle.Turtle()
    circle.color('white')
    circle.shape('circle')
    circle.speed(0)
    circle.penup()
    circle.shapesize(stretch_wid=8, stretch_len=8)
    circle.goto(x, y)
    second_circle = turtle.Turtle()
    second_circle.color('black')
    second_circle.shape('circle')
    second_circle.speed(0)
    second_circle.penup()
    second_circle.shapesize(stretch_wid=6, stretch_len=6)
    circle.goto(x, y)
    second_circle.goto(x, y)


# cross
def cross_creator(cords: tuple):
    x = cords[0]
    y = cords[1]
    background = turtle.Turtle()
    background.color('black')
    background.shape('square')
    background.speed(0)
    background.penup()
    background.shapesize(stretch_len=8, stretch_wid=8)
    first_line = turtle.Turtle()
    first_line.color('white')
    first_line.shape('square')
    first_line.speed(0)
    first_line.penup()
    first_line.shapesize(stretch_wid=10, stretch_len=1)
    first_line.right(45)
    second_line = turtle.Turtle()
    second_line.color('white')
    second_line.shape('square')
    second_line.speed(0)
    second_line.penup()
    second_line.shapesize(stretch_wid=10, stretch_len=1)
    second_line.right(-45)
    background.goto(x, y)
    first_line.goto(x, y)
    second_line.goto(x, y)


# x mover
def put_x_1():
    cross_creator(list_of_cords[0])
    list_of_moves[0] = 'x'
    wn.onkey(None, "1")
    wn.onkey(None, "q")


def put_x_2():
    cross_creator(list_of_cords[1])
    list_of_moves[1] = 'x'
    wn.onkey(None, "2")
    wn.onkey(None, "w")


def put_x_3():
    cross_creator(list_of_cords[2])
    list_of_moves[2] = "x"
    wn.onkey(None, "3")
    wn.onkey(None, "e")


def put_x_4():
    cross_creator(list_of_cords[3])
    list_of_moves[3] = 'x'
    wn.onkey(None, "4")
    wn.onkey(None, "r")


def put_x_5():
    cross_creator(list_of_cords[4])
    list_of_moves[4] = 'x'
    wn.onkey(None, "5")
    wn.onkey(None, "t")


def put_x_6():
    cross_creator(list_of_cords[5])
    list_of_moves[5] = 'x'
    wn.onkey(None, "6")
    wn.onkey(None, "y")


def put_x_7():
    cross_creator(list_of_cords[6])
    list_of_moves[6] = 'x'
    wn.onkey(None, "7")
    wn.onkey(None, "u")


def put_x_8():
    cross_creator(list_of_cords[7])
    list_of_moves[7] = 'x'
    wn.onkey(None, "8")
    wn.onkey(None, "i")


def put_x_9():
    cross_creator(list_of_cords[8])
    list_of_moves[8] = 'x'
    wn.onkey(None, "9")
    wn.onkey(None, "o")


# o mover
def put_o_1():
    circle_creator(list_of_cords[0])
    list_of_moves[0] = 'o'
    wn.onkey(None, "1")
    wn.onkey(None, "q")


def put_o_2():
    circle_creator(list_of_cords[1])
    list_of_moves[1] = 'o'
    wn.onkey(None, "2")
    wn.onkey(None, "w")


def put_o_3():
    circle_creator(list_of_cords[2])
    list_of_moves[2] = 'o'
    wn.onkey(None, "3")
    wn.onkey(None, "e")


def put_o_4():
    circle_creator(list_of_cords[3])
    list_of_moves[3] = 'o'
    wn.onkey(None, "4")
    wn.onkey(None, "r")


def put_o_5():
    circle_creator(list_of_cords[4])
    list_of_moves[4] = 'o'
    wn.onkey(None, "5")
    wn.onkey(None, "t")


def put_o_6():
    circle_creator(list_of_cords[5])
    list_of_moves[5] = 'o'
    wn.onkey(None, "6")
    wn.onkey(None, "y")


def put_o_7():
    circle_creator(list_of_cords[6])
    list_of_moves[6] = 'o'
    wn.onkey(None, "7")
    wn.onkey(None, "u")


def put_o_8():
    circle_creator(list_of_cords[7])
    list_of_moves[7] = 'o'
    wn.onkey(None, "i")
    wn.onkey(None, "8")


def put_o_9():
    circle_creator(list_of_cords[8])
    list_of_moves[8] = 'o'
    wn.onkey(None, "9")
    wn.onkey(None, "o")


# Key binds

wn.onkey(put_x_1, "1")
wn.onkey(put_x_2, "2")
wn.onkey(put_x_3, "3")
wn.onkey(put_x_4, "4")
wn.onkey(put_x_5, "5")
wn.onkey(put_x_6, "6")
wn.onkey(put_x_7, "7")
wn.onkey(put_x_8, "8")
wn.onkey(put_x_9, "9")

wn.onkey(put_o_1, "q")
wn.onkey(put_o_2, "w")
wn.onkey(put_o_3, "e")
wn.onkey(put_o_4, "r")
wn.onkey(put_o_5, "t")
wn.onkey(put_o_6, "y")
wn.onkey(put_o_7, "u")
wn.onkey(put_o_8, "i")
wn.onkey(put_o_9, "o")

wn.onkey(wn.bye, 'b')

wn.listen()


def is_it_end(list_of_moves: list):
    # checking are three signs in a row
    for i in range(3):
        # vertical option
        if list_of_moves[i] == list_of_moves[i + 3] == list_of_moves[i + 6] != ' ':
            vertical_end_line_creator(i)

            return list_of_moves[i], True
        # horizontal option
        if list_of_moves[0 + 3 * i] == list_of_moves[1 + 3 * i] == list_of_moves[2 + 3 * i] != ' ':
            horizontal_end_line_creator(i)

            return list_of_moves[0 + 3 * i], True
    # oblique options
    if list_of_moves[0] == list_of_moves[4] == list_of_moves[8] != ' ':
        oblique_end_line_creator(0)

        return list_of_moves[4], True
    elif list_of_moves[2] == list_of_moves[4] == list_of_moves[6] != ' ':
        oblique_end_line_creator(1)

        return list_of_moves[4], True

    return '_', False


def end_action(sign: str):
    # Unbind keys
    wn.onkey(None, "q")
    wn.onkey(None, "w")
    wn.onkey(None, "e")
    wn.onkey(None, "r")
    wn.onkey(None, "t")
    wn.onkey(None, "y")
    wn.onkey(None, "u")
    wn.onkey(None, "i")
    wn.onkey(None, "o")

    wn.onkey(None, "1")
    wn.onkey(None, "2")
    wn.onkey(None, "3")
    wn.onkey(None, "4")
    wn.onkey(None, "5")
    wn.onkey(None, "6")
    wn.onkey(None, "7")
    wn.onkey(None, "8")
    wn.onkey(None, "9")

    # create pen to write ending text
    endPen = turtle.Turtle()
    endPen.speed(2)
    endPen.color('white')
    endPen.penup()
    endPen.hideturtle()
    endPen.goto(0, 350)
    endPen.write(f'{sign} won', align='center', font=("Courier", 30, 'normal'))


def draw():
    endPenDraw = turtle.Turtle()
    endPenDraw.speed(2)
    endPenDraw.color('white')
    endPenDraw.penup()
    endPenDraw.hideturtle()
    endPenDraw.goto(0, 350)
    endPenDraw.write('draw', align='center', font=("Courier", 30, 'normal'))
    return True


def vertical_end_line_creator(x: int):
    if x == 0:
        x = -200
    elif x == 1:
        x = 0
    else:
        x = 200
    verticalEndLine = turtle.Turtle()
    verticalEndLine.color('green')
    verticalEndLine.shape('square')
    verticalEndLine.speed(0)
    verticalEndLine.penup()
    verticalEndLine.shapesize(stretch_wid=30, stretch_len=1)
    verticalEndLine.goto(x, 0)


def horizontal_end_line_creator(y: int):
    if y == 0:
        y = 200
    elif y == 1:
        y = 0
    else:
        y = -200
    horizontalEndLine = turtle.Turtle()
    horizontalEndLine.color('green')
    horizontalEndLine.shape('square')
    horizontalEndLine.speed(0)
    horizontalEndLine.penup()
    horizontalEndLine.shapesize(stretch_wid=1, stretch_len=30)
    horizontalEndLine.goto(0, y)


def oblique_end_line_creator(option: int):
    if option == 1:
        option = -45
    else:
        option = 45
    obliqueEndLine = turtle.Turtle()
    obliqueEndLine.color('green')
    obliqueEndLine.shape('square')
    obliqueEndLine.speed(0)
    obliqueEndLine.penup()
    obliqueEndLine.shapesize(stretch_wid=1, stretch_len=40)
    obliqueEndLine.goto(0, 0)
    obliqueEndLine.right(option)


is_ended = False
if __name__ == '__main__':
    while True:
        wn.update()
        end_checker, is_ended = is_it_end(list_of_moves)
        if end_checker != '_':
            end_action(end_checker)
        #       if moves are ended
        if ' ' not in list_of_moves and not is_ended:
            is_ended = draw()
