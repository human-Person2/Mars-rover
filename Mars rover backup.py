#sets original bearing
bearing="N"
#sets minimum value for the x and y co-ordinates
minx=0
miny=0
#sets a default value for r1x,r1y,r1bearing and r2x,r2y,r2bearing
r1x=0
r1y=0
r1bearing="N"
r2x=1
r2y=0
r2bearing="N"
#sets a defualt for the maxium x and y value
maxx=3
maxy=3
#sests a value that will start the loop
loop="y"
#input for max co-ordinate of the plateau
try:
    maxx=int(input("What is the x co-ordinate of the upper-right corner of the plateau (must be greater than 0): "))
    maxy=int(input("What is the y co-ordinate of the upper-right corner of the plateau (must be greater than 0): "))
except ValueError:
    print("INVALID ENTRY")
    exit()
#checks to see if the plateu is greater than 0
if (maxx or maxy)<=0:
    print("Incorrect size")
    exit()
else:
    try:
        r1x=int(input("What is the starting x co-ordinate for Rover 1: "))
        r1y=int(input("What is the starting y co-ordinate for Rover 1: "))
        r1bearing=input("What would you like the starting bearing to be (N/E/S/W): ")
        r1move=input("The way to move the rover is by combing L (left 90 degrees), R (Right 90 degrees) and M (move forward one in the direction the rover is facing), an example movement is MLMRRMMR\nHow would you like to move the rover: ")
        if r1x>maxx or r1y>maxy:
            print("Must be within the palateu")
            exit()
        else:
            for i in r1move:
                #this will change the bearing of the rover left by 90 degrees
                if i.lower()=="l":
                    if r1bearing.lower()=="n":
                        r1bearing="W"
                    elif r1bearing.lower()=="w":
                        r1bearing="S"
                    elif r1bearing.lower()=="s":
                        r1bearing="E"
                    elif r1bearing.lower()=="e":
                        r1bearing="N"
                    else:
                        print("INVALID")
                        exit()
                elif i.lower()=="r":
                    #this will change the bearing of the rover right by 90 degrees
                    if r1bearing.lower()=="n":
                        r1bearing="E"
                    elif r1bearing.lower()=="e":
                        r1bearing="S"
                    elif r1bearing.lower()=="s":
                        r1bearing="W"
                    elif r1bearing.lower()=="w":
                        r1bearing="N"
                    else:
                        print("INVALID")
                        exit()
                elif i.lower()=="m":
                    #this will move the rover forward one in either the x or y corodinate unless it exceedes the maximum value for x or y or if it goes below 0
                    if r1bearing.lower()=="n" and r1y<maxy:
                        r1y=r1y+1
                    elif r1bearing.lower()=="s" and r1y>0:
                        r1y=r1y-1
                    elif r1bearing.lower()=="e" and r1x<maxx:
                        r1x=r1x+1
                    elif r1bearing.lower()=="w" and r1x>0:
                        r1x=r1x-1
                    else:
                        print("INVALID")
                        exit()
                else:
                    print("INVAILD MOVEMENT")
                    exit()
    except ValueError:
        print("INVALID ENTRY")
        exit()
    try:
        r2x=int(input("What is the starting x co-ordinate for Rover 2: "))
        r2y=int(input("What is the starting y co-ordinate for Rover 2: "))
        r2bearing=input("What would you like the starting bearing to be (N/E/S/W): ")
        r2move=input("The way to move the rover is by combing L (left 90 degrees), R (Right 90 degrees) and M (move forward one in the direction the rover is facing), an example movement is MLMRRMMR\nHow would you like to move the rover: ")
        if r2x>maxx or r2y>maxy:
            print("Must be within the palateu")
            exit()
        else:
            for i in r2move:
                #this will change the bearing of the rover left by 90 degrees
                if i.lower()=="l":
                    if r2bearing.lower()=="n":
                        r2bearing="W"
                    elif r2bearing.lower()=="w":
                        r2bearing="S"
                    elif r2bearing.lower()=="s":
                        r2bearing="E"
                    elif r2bearing.lower()=="e":
                        r2bearing="N"
                    else:
                        print("INVALID")
                        exit()
                elif i.lower()=="r":
                    #this will change the bearing of the rover right by 90 degrees
                    if r2bearing.lower()=="n":
                        r2bearing="E"
                    elif r2bearing.lower()=="e":
                        r2bearing="S"
                    elif r2bearing.lower()=="s":
                        r2bearing="W"
                    elif r2bearing.lower()=="w":
                        r2bearing="N"
                    else:
                        print("INVALID")
                        exit()
                elif i.lower()=="m":
                    #this will move the rover forward one in either the x or y corodinate unless it exceedes the maximum value for x or y or if it goes below 0
                    if r2bearing.lower()=="n" and r2y<maxy:
                        r2y=r2y+1
                    elif r2bearing.lower()=="s" and r2y>0:
                        r2y=r2y-1
                    elif r2bearing.lower()=="e" and r2x<maxx:
                        r2x=r2x+1
                    elif r2bearing.lower()=="w" and r2x>0:
                        r2x=r2x-1
                    else:
                        print("INVALID")
                        exit()
                else:
                    print("INVAILD MOVEMENT")
                    exit()
    except ValueError:
        print("INVALID ENTRY")
        exit()
#prints the final result
print("("+str(r1x)+","+str(r1y)+") "+r1bearing)
print("("+str(r2x)+","+str(r2y)+") "+r2bearing)
