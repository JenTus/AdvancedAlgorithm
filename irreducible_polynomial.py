# addition table
a = [[(i + j) % 9 for i in range(9)] for j in range(9)]
for i in range(9):
    print a[i]


# Multiplication table in F_9
b = [[(i * j) % 9 for i in range(9)] for j in range(9)]
for i in range(9):
    print b[i]
