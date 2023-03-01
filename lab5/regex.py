# import re

# txt = "alphabbbbet"

# x = re.findall('a' , txt)

# print(x)

# import re

# txt = 'asd abb wejkwe abbbsds sdabb sfdsf'

# t = re.findall('a[b]{0,237487679}', txt)

# print(t)



# import re

# txt = 'asd abb wejkwe abbbsds sdabb sfdsf'

# t = re.findall('a[b]{2,3}', txt)

# print(t)


# import re

# txt = 'abc abc_bc xyz xy_z u_p'

# x = re.findall(r'[a-z]+[_][a-z]+' , txt)

# print(x)


# import re

# txt = 'aBc AbdgaD vvhAAnd Asd asD'

# x = re.findall(r'[A-Z][a-z]+' , txt)

# print(x)

# import re

# txt = "abcd ahhuydgb hdaid annhbcfd"

# x = re.findall(r'a[a-zA-z]+b' , txt)

# print(x)

# import re 

# txt = "abdj jfs.nadh kav,ad"

# x = re.sub(r'[ ]|[,]|[.]',':' , txt)

# print(x)

# import re


# text = input()

# match = re.split('_', text)

# for iter in match:
#     print(iter, sep = '')
    
# import re
# text = input()
# match = re.split('[A-Z]', text)
# print(match)

# import re

# text = input()

# match = re.split('[A-Z]', text)

# for iter in match:
#     print(iter, ' ')

# import re

# def ToSnake(s):
#     return re.sub("(?!^)(?=[A-Z])", '_', s).lower()

# text = input()

# res = ToSnake(text)

# print(res)