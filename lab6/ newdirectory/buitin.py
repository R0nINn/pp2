import math

mylist = [1,2,3,4,5]

def multy(mylist):
    
    prod = math.prod(mylist,start = 1)
    return prod

print(multy(mylist))

s=input()

def count (s):
    
    l ={ 'lower_case' : 0 , 'upper_case' : 0 }
    for x in s:
        if x.isupper():
            l['upper_case']+=1
        elif x.islower():
            l['lower_case']+=1
        else :
            pass
    print('NO. of lower case letters: ' , l['lower_case'])
    print('No. of upper case letters: ' , l['upper_case'])
    
count(s)


word = input()

def isPal(word):

    return True if word[::-1] == word else False

print(isPal(word))
    




x = (True, True, False)

result = all(x)

print(result)