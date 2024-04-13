import turtle
t=turtle.Pen()

letters={
    'A':['speed','pensize','left75','forward50','right145','forward50','backward15','right110','forward20','backward20','left110','forward15','left70','save'],
    'B':['speed','pensize','left90','forward40','circle-15/200','forward20','left180','circle-15/250','forward30','right180','forward50','save'],
    'C':['speed','pensize','up','forward20','down','circle25/-180','circle25/180','save'],
    'D':['speed','pensize','left90','forward45','right150','forward50','right110','forward25','left170'],
    'E':['speed','pensize','left90','forward45','right90','forward20','up','backward20','right90','forward20','left90','down','forward20','up','backward20','right90','forward25','left90','down','forward20'],
    'F':['speed','pensize','left90','forward45','right90','forward20','up','backward20','right90','forward20','left90','down','forward20','up','backward20','right90','forward25','left90','down'],
    'G':['speed','pensize','circle25/-180','up','circle25/180','down','circle15/100','left80','forward20','up','backward20','right80','circle15/-100','home','down','save'],
    'H':['speed','pensize','left90','forward45','backward20','right90','forward20','left90','forward20','backward45','right90'],
    'I':['speed','pensize','left90','forward45','left90','forward10','backward20','up','forward10','left90','forward45','left90','down','backward10','forward20'],
    'J':['speed','pensize','circle15/-90','up','circle15/90','down','left90','forward45','backward45','right90'],
    'K':['speed','pensize','left90','forward45','backward25','right45','forward25','backward25','left45','right180','left45','forward25','left45'],
    'L':['speed','pensize','left90','forward45','backward45','right90','forward25'],
    'M':['speed','pensize','left90','forward45', 'right135','forward25','left90','forward25', 'right135','forward45','left90','save'],
    'N':['speed','pensize','left90','forward45','right155','forward50','left155','forward45','backward45','right90'],
    'O':['speed','pensize','circle25'],
    'P':['speed','pensize','left90','forward45','right90','forward15','circle-15/150','right30','forward20','up','left90','forward20','left90','down'],
    'Q':['speed','pensize','circle25','up','left90', 'forward15','right120','down','forward30','left30'],
    'R':['speed','pensize','left90','forward45','right90','forward15','circle-15/150','right30','forward20','left150','forward30','left30'],
    'S':['speed','pensize','up','forward20','down','left90','circle15/-170','circle15/170','left45','forward30','circle-15/200','up','right35','forward55','down','left100'],
    'T':['speed','pensize','left90','forward45','left90','forward20','backward40','forward20','left90','forward45','left90'],
    'U':['speed','pensize','forward5','left90','up','forward10','down','circle15/-180','left180','forward30','backward30','circle-15/-180','left180','forward30','backward30','up','backward15','right90','down'],
    'V':['speed','pensize','left110','forward35','backward35','right110','left70','forward35','backward35','right70'],
    'W':['speed','pensize','left110','forward35','backward35','right110','left70','forward35','right140','forward35','left140','forward35','backward35','right140','left70'],
    'X':['speed','pensize','left110','forward45','backward45','left70','up','forward15','down','right110','forward45','backward45','right70','up','forward15','down'],
    'Y':['speed','pensize','left90','forward20','left25','forward25','backward25','right50','forward25','backward25','left25','backward20','right90'],
    'Z':['speed','pensize','left60','forward50','left117','forward25','backward25','right117','backward50', 'right60','forward25'],
    '.':['speed','.'],
    '!':['speed','pensize','.','left90','up','forward10','down','forward40','up','home','down'],
    '?':['speed','pensize','.','left90','up','forward10','down','forward5','right30','forward20','circle10/200','up','home','down'],
    ' ':['up','space','down'],
    'Patrat':['speed', 'pensize', 'forward10',  'right45', 'backward10', 'left45','forward10',  'right45']
}

drawings={}
def vorwärts():
    t.forward(10)

turtle.listen()
turtle.onkey(vorwärts, 'w')


def rückwärts():
    t.backward(10)

turtle.listen()
turtle.onkey(rückwärts, 's')


def rechts():
    t.right(45)

turtle.listen()
turtle.onkey(rechts, 'd')


def links():
    t.left(45)

turtle.listen()
turtle.onkey(links, 'a')

def up():
    t.up()
turtle.listen()
turtle.onkey(up, 'f')

def down():
    t.down()
turtle.listen()
turtle.onkey(down, 'g')

def space():
    t.reset()
