#Finding multiplication Table
while True:
    x = input("Which number you want Table:")
    if x.isnumeric():
        x = int(x)
        for i in range(1, 11): 
            print(f"{x} x {i} = {x*i}")
        print("Thanks for Using")
        break
    else:
        print("Your Input is not a Number!!!!")