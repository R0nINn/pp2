import re

txt = "cat cot car coat cut"

x = re.findall(r"\bc\wt\b" , txt)

print(x)