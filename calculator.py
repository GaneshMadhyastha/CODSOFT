
def calculator():
    #functon to perform basic arithemetic operations based on user input
    print("\n" + "-" * 40)
    print("====== Simple Python Calculator ======".center(40))
    print("\n" + "-" * 40)
    print("Operation: +,-,*,/ (Type 'exit' or 'quit')")
    
    while True:
        try:
            #capture user choice for the operation
            choice=input("\nEnter operation(+,-,*,/) or 'exit': ").strip()
            print("\n" + "-" * 35)
            #Check if user wants to exit/quit from the program
            if choice.lower() in ["exit","quit"]:
                print("Goodbye!")
                break
            #showcases that the choices should be one of the four supported operators
            if choice not in['+','-','*','/']:
                print("Invalid operation!Please choose +,-,*,/")
                continue
            #Validates numerical inputs
            num1=float(input("Enter first number: "))
            print("\n" + "-" * 20)
            num2=float(input("Enter second number: "))

            if choice == '+':
                result = num1 + num2
            elif choice == '-':
                result = num1 - num2
            elif choice == '*':
                result = num1 * num2
            elif choice == '/':
                #Handle edge cases:Zero division error
                if num2 == 0:
                    print("\n" + "-" * 35)
                    print("Error! Cannot divide by zero!")
                    continue
                result = num1 / num2
            
            #Display formated result to user
            print("\n" + "-" * 35)
            print(f"Result: {num1} {choice} {num2} = {result}".center(40))
            print("\n" + "-" * 35)

        except ValueError:
            #Handle things where user input is invalid(example,typing 'abc')
            print("Invalid input! Please enter numeric values.")
#Entry point of script
if __name__ == "__main__":
    calculator()
