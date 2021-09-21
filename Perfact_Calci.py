#all the formulas are here
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def devide(x, y):
    return x / y

print("Hi, Wellcome to the Calulator -_-")

while True:
    c = input("Choose what you wnat to do:\n1. Add\n2. Substract\n3. Multiply\n4. Devide\n:")
    if c in ('1', '2', '3', '4'):
        c = int(c)
        break
    else:
        print("!!Invalid Input!!")


while True:
    a = input("Enter 1st Number:")
    if a.isnumeric():
        a = int(a)
        break
    else:
        print("!!Please enter only number!!")

while True:
    b = input("Enter 2nd Number:")
    if b.isnumeric(): 
        b = int(b) 
        break
    else:
        print("!!Please enter only number!!")

if c == 1: print(f"{a} + {b} = {add(a, b)}")
elif c == 2: print(f"{a} - {b} = {subtract(a, b)}")
elif c == 3: print(f"{a} x {b} = {multiply(a, b)}")
elif c == 4: print(f"{a} / {b} = {devide(a, b)}")
else: print("!!Invalid Input!!")

print("Thanks for Using -_-")