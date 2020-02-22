number = int(input("Enter a number: "))
def armstrong(number):
    for count in range(0,number,1):
        temp=count
        ord=len(str(count))
        s=0
        while(temp>0):
            rem=temp%10
            s+=rem**ord
            temp=temp//10
        if(count==s):
            print(s)
print("Armstrong numbers upto:",number)            
armstrong(number)
