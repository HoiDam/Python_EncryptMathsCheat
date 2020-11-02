import os

def func_bs():
    bs_array=[]
    print("baby step = a * b ^ r mod c")
    print("a:")
    a=int(input())
    print("b:")
    b=int(input())
    print("r:")
    r=int(input())+1
    print("c:")
    c=int(input())

    for i in range(r):
        ans=((a*pow(b,i))%c)
        print(i,"\t",ans)
        bs_array.append(ans)
    return bs_array
    

def func_gs():
    gs_array=[]
    print("giant step = b ^ m mod c")    
    print("b:")
    b=int(input())
    print("m:")
    m=int(input())+1
    print("c:")
    c=int(input())
    for i in range(m):
        ans=(pow(b,i))%c
        print(i,"\t",ans)
        gs_array.append(ans)
    return gs_array

def func_find(bs_array,gs_array):
    print("baby step array : ")
    print("[",end='')
    for i in range(len(bs_array)):
        print("(",i,",",bs_array[i],"),",end='')
    print("]")

    print("giant step array : ")
    print("[",end='')
    for i in range(len(gs_array)):
        print("(",i,",",gs_array[i],"),",end='')
    print("]")

    for m in range(len(gs_array)):
        for i in range(len(bs_array)):
            if gs_array[m]==bs_array[i]:
                print("r : ",i)
                print("m : ",m)
                return 0      


while True:
    print("1 : baby steps(right hand)")
    print("2 : giant steps(left hand)")
    print("3 : find same")
    msg=int(input())
    if msg==1:
        bs_array=func_bs()
    elif msg==2:
        gs_array=func_gs()
    elif msg==3:
        func_find(bs_array,gs_array)
    

