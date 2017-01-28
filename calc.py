def add(var1, var2):
    return var1 + var2

def sub(var1, var2):
    return var1 - var2

def mul(var1, var2):
    return var1 * var2

def div(var1, var2):
    return var1 / var2

lookup_table = {'-': sub, '+': add, '*': mul, '/': div}

def start():
    operation = input ("Pick your operation *,/,-,+ ")
    if operation not in ['+','-','/','*']:
        print("your must enter a valid operation")
        return start()
    else:
        try:
            var1 = int(input("Enter Number: "))
            var2 = int(input("Enter Number: "))
        except ValueError:
            print("That's not a number")
            return start()
        print(lookup_table[operation](var1, var2))
    again()
def again():
    redo = input("do you want to calculate a new number? yes or no ")

    if (redo == 'yes'):
        return start()

    if (redo == 'no'):
        print("Goodbye")

    if redo not in ['yes','no']:
        print("NOT A VALID AWNSER")
        return again()

if __name__ == '__main__':
    start()
