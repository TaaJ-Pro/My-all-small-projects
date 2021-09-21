print("Hi, Welcome to Star Maker")
Int_var = int(input("Enter no of rows you want to print: "))
Bool_var = input("Enter 1 for True and 0 for False: ")

if Bool_var == '1':
    for i in range(0, Int_var+1):
        print("*"*i)
elif Bool_var == '0':
    for i in  range(Int_var,0,-1):
        print("*"*i)
