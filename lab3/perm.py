import itertools

def perm(string):
    
  perms = [''.join(p) for p in itertools.permutations(string)]
  print(*perms, sep=' ')

# permutations("abc")
# result: abc acb bac bca cab cba