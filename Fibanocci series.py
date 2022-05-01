first_no=0
second_no=1
limit=int(input("Enter a number")) 
print(first_no,second_no,end="\n")
for i in range(1,limit+1,1):
    sum=first_no+second_no
    first_no=second_no
    second_no=sum
    print( sum,end="\n")
