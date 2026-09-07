while True:
    print("\n--- CALCULATOR---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Remainder (%)")
    print("6. Exit")
    c = input("Enter operation (1-5 or +, -, *, /, %) or 'exit': ").strip()
    if c.lower() == "exit":
        print("Calculator closed. Goodbye!")
        break

    operations = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "%"}
    c = operations.get(c, c)

    a = int(input("enter your first no. = "))

    b = int(input("enter your second no. ="))


    if c == "+":
        print(a + b)

    elif c == "-":
        print(a - b)

    elif c == "*":
        print(a * b)

    elif c == "/":
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(a / b)

    elif c == "%":
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(a % b)

    else:
        print("invalid input")