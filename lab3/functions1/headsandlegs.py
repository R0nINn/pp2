h = 34
l =94

def puzzle(h,l):
    chikens = (l - (4 * h)) / -2
    rabits = h - chikens
    return chikens,rabits
print(puzzle(h,l))