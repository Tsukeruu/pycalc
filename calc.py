try:
    ########################################
    #//IDENTIFYING VARS AND LIBRARIES\\#
    
    import math
    import os
    from time import sleep
    import platform

    while True:
        lib__ = input('WOULD YOU LIKE TO INSTALL NUMPY/PYSTYLE (Y/N): ')

        if lib__.lower() == "y":
            os.system("pip install numpy")
            os.system("pip install pystyle")
            if platform.system() == "Linux":
                os.system('clear')
            elif platform.system() == "Windows":
                os.system('cls')
            break
        elif lib__.lower() == "n":
            if platform.system() == "Linux":
                os.system('clear')
            elif platform.system() == "Windows":
                os.system('cls')
            break
        else:
            print('INVALID CHOICE!')

    import numpy
    import pystyle
    pystyle.System.Title("PYCALC")


    inputch = None
    firstnum = None
    currop = None
    Secondnum = None
    firstcdparam = int((360 / 360) + (numpy.round(numpy.pi) + 1))
    secondcdparam = int((360 / 360) - 1 + math.sin(0))
    thirdcdparam = int(((360 / 360 + 1) / 2) - 2)

    OPERATIONS = [
    "/",
    "*",
    "+",
    "-",
    "**",
    "*/",
    "sin",
    "cos",
    "tan",
    "acos",
    "atan",
    "asin"
    ]

    ########################################


    def countdown(starttime:float,endtime:float,step:float):
        for __Z in range(starttime,endtime,step):
            print(f'CLEARING SCREEN IN: {__Z}',end='\r')
            sleep(1)


    def introduc():
        print("=" * int((-1 * -50 - (math.sin(0) or numpy.sin(0)))))

        introduc = '''
        WELCOME TO THE CALCULATOR!
        / IS A SIGN OF DIVISION, PARAMS=(FIRSTNUM, SECNODNUM)
        * IS A SIGN OF MULTIPLICATION, PARAMS=(FIRSTNUM, SECONDNUM)
        + IS A SIGN OF ADDITION, PARAMS=(FIRSTNUM, SECONDNUM)
        - IS A SIGN OF SUBTRACTION, PARAMS=(FIRSTNUM (LARGER), SECONDNUM(SMALLER))
        ** IS A SIGN OF POWER OF, PARAMS=(BASE,EXPONENT)
        */ IS A SIGN OF SQUAREROOT, PARAMS=(NUMBER)
        --------------ADVANCED TRIGINOMETRIC FUNCTIONS--------------

        ASIN IS BETWEEN -1, 1
        ACOS IS BETWEEN -1, 1

        sin (IS THE SIN TRIGINOMETRIC FUNCTION, PARAMS=(NUMBER))
        cos (IS THE COS TRIGINOMETRIC FUNCTION, PARAMS=(NUMBER))
        tan (IS THE TAN TRIGINOMETRIC FUNCTION, PARAMS=(NUMBER))

        ASIN (IS THE SIN INVERSE TRIGINOMETRIC FUNCTION, PARAMS=(NUMBER)) 
        ACOS (IS THE COS INVERSE TRIGINOMETRIC FUNCTION, PARAMS=(NUMBER))
        ATAN (IS THE TAN INVERSE TRIGINOMETRIC FUNCTION, PARAMS=(NUMBER))

        '''
        print(introduc)

        print("=" * int((-1 * -50 - (math.sin(0) or numpy.sin(0)))))



    introduc()
    
    

    while True:
        inputch = str(input("ENTER OPERATION: "))
        if inputch == "/" and inputch in OPERATIONS:
            currop = "DIVISION"
            print(f"CURRENT OPERATION: {currop}")
            firstnum = float(input("ENTER FIRST NUMBER: "))
            Secondnum = float(input("ENTER SECOND NUMBER: "))
            print((lambda firstnum, Secondnum: numpy.divide(firstnum,Secondnum))(firstnum,Secondnum))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()
        elif inputch == "*" and inputch in OPERATIONS:
            currop = "Multiplication"
            print(f"CURRENT OPERATION: {currop}")
            firstnum = float(input("ENTER FIRST NUMBER: "))
            Secondnum = float(input("ENTER SECOND NUMBER: "))
            print((lambda firstnum, Secondnum: numpy.multiply(firstnum,Secondnum))(firstnum,Secondnum))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()
        elif inputch == "**" and inputch in OPERATIONS:
            currop = "POWER"
            print(f"CURRENT OPERATION: {currop}")
            firstnum = float(input("ENTER FIRST NUMBER: "))
            Secondnum = float(input("ENTER SECOND NUMBER: "))
            print((lambda firstnum, Secondnum: math.pow(firstnum,Secondnum))(firstnum,Secondnum))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()
        elif inputch == "+" and inputch in OPERATIONS:
            currop = "ADDITION"
            print(f"CURRENT OPERATION: {currop}")
            firstnum = float(input("ENTER FIRST NUMBER: "))
            Secondnum = float(input("ENTER SECOND NUMBER: "))
            print((lambda firstnum, Secondnum: numpy.add(firstnum,Secondnum))(firstnum,Secondnum))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()
        elif inputch == "-" and inputch in OPERATIONS:
            currop = "SUBTRACTION"
            print(f"CURRENT OPERATION: {currop}")
            firstnum = float(input("ENTER FIRST NUMBER: "))
            Secondnum = float(input("ENTER SECOND NUMBER: "))
            print((lambda firstnum, Secondnum: numpy.subtract(firstnum,Secondnum))(firstnum,Secondnum))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()
        elif inputch == "*/" and inputch in OPERATIONS:
            currop = "SQRT"
            print(f"CURRENT OPERATION: {currop}")
            num = float(input("ENTER FIRST NUMBER: "))
            print((lambda num: math.sqrt(num))(num))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()
        elif inputch.lower() == "sin" and inputch.lower() in OPERATIONS:
            currop = "SIN"
            print(f"[+] CURRENT OPERATION: {currop}")
            num = float(input("ENTER FIRST NUMBER: "))
            print((lambda num: math.sin(num) or numpy.sin(num))(num))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()
        elif inputch.lower() == "cos" and inputch.lower() in OPERATIONS:
            currop = "COS"
            print(f"[+] CURRENT OPERATION: {currop}")
            num = float(input("ENTER FIRST NUMBER: "))
            print((lambda num: math.cos(num) or numpy.cos(num))(num))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()
        elif inputch.lower() == "tan" and inputch.lower() in OPERATIONS:
            currop = "TAN"
            print(f"[+] CURRENT OPERATION: {currop}")
            num = float(input("ENTER FIRST NUMBER: "))
            print((lambda num: math.tan(num) or numpy.tan(num))(num))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()


        elif inputch.lower() == "asin" and inputch.lower() in OPERATIONS:
            currop = "ASIN"
            print(f"[+] CURRENT OPERATION: {currop}")
            num = float(input("ENTER FIRST NUMBER: "))
            print((lambda num: math.asin(num) or numpy.asin(num))(num))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()
        elif inputch.lower() == "acos" and inputch.lower() in OPERATIONS:
            currop = "ACOS"
            print(f"[+] CURRENT OPERATION: {currop}")
            num = float(input("ENTER FIRST NUMBER: "))
            print((lambda num: math.acos(num) or numpy.acos(num))(num))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()
        elif inputch.lower() == "atan" and inputch.lower() in OPERATIONS:
            currop = "ATAN"
            print(f"[+] CURRENT OPERATION: {currop}")
            num = float(input("ENTER FIRST NUMBER: "))
            print((lambda num: math.atan(num) or numpy.atan(num))(num))
            currop = None #REMEMBER TO RESET TO NIL!
            inputch = None #REMEMBER TO RESET TO NIL!
            if platform.system() == "Linux":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('clear')
                introduc()
            elif platform.system() == "Windows":
                countdown(firstcdparam or int((360 / 360) + (numpy.round(numpy.pi) + 1)),secondcdparam or int((360 / 360) - 1 + math.sin(0)),thirdcdparam or int(((360 / 360 + 1) / 2) - 2))
                os.system('cls')
                introduc()
        else:
            print('UNKOWN CHOICE OR OPERATION IS NOT LISTED.. YET')
except ValueError as e:
    print(f'bru you prolly tried to multiply a string and a float shame on you, error: {e}')





#----creator notes----#
#im going to add more stuff in the future
#this is just my 3rd or 4th python program!








