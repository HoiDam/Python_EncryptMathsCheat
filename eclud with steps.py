import os
while True:
    print("Big:")
    b=input()
    print("Small:")
    s=input()
    print(b," x + ",s," y = 1")
    r=999999
    line=1
    d_array=[]
    while r>1:
        
        d=int(int(b)/int(s))
        r=int(int(b)%int(s))
        d_array.append(d)
        print("line:",line,"equation:",b,"=",d,"x",s,"+",r)
        b=s
        s=r
        line+=1

    print("i\txi\tyi\tqi")
    print("0\t1\t0\t")
    curr=1
    old_xi=1
    old_yi=0
    xi=0
    yi=1
    while curr<line:
        print(curr,"\t",xi,"\t",yi,"\t",d_array[curr-1])
        
        temp_old_xi=xi
        temp_old_yi=yi
        xi=d_array[curr-1]*xi+old_xi
        yi=d_array[curr-1]*yi+old_yi
        old_xi=temp_old_xi
        old_yi=temp_old_yi
        curr+=1

    print(curr,"\t",xi,"\t",yi,"\t")    
    input("Press Enter to continue...")
    os.system('cls')