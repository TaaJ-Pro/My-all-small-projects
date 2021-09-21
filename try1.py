def checknum(num):
    while True:
        if num.isnumeric():
            num = int(num)
            return True
            break
        else:
            print("!!Enter Only Number!!")
            return False

while True:
    check = checknum()
    num = input("Enter a number: ")
    check = checknum(num)
    next(check)
    check.send(num)

# while True:
#     try:
#         print("Input is an integer number.")
#         break
#     except ValueError:
#         try:
#             num = float(num)
#             print("Input is an float number.")
#             break
#         except ValueError:
#             print("This is not a number. Please enter a valid number")

