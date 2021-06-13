print("You want Arithemetic calculation and L.C.M on press : [1]")
print("You want  Multiplication  Tables  on  press         : [2]")
user=int(input("enter the number :"))
if user==1:
    ram = int(input("How many numbers are calculate (only choose :2,3,4) :"))

    if ram == 2:
        def addition(x, y):
            return x + y

        def subraction(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def dividion(x, y):
            return x / y

        def lcm_code(x, y):
            if x > y:
                greater = x
            else:
                greater = y
            while (True):
                if (greater % x == 0) and (greater % y == 0):
                    lcm = greater
                    break
                greater += 1
            return lcm


        # print("do you select the option :\n","1. addition\n","2. subraction\n","3. multiply\n","4. dividion\n")
        print("note this :")
        print("YOU WANT  ADDICTION  is PRESS  :[1]")
        print("YOU WANT  SUBRACTION is PRESS  :[2]")
        print("YOU WANT  MULTIPLY   is PRESS  :[3]")
        print("YOU WANT  DIVIDION   is PRESS  :[4]")
        print("YOU WANT  L.C.M      is press  :[5]")
        print("...................................")
        select = int(input("choose the option :"))

        if select == 1:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            print(num1, "+", num2, "=", addition(num1, num2))
        elif select == 2:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            print(num1, "-", num2, "=", subraction(num1, num2))
        elif select == 3:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif select == 4:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            print(num1, "/", num2, "=", dividion(num1, num2))
        elif select == 5:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            print(num1, "and", num2, "L.C.M is", lcm_code(num1, num2))
        else:
            print("INVALID INPUT")
    elif ram == 3:
        def addition(x, y, z):
            return x + y + z


        def subraction(x, y, z):
            return x - y - z


        def multiply(x, y, z):
            return x * y * z


        def dividion(x, y, z):
            c = x / y
            return c / z


        def lcm_code(x, y, z):
            if x > y:
                greater = x
            elif y > z:
                greater = y
            else:
                greater = z

            while (True):
                if (greater % x == 0) and (greater % y == 0) and (greater % z == 0):
                    lcm = greater
                    break
                greater += 1
            return lcm


        # print("do you select the option :\n","1. addition\n","2. subraction\n","3. multiply\n","4. dividion\n")
        print("note this :")
        print("YOU WANT  ADDICTION  is PRESS  :[1]")
        print("YOU WANT  SUBRACTION is PRESS  :[2]")
        print("YOU WANT  MULTIPLY   is PRESS  :[3]")
        print("YOU WANT  DIVIDION   is PRESS  :[4]")
        print("YOU WANT  L.C.M      is press  :[5]")
        print("...................................")
        select = int(input("choose the option :"))

        if select == 1:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            num3 = float(input("enter the 3rd value :"))
            print(num1, "+", num2, "+", num3, "=", addition(num1, num2, num3))
        elif select == 2:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            num3 = float(input("enter the 3rd value :"))
            print(num1, "-", num2, "_", num3, "=", subraction(num1, num2, num3))
        elif select == 3:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            num3 = float(input("enter the 3rd value :"))
            print(num1, "*", num2, "*", num3, "=", multiply(num1, num2, num3))
        elif select == 4:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            num3 = float(input("enter the 3rd value :"))
            print(num1, "/", num2, "/", num3, "=", dividion(num1, num2, num3))
        elif select == 5:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            num3 = float(input("enter the 3rd value :"))
            print(num1, "and", num2, "and", num3, " is L.C.M of", lcm_code(num1, num2, num3))
        else:
            print("INVALID INPUT")

    elif ram == 4:
        def addition(x, y, z, m):
            return x + y + z + m


        def subraction(x, y, z, m):
            return x - y - z - m


        def multiply(x, y, z, m):
            return x * y * z * m


        def dividion(x, y, z, m):
            c = x / y / z
            return c / m


        def lcm_code(x, y, z, m):
            if x > y:
                greater = x
            elif y > z:
                greater = y
            elif z > m:
                greater = z
            else:
                greater = m

            while (True):
                if (greater % x == 0) and (greater % y == 0) and (greater % z == 0) and (greater % m == 0):
                    lcm = greater
                    break
                greater += 1
            return lcm


        # print("do you select the option :\n","1. addition\n","2. subraction\n","3. multiply\n","4. dividion\n")
        print("note this :")
        print("YOU WANT  ADDICTION  is PRESS  :[1]")
        print("YOU WANT  SUBRACTION is PRESS  :[2]")
        print("YOU WANT  MULTIPLY   is PRESS  :[3]")
        print("YOU WANT  DIVIDION   is PRESS  :[4]")
        print("YOU WANT  L.C.M      is press  :[5]")
        print("...................................")
        select = int(input("choose the option :"))

        if select == 1:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            num3 = float(input("enter the 3rd value :"))
            num4 = float(input("enter the 4th value :"))
            print(num1, "+", num2, "+", num3, "+", num4, "=", addition(num1, num2, num3, num4))
        elif select == 2:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            num3 = float(input("enter the 3rd value :"))
            num4 = float(input("enter the 4th value :"))
            print(num1, "-", num2, "_", num3, "-", num4, "=", subraction(num1, num2, num3, num4))
        elif select == 3:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            num3 = float(input("enter the 3rd value :"))
            num4 = float(input("enter the 4th value :"))
            print(num1, "*", num2, "*", num3, "*", num4, "=", multiply(num1, num2, num3, num4))
        elif select == 4:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            num3 = float(input("enter the 3rd value :"))
            num4 = float(input("enter the 4th value :"))
            print(num1, "/", num2, "/", num3, "/", num4, "=", dividion(num1, num2, num3, num4))
        elif select == 5:
            num1 = float(input("enter the 1st value :"))
            num2 = float(input("enter the 2nd value :"))
            num3 = float(input("enter the 3rd value :"))
            num4 = float(input("enter the 4th value :"))
            print(num1, "and", num2, "and", num3, "and", num4, " is L.C.M of", lcm_code(num1, num2, num3, num4))
        else:
            print("INVALID INPUT")
    else:
        print("ONLY [2],[3],[4] NUMBERS IS SUPPORT IN THIS CALCULATER , OTHER VALUES ARE NOT VALID")

elif user==2:
    num = int(input("which tables are you want :"))
    for i in range(1,13):
        print(num, "x", i, "=", num * i)

else:
    print("THE NUMBER IS INVALID ")




