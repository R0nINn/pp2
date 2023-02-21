# x = int(input())

# def mygen(x):
#     y = (i**2 for i in range(x))
#     for i in range(x):
#         print(next(y))
    
# mygen(x)
        
    
# def gen(x):
#     i = 0
#     while i <=x:
#         if i%2 == 0:
#             yield i
#         i+=1
        
# x = int(input())
# values =[]

# for i in gen(x):
#     values.append(str(i))
    
# print(",".join(values))
            
# def devisible(n):
#     i = 0
#     while i <=n:
#         if i%3 == 0 and i%4 == 0:
#             yield i
#         i+=1
        
# n = int(input())

# for i in devisible(n):
#     print(i)

# def square(n):
#     i = 0
#     while i <= n:
#         yield i*i
#         i+=1
    
# n = int(input())

# for i in square(n):
#     print(i)

def back(n):
    i = n
    while i>=0:
        yield i
        i-=1
        
n = int(input())

for i in back(n):
    print(i)    