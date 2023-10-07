def printnext5():
    for sth in range(2,5):
        yield sth +5
        yield sth -6
#two results for each number from 2 to 4 --> 3 pairs

y = printnext5()

for i in range(9):
    print(next(y))