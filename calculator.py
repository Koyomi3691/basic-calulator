def add(a, b):
    answer = a + b 
    print(str(a) + " + " + str(b) + " = " + str(answer))

def subtract(a,b):
    answer = a - b 
    print(str(a) + " - " + str(b) + " = " + str(answer))

def multiply(a,b):
    answer = a * b 
    print(str(a) + " * " + str(b) + " = " + str(answer))

def divide(a,b):
    answer = a / b 
    print(str(a) + " / " + str(b) + " = " + str(answer))

def module(a,b):
    answer = a % b 
    print(str(a) + " % " + str(b)+ " = " + str(answer))

def power(a,b):
    answer = a ** b 
    print(str(a) + " ** " + str(b) + " = " + str(answer))

def equal(a,b):
    answer = a == b 
    print(str(a) + " == " + str(b) + " = " + str(answer))

def notequal(a,b):
    answer = a!= b 
    print(str(a) + "!= " + str(b) + " = " + str(answer))
    
def greater(a,b):
    answer = a > b
    print(str(a) + " > " + str(b) + " = " + str(answer))
    
def less(a,b):
    answer = a < b
    print(str(a) + " < " + str(b) + " = " +str(answer))
    
def greaterequal(a,b):
    answer = a >= b
    print(str(a) + " >= " + str(b) + " = " +str(answer))
    
def lesserequal(a,b):
    answer = a <= b
    print(str(a) + " <= " + str(b) + " = " +str(answer))

def notgreaterequal(a,b):
    answer = a!= b
    print(str(a) + "!= " +str(b) + " = " +str(answer))

def notless(a,b):
    answer = a < b
    print(str(a) + " < " + str(b) + " = " +str(answer))

def notlesserequal(a,b):
    answer = a <= b
    print(str(a) + " <= " + str(b) + " = " +str(answer))

def notgreater(a,b):
    answer = a > b
    print(str(a) + " > " + str(b)+ " = " +str(answer))

def notgreatererequal(a,b):
    answer = a >= b
    print(str(a) + " >= " + str(b) + " = " +str(answer))

while True:
    print("A. addition")
    print("B. Subtraction")
    print("C. Multiply")
    print("D. Divide")
    print("E. Module")
    print("F. Power")
    print("G. Equal")
    print("H. NotEqual")
    print("I. Greater")
    print("J. Less")
    print("K. GreaterEqual")
    print("L. LesserEqual")
    print("M. NotGreaterEqual")
    print("N. NotLess")
    print("O. NotLesserEqual")
    print("P. NotGreater")
    print("Q. NotGreaterEqual")
    print("R. Exit")

    choice=input("Input your choice: ")

    if choice == "a" or choice =="A":
     print("Addition")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     add(a,b)

    elif choice == "b" or choice =="B":
     print("Subtraction")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     subtract(a,b)

    elif choice == "c" or choice =="C":
     print("Multiply")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     multiply(a,b)

    elif choice == "d" or choice =="D":
     print("Divide")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     divide(a,b)

    elif choice == "e" or choice =="E":
     print("Module")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     module(a,b)

    elif choice == "f" or choice =="F":
     print("Power")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     power(a,b)

    elif choice == "g" or choice =="G":
     print("Equal")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     equal(a,b)

    elif choice == "h" or choice =="H":
     print("Greater")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     greater(a,b)

    elif choice == "i" or choice =="I":
     print("GreaterEqual")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     greaterequal(a,b)

    elif choice == "j" or choice =="J":
     print("Less")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     less(a,b)

    elif choice == "k" or choice =="K":
     print("GreaterEqual")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     greaterequal(a,b)

    elif choice == "l" or choice =="L":
     print("LesserEqual")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     less(a,b)

    elif choice == "m" or choice =="M":
     print("NotGreaterEqual")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     greaterequal(a,b)

    elif choice == "n" or choice =="N":
     print("NotLess")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     notless(a,b)

    elif choice == "o" or choice =="O":
     print("NotLesserEqual")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     notlesserequal(a,b)

    elif choice == "p" or choice =="P":
     print("NotGreater")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     notgreater(a,b)

    elif choice == "q" or choice =="Q":
     print("NotGreaterEqual")
     a=int(input("Enter your first number: "))
     b=int(input("Enter your second number: "))
     notgreaterequal(a,b)

    elif choice == "r" or choice =="R":
     print("Program Ended")
     quit()





