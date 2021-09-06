#nterm=int(input("enter the number of terms of series\n"))
#count=0
#n1,n2=0,1
#while count <nterm:
#    print(n1)
#    nth=n1+n2
#    n1=n2
#    n2=nth
#    count=count+1




nterm = int(input("enter the number of terms in fibo series\n"))
count=0
n1,n2=0,1
while count<nterm:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1