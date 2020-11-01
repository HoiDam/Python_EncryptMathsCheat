import os
while True:
    print("root:")
    r=input()
    r=int(r)
    ori_r=int(r)
    print("expo:")
    e=input()
    e=int(e)
    print("mod")
    m=input()
    m=int(m)
	
	
    bin_e=bin(int(e))[2:]
    
    count = 0
    for i in range(len(bin_e)):
        if i==0:
            ans=r
            
        else:
            if int(bin_e[i])==1:
                ans=str(r)+" ^ 2 * "+str(ori_r)+" = "
                cal=r*r
                cal=cal%m
                cal=cal*ori_r
                cal=cal%m
                r=cal
                ans+=str(cal)
            elif int(bin_e[i])==0:
                ans=str(r)+" ^ 2 "+"="
                cal=r*r
                cal=cal%m
                r=cal
                ans+=str(cal)
        print(bin_e[i],"\t",ans)
        count+=1
        if count==4:
            print("\t")
            count=0
    
    input("Press Enter to continue...")
    os.system('cls')

