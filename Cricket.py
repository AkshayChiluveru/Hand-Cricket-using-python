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


def bat():
    print("You are going to bat first")
    print("Enter a number between 1 and 6: ")
    score = 0
    while True:
        user = int(input("Choose a number: "))
        if user == 0:
            print("Your score is ", score)
            break
        elif user <1 and user > 6:
            print("Invalid number")
            continue
        else:
            computer = random.randint(1,6)
            print("Computer chose", computer)
            if user == computer:
                print("You are out")
                print("Your score is", score)
                break
            else:
                score += user
                print("Your score is", score)

def bowl():
    print("You are bowling")
    print("Enter a number between 1 and 6")
    print("Enter 0 to quit")
    score = 0
    while True:
        computer = random.randint(1, 6)
        print("Computer chose", computer)
        user = int(input("Choose a number: "))
        if user == 0:
            print("Computer score is", score)
            break
        elif user < 1 or user > 6:
            print("Invalid input")
            continue
        else:
            if user == computer:
                print("Computer is out")
                print("Computer score is", score)
                break
            else:
                score += computer
                print("Computer score is", score)


if __name__ == "__main__":
    main()
