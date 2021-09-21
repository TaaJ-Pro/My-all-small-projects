print("Hi, Wellcome to the Calculator -_-")
sum = 0

while True:
    while True:
        UserInput = input('Enter a Number: ')
        if UserInput.isnumeric():
            UserInput = int(UserInput)
            sum = sum + int(UserInput)
            print(f"Your Total so far {sum}")
        elif UserInput == 'q':
            print(f"Your total is '{sum}'")
            break
        else:
            print("!!Invalid Input!!")
    