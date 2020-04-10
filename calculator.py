try:    
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    op = (input("Enter an operation: "))



    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("Error") 

except ValueError:

    print("Invalid Input")    

           