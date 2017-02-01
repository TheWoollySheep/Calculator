def HelloWorld (myString):
    print (myString)
    myName = input ("what is your name?")
    myVar = input ("Enter a Number")

    if(myName == "Kayode" and myVar == "0"):
        print("Kayode is great")
    elif(myName == "Bob"):
        print("Bob you are ok")
    else:
        print("Hello world")

HelloWorld("Hello function world")
HelloWorld("Hello 123 world")
