def f(x):
    nr = (x ** 2 + 1) % n
    return nr


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def pollard(x0, n):
    d = 1
    xi = x2i = x0
    i = 0
    count = 0
    while (d == 1 or d == n):
        xi = f(xi)
        x2i = f(f(x2i))
        i += 2
        d = gcd(abs(x2i - xi), n)
        print('(|x' + str(i) + ' - x' + str(i // 2) + '|, n) = ' + str(d))
        # if d == n:
        #     print('FAILURE')
        #     return
        count += 1
        if count > 1000:
            print('Count reached 1000')
            break
    print(xi % d)
    print(x2i % d)
    print('n = ' + str(d) + ' * ' + str(n // d))


if __name__ == '__main__':
    x0 = 2
    n = 2 ** 499 - 1
    #n = 187
    pollard(x0, n)
