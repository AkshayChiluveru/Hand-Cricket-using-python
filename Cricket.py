import random

def main():
    print("Welcome to Hand Cricket")
    print("You will be playing against the computer")
    # print("You will be batting first")
    print("Enter 1 to bat,2 to bowl")
    choice =int(input("Choose a number: "))
    if choice == 1:
        bat()
    
    elif choice == 2:
        bowl()

    else:
        print("Invalid choice")
        main()
        