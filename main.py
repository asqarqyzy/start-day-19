import turtle as t

tim = t.Turtle()
screen = t.Screen()

def forward():
    return tim.forward(10)


def backward():
    return tim.backward(10)


def counter_clockwise():
    return tim.left(10)


def clockwise():
    return tim.circle(50, 10)

def clear():
    tim.home()
    tim.clear()



screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=clear)

screen.listen()


screen.exitonclick()