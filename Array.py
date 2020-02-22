num = input("Enter how many elements you want:")
print ('Enter numbers in array: ') #Enter the elements you want to insert horizontally with space
num_list=list(map(int,input().split()))
print(num_list) 
num = int(input("Enter the element you want to insert:"))
pos = int(input("Enter the position you want to enter the element:"))
def insert(num_list,num,pos):
    l=[ ]
    sp=[ ]
    le=len(num_list)
    if(pos==0 or int(pos)>le+1):
        print("Invalid postion")
        print("Enter valid position")
    else:
        print("Array before insertion")
        print(num_list)
        a=int(pos)-1
        for i in range(0,a):
            l.append(num_list[i])
        for i in range(a,le):
            sp.append(num_list[i])
        l.append(num)
        print("Array after insertion")
        num_list=l+sp
        print(num_list)
insert(num_list,num,pos)
