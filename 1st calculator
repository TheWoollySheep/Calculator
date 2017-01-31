def add (var1, var2):
    return var1 + var2
    #Returns the sum of num1 and num2
    # *, -, /
def sub (var1, var2):
    return var1 - var2

def mul (var1, var2):
    return var1 * var2

def div (var1, var2):
    return var1 / var2

def main():
    operation = input ("Pick a operation (+,-,*,/)")
    if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
        print("You must enter a valid operation")
    else:
        var1 = int (input ("Enter number: "))
        var2 = int (input ("Enter number: "))
    if (operation == '+'):
            print(add(var1,var2))
    elif (operation == '-'):
            print(sub(var1,var2))
    elif (operation == '*'):
            print(mul(var1,var2))
    else:
        if (operation == '/'):
            print(div(var1,var2))
main()

def redo():
    again = input ("do you want to calculate another number? yes or no ")
    if (again != 'yes' and again != 'no'):
        return redo()
    if (again == 'yes'):
        print ("ENTER A VALID AWNSER")
        return main()
    elif (again == 'no'):
        print ("Goodbye")
redo()
