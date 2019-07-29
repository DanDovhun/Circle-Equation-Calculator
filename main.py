from functions import *

while True:
    print("\nGet an equation of a circe")
    print("Options: 1.) Using radius and centre")
    print("         2.) Using centre and a One point on circunference")
    print("         3.) Using two points on circunference")
    print("         4.) Using three points on circumference")

    choice = input("\nChoice: ")

    if choice == "1":
        while True:
            rad = float(input("\nRadius: "))
            print("Coordinates of the centre:")
            x = float(input("X: "))
            y = float(input("Y: "))

            try:
                if rad > 0:
                    radAndCent(rad,x,y)
                    break

                else:
                    print("Radius must be above 0")

            except ValueError:
                print("Only enter numbers")

    elif choice == "2":
        while True:
            print("\nCoordinates of the centre:")
            xC = float(input("X: "))
            yC = float(input("Y: "))

            print("\nPoint on a circumference:")
            xK = float(input("X: "))
            yK = float(input("Y: "))

            try:
                centAndCirc(xC,yC,xK,yK)
                break

            except ValueError:
                print("Please only enter numbers")

    elif choice == "3":
        while True:
            print("\nCoordinates of point A:")
            xA = float(input("X: "))
            yA = float(input("Y: "))

            print("\nCoordinates of point B:")
            xB = float(input("X: "))
            yB = float(input("Y: "))

            try:
                twoPoints(xA,yA,xB,yB)
                break

            except ValueError:
                print("Please only enter numbers")

    elif choice == "4":
        while True:
            print("\nCoordinates of point A:")
            xA = float(input("X: "))
            yA = float(input("Y: "))

            print("\nCoordinates of point B:")
            xB = float(input("X: "))
            yB = float(input("Y: "))

            print("\nCoordinates of point C:")
            xC = float(input("X: "))
            yC = float(input("Y: "))

            try:
                threePoints(xA,yA,xB,yB,xC,yC)
                break

            except ValueError:
                print("Please only enter numbers")

    elif choice == "quit" or choice == "Quit":
        break

    else:
        print("Please only enter numbers")