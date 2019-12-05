#a = [1,23,4,[3,31,2,[123,123,[99,44,[3,[2],[]]]]]]
a= [1,23,4,[3,31,2,[123,123,[99,44,[3,[20],[2,[[3,[[[[2]]],[484,[]],[[[]]]]]]],[1092]]]]]]
c = []
print('original list : ',a)

def flatlist(a):
    b = []
    for i in a:
        if type(i)!=list:
            b.append(i)
        else:
            b.extend(flatlist(i))
    return b

# def flatlist2(a):
#     b=[]
#     for i in a:
#         if type(i)!=list:
#             b.append(i)
#         else:
#             flatlist3(i)
#     return b
c=flatlist(a)
print("flatten - \n",c)
