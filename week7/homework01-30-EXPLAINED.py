# lst = [[x for x in range(3)]
# for y in range(3)]
#   for r in range(3):
#       for c in range(3):
#           if lst[r][c] % 2 != 0:
#               print(“#”)
# (a) zero
# (b) three
# (c) nine
# (d) six


lst = [[x for x in range(3)] for y in range(3)]
print(lst)
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")
