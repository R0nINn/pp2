def reverse(s):
    s = s.split(" ")
    t = list(s)
    t.reverse()
    for i in t:
        print(i, end = ' ')

# reverseSentence("We are ready")
# result: ready are We