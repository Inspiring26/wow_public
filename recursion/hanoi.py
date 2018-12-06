num = 0
def hanoi(n,x,y,z):
    global num

    if(n==1):
        print(x,"-->",z)
        num+=1
    else:
        hanoi(n-1,x,z,y)
        print(x,"-->",z)
        num+=1
        hanoi(n-1,y,x,z)

n=int(input("num:"))


hanoi(n,"x","y","z")
print("一共移动了",num, "次")
print("over")
