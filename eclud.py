import os
while True:
    print("Big:")
    b=input()
    print("Small:")
    s=input()
    d=int(b)/int(s)
    r=int(b)%int(s)
    print("divident:",int(d),"remainder:",r)
    input("Press Enter to continue...")
    os.system('cls')