n=int(input())

while n<=0:
    n=int(input())

total=0
count=0

number=int(input())

total=total+number
count=count+1

while count<n:
    number=int(input())

    total=total+number
    count=count+1    

print(total/count)