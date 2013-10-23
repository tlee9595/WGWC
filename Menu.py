#Thomas Lee
#tlee319@gatech.edu
#I worked on the homework assignment alone, using on this semester's course mateials"

from Myro import*

def menu():
    exit = False
    while exit == False:
        choice = input("1.Twerk \n2.Scaptical turning \n3.Up and Down \n4.Harry Potter \n0. Exit \nWhich dance step/song would you like?")

        choice = int(choice)

        if choice == 1:
            x = 0
            while x <= 10:
                rotate(1,0.01)
                rotate(-1,0.01)
                x = x+1
        elif choice == 2:
            x = 0
            while x <= 4:
                rotate(1,0.2)
                rotate(-1,0.2)
                rotate(1,0.3)
                rotate(-1,0.2)
                x = x +1
        elif choice == 3:
            x=0
            i = 0
            while x <= 8:
                beep(0.2,70*x + 500)
                x = x+1
            while x > 0:
                beep(0.1, 1060 - 70*i)
                i = i + 1
                x = x - 1
        elif choice == 4:
            tone2()
            tone2()
            tone3()
            tone4()
            wait(1.7)
            tone2()
            tone2()
            tone5()
            tone6()
        elif choice == 0:
            print("Have a good day!")
            exit = True
        else:
            print ("I'm sorry, I don't know that one.")




def danceSing():
    for seconds in timer(20):
        x = 0
        while x <= 6:
            beepbeep()
            x = x+1
        stop()
        wait(2)
        forward(0.3,1)
        backward(0.7,0.6)
        forward(0.7,0.4)
        wiggleWiggle()
        forward(1,1)
        slowDown()
        beepbeep()
        wiggleWiggle()
    tone1()
    tone2()
    tone2()
    tone3()
    tone4()
    wait(1.7)
    tone2()
    tone2()
    tone5()
    tone6()



def tone1():
    x=0
    i = 0
    while x <= 8:
        beep(0.2,70*x + 500)
        x = x+1
    while x > 0:
        beep(0.1, 1060 - 70*i)
        i = i + 1
        x = x - 1
def tone2():
    beep(0.4, 800)
    beep(1, 1000)

def tone3():
    beep(0.4, 800)
    beep(.8, 1050)
    beep(0.15, 1000)
    beep(0.2, 940)
    beep(1, 900)

def tone4():
    beep(0.4, 750)
    beep(0.7, 800)
    beep(0.18, 960)
    beep(0.2, 850)
    beep(0.7, 610)
    beep(0.4, 700)
    beep(1, 900)

def tone5():
    beep(0.4, 800)
    beep(0.8, 1190)
    beep(0.4, 1100)
    beep(0.8, 1050)

def tone6():
    beep(0.4, 880)
    beep(0.7, 1050)
    beep(0.12, 980)
    beep(0.2, 940)
    beep(0.7, 610)
    beep(0.4, 800)
    beep(1, 650)

def beepbeep():
    rotate(1,0.2)
    rotate(-1,0.2)
    rotate(1,0.3)
    rotate(-1,0.2)

def wiggleWiggle():
    x = 0
    while x <= 10:
        rotate(1,0.01)
        rotate(-1,0.01)
        x = x+1
def slowDown():
    x = 0
    while x<=1:
        motors(1,0.5)
        wait(1)
        stop()
        motors(-1,0.5)
        wait(1)
        stop()
        x = x + 1