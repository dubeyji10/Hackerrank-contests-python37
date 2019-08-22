#n = int(input('enter the number '))
#h = len(str(bin(n))[2:])

#for k in range(n+1):
#    tt=str(bin(k))[2:]
#    p=len(tt)
#    print(' '*(h-p)+tt)
# or we could do this  -___________________



n = eval(input(""))
if n>15:
    for i in range(0,n+1):
        print("{:5b}".format(i))
else:
    for i in range(0,n+1):
        print("{:4b}".format(i))
