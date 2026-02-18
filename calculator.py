
def calculator():
    print("---Simple Python Calculator---")
    print("Operation: +,-,*,/ (Type 'exit' or 'quit')")
    
    while True:
        try:
            choice=input("\nEnter operation(+,-,*,/) or 'exit': ").strip()

            if choice.lower() in ["exit","quit"]:
                print("Goodbye!")
                break

            if choice not in['+','-','*','/']:
                print("Invalid operation!Please choose +,-,*,/")
                continue

            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))

            if choice == '+':
                result = num1 + num2
            elif choice == '-':
                result = num1 - num2
            elif choice == '*':
                result = num1 * num2
            elif choice == '/':
                if num2 == 0:
                    print("Error! Cannot divide by zero!")
                    continue
                result = num1 / num2
            

            print(f"Result: {num1} {choice} {num2} = {result}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    calculator()