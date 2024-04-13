
from logik.letters import *
def menu():
    return"""
    Turtle Paint v1.0

    1. Textnachricht zeichnen
    2. Neues Zeichen hinzufügen
    3. Das benutzerdefinierte Zeichen zeichnen
    0. Exit

    """
def reafist_text(name):
    p=[]
    f=open('desen.txt','r')
    actions=f.readlines()
    for comand in actions[1:]:
        p.append(comand.strip())

    letters[name] = p
    print(letters[name])
    f.close()

def move_turtle(new_x, new_y):
    t.up()
    t.home()
    t.goto(new_x, new_y)
    t.down()
def main():
    x = -325.00
    y = 250.00
    space_between_letters = 40
    zeichen=None
    while True:
        print(menu())
        try:
            opt=int(input('Was möchten Sie zeichnen?:\n '))
            if opt==1:
                try:
                    t.up()
                    t.home()
                    t.down()
                    t.teleport(x,y)
                    wort= input('Wählen Sie ein Wort:\n ')
                    for litera in wort.upper():
                        instructiuni = letters.get(litera)
                        move_turtle(x, y)
                        x += space_between_letters
                        for actiune in instructiuni:
                                if actiune == 'save':
                                    x+=30
                                if actiune == 'speed':
                                    t.speed(50)
                                if actiune == 'pensize':
                                    t.pensize(5)
                                if actiune == 'left180':
                                    t.left(180)
                                if actiune == 'left170':
                                    t.left(170)
                                if actiune == 'left155':
                                    t.left(155)
                                if actiune == 'left150':
                                    t.left(150)
                                if actiune == 'left140':
                                    t.left(140)
                                if actiune == 'left117':
                                    t.left(117)
                                if actiune == 'left110':
                                    t.left(110)
                                if actiune == 'left100':
                                    t.left(100)
                                if actiune == 'left90':
                                    t.left(90)
                                if actiune == 'left80':
                                    t.left(80)
                                if actiune == 'left75':
                                    t.left(75)
                                if actiune == 'left70':
                                    t.left(70)
                                if actiune == 'left60':
                                    t.left(60)
                                if actiune == 'left50':
                                    t.left(50)
                                if actiune == 'left45':
                                    t.left(45)
                                if actiune == 'left30':
                                    t.left(30)
                                if actiune == 'left25':
                                    t.left(25)
                                if actiune == 'forward55':
                                    t.forward(55)
                                if actiune == 'forward50':
                                    t.forward(50)
                                if actiune == 'forward40':
                                    t.forward(40)
                                if actiune == 'forward45':
                                    t.forward(45)
                                if actiune == 'forward35':
                                    t.forward(35)
                                if actiune == 'forward30':
                                    t.forward(30)
                                if actiune == 'forward25':
                                    t.forward(25)
                                if actiune == 'forward22':
                                    t.forward(22)
                                if actiune == 'forward20':
                                    t.forward(20)
                                if actiune == 'forward15':
                                    t.forward(15)
                                if actiune == 'forward10':
                                    t.forward(10)
                                if actiune == 'forward5':
                                    t.forward(5)
                                if actiune == 'backward50':
                                    t.backward(50)
                                if actiune == 'backward45':
                                    t.backward(45)
                                if actiune == 'backward40':
                                    t.backward(40)
                                if actiune == 'backward35':
                                    t.backward(35)
                                if actiune == 'backward30':
                                    t.backward(30)
                                if actiune == 'backward25':
                                    t.backward(25)
                                if actiune == 'backward20':
                                    t.backward(20)
                                if actiune == 'backward22':
                                    t.backward(22)
                                if actiune == 'backward15':
                                    t.backward(15)
                                if actiune == 'backward10':
                                    t.backward(10)
                                if actiune == 'right180':
                                    t.right(180)
                                if actiune == 'right155':
                                    t.right(155)
                                if actiune == 'right150':
                                    t.right(150)
                                if actiune == 'right145':
                                    t.right(145)
                                if actiune == 'right140':
                                    t.right(140)
                                if actiune == 'right135':
                                    t.right(135)
                                if actiune == 'right120':
                                    t.right(120)
                                if actiune == 'right117':
                                    t.right(117)
                                if actiune == 'right110':
                                    t.right(110)
                                if actiune == 'right90':
                                    t.right(90)
                                if actiune == 'right80':
                                    t.right(80)
                                if actiune == 'right70':
                                    t.right(70)
                                if actiune == 'right60':
                                    t.right(60)
                                if actiune == 'right50':
                                    t.right(50)
                                if actiune == 'right45':
                                    t.right(45)
                                if actiune == 'right35':
                                    t.right(35)
                                if actiune == 'right30':
                                    t.right(30)
                                if actiune == 'right25':
                                    t.right(25)
                                if actiune == 'circle-15/200':
                                    t.circle(-15, 200)
                                if actiune == 'circle-15/250':
                                    t.circle(-15, 250)
                                if actiune == 'circle10/200':
                                    t.circle(10, 200)
                                if actiune == 'circle25/180':
                                    t.circle(25, 180)
                                if actiune == 'circle25/-180':
                                    t.circle(25, -180)
                                if actiune == 'circle15/-180':
                                    t.circle(15, -180)
                                if actiune == 'circle-15/-180':
                                    t.circle(-15, -180)
                                if actiune == 'circle15/170':
                                    t.circle(15, 170)
                                if actiune == 'circle15/-170':
                                    t.circle(15, -170)
                                if actiune == 'circle15/100':
                                    t.circle(15, 100)
                                if actiune == 'circle15/-100':
                                    t.circle(15, -100)
                                if actiune == 'circle-15/150':
                                    t.circle(-15, 150)
                                if actiune == 'circle15/-90':
                                    t.circle(15, -90)
                                if actiune == 'circle15/90':
                                    t.circle(15, 90)
                                if actiune == 'circle25':
                                    t.circle(25)
                                if actiune == 'up':
                                    t.up()
                                if actiune == 'down':
                                    t.down()
                                if actiune == 'home':
                                    t.home()
                                if actiune == '.':
                                    t.dot(7)
                                if actiune == 'space':
                                    t.forward(50)
                except ValueError:
                    print('Wählen Sie Litter:\n ')

            if opt==2:
                t.up()
                t.home()
                t.down()
                l=['speed','pensize']
                while True:
                    try:

                        key = input('Drücken Sie eine aus die folgende: W, S, A, D, F, G, Space:\n')
                        if key == 'w':
                            l.append('forward10')
                            vorwärts()
                        if key == 's':
                            l.append('backward10')
                            rückwärts()
                        if key == 'd':
                            l.append('right45')
                            rechts()
                        if key == 'a':
                            l.append('left45')
                            links()
                        if key == 'f':
                            l.append('up')
                            up()
                        if key == 'g':
                            l.append('down')
                            down()
                        if key == ' ':
                            print(l)
                            l_exists = False
                            for cheie in letters:
                                if l == letters[cheie]:
                                    print('Das Zeichen existiert schon\n')
                                    l_exists = True
                            if l_exists== False :
                                zeichen = input('Wie soll das Zeichen gennant werden?\n')
                                drawings[zeichen] = l
                                print(drawings)
                            with open('desen.txt', 'w') as file:
                                file.write(zeichen + '\n')
                                for actiune in l:
                                    file.write(actiune + '\n')
                            t.reset()
                            print('Das Zeiche wurde ins "desen.txt" gespeichert')
                            break


                    except KeyError:
                        print('')
                        print('Das gewählte Key existiert nicht: \n')

            if opt == 3:
                if zeichen is None:
                    print("Bitte wählen Sie zuerst Option 2, um ein Zeichen hinzuzufügen.")
                    continue
                else:
                    move_turtle(-250,-100)
                    reafist_text(zeichen)
                    instructiuni = letters.get(zeichen)
                    for actiune in instructiuni:
                        if actiune == 'speed':
                            t.speed(10)
                        if actiune == 'pensize':
                            t.pensize(5)
                        if actiune == 'forward10':
                            t.forward(10)
                        if actiune == 'backward10':
                            t.backward(10)
                        if actiune == 'right45':
                            t.right(45)
                        if actiune =='left45':
                            t.left(45)
                        if actiune =='up':
                            t.up()
                        if actiune =='down':
                            t.down()
                        if actiune == ' ':
                            break

            if opt==0:
                turtle.done()
                break

        except ValueError:
            print('')
            print('Bitte ein Zahl zwischen 0 und 2 eingeben: \n')
    turtle.done()