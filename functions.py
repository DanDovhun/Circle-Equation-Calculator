from numpy import pi, sqrt

def makeEquation(rad,x,y):
    if x == 0 and y != 0:
        if y > 0:
            print("Equation: (x)^2 + (y - " + str(round(y,5)) + ")^2 = " + str(round(rad**2,5)))

        if y < 0:
            print("Equation: (x)^2 + (y + " + str(round(y * -1,5)) + ")^2 = " + str(round(rad**2,5)))

    elif x != 0 and y == 0:
        if x > 0:
            print("Equation: (x - " + str(round(x,5)) + ")^2 + (y)^2 = " + str(round(rad**2,5)))

        if x < 0:
            print("Equation: (x + " + str(round(x * -1,5)) + ")^2 + (y)^2 = " + str(round(rad**2,5)))

    elif x == 0 and y == 0:
        print("Equation: x^2 + y^2 = " + str(round(rad**2,5)))

    else:
        if x > 0 and y > 0:
            print("Equation: (x - " + str(round(x,5)) + ")^2 + (y - " + str(round(y,5)) + ")^2 = " + str(round(rad**2,5)))

        elif x > 0 and y < 0:
            print("Equation: (x - " + str(round(x,5)) + ")^2 + (y + " + str(round(y * -1,5)) + ")^2 = " + str(round(rad**2,5)))

        elif x < 0 and y > 0:
            print("Equation: (x + " + str(round(x * -1,5)) + ")^2 + (y - " + str(round(y,5)) + ")^2 = " + str(round(rad**2,5)))

        else:
            print("Equation: (x + " + str(round(x * -1,5)) + ")^2 + (y + " + str(round(y * -1,5)) + ")^2 = " + str(round(rad**2,5)))


def circleParameters(rad,x,y):
    print("Parameters of the circle:")
    print("Radius: " + str(round(rad,5)) + " units")
    print("Centre: (" + str(round(x,5)) + ", " + str(round(y,5)) + ")")
    print("Area: " + str(round(pi * (rad**2), 5)) + " units^2")
    print("Circumference: " + str(round(2 * pi * rad,5)) + " units")


def radAndCent(rad, x, y):
    print("\n* Decimal values are all rounded to the 5th decimal value:\n")
    circleParameters(rad,x,y)

    makeEquation(rad,x,y)


def centAndCirc(xC,yC,xK,yK):
    rad = sqrt(((xC - xK) * (xC - xK)) + ((yC - yK) * (yC - yK)))
    print("\n* Decimal values are all rounded to the 5th decimal value\n")
    print("Entered points on the circumference:\nA(" + str(round(xK, 5)) + ", " + str(round(yK,5)) + ")\n")

    circleParameters(rad,xC,yC)
    makeEquation(rad,xC,yC)


def twoPoints(xA,yA,xB,yB):
    x = (xA + xB) / 2
    y = (yA + yB) / 2

    rad = sqrt(((x - xA) * (x - xA)) + ((y - yA) * (y - yA)))

    print("\n* Decimal values are all rounded to the 5th decimal value\n")
    print("Entered points on the circumference:")
    print("A(" + str(round(xA,5)) + ", " + str(round(yA,5)) + ")")
    print("B(" + str(round(xB,5)) + ", " + str(round(yB,5)) + ")\n")

    circleParameters(rad,x,y)
    makeEquation(rad, x, y)


def threePoints(xA,yA,xB,yB,xC,yC):
    mAB = (yB - yA) / (xB - xA)
    mAC = (yC - yA) / (xC - xA)

    dX = (xA + xB) / 2
    dY = (yA + yB) / 2

    eX = (xA + xC) / 2
    eY = (yA + yC) / 2

    mDO = -1 / mAB
    mEO = -1 / mAC

    aOne = mDO 
    bOne = dY - (mDO * dX)

    aTwo = mEO 
    bTwo = eY - (mEO * eX)

    a = bTwo - bOne
    b = aTwo - aOne

    x = a / b * -1
    y = mDO * x + bOne

    rad = sqrt(((x - xA) * (x - xA)) + ((y - yA) * (y - yA)))

    print("\n* Decimal values are all rounded to the 5th decimal value\n")
    print("Entered points on the circumference:")
    print("A(" + str(round(xA,5)) + ", " + str(round(yA,5)) + ")")
    print("B(" + str(round(xB,5)) + ", " + str(round(yB,5)) + ")")
    print("C(" + str(round(xC,5)) + ", " + str(round(yC,5)) + ")\n")

    circleParameters(rad,x,y)
    makeEquation(rad,x,y)