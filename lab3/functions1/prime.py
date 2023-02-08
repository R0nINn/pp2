mylist = [1,2,3,4,5,6,7,8,9,10]

# def prime ():
    
#     cnt =0
    
#     l = []
#     for i in mylist:
#         if i == 2:
#             l.append(i)
            
#         elif i==1:
#             continue
#         for j in (2,i):
#             if i%j==0:
#                 cnt+=1
#         if cnt == 0:
#                l.append(j)
#     return l
# print(prime())
        
def filterprime():
    l = []
    for i in mylist:
        cnt = 0
        if(i == 2):
            l.append(i)
            continue
        elif(i == 1):
            continue
        for j in range(2, i):
            if(i % j == 0):
                cnt += 1
        if(cnt == 0):
            l.append(i)
    return l
print(filterprime())