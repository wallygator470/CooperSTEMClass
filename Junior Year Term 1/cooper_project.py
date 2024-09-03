

a = 15
b = 23
c = 29
d = 555

def fraction(n, d):
    return str(n) + '/' + str(d)

def mult_nums(x, y):
    return x * y

def answer(a, b, c, d):
    return fraction(a, b) + ' + ' + fraction(c, d) + ' = ' + fraction(mult_nums(a, d) + mult_nums(b, c), mult_nums(b, d))

print(answer(a, b, c, d))
