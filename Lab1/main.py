import time


def isDivisible(x, a):
    while x >= a:
        x -= a
    return x == 0


def gcd_euclidean(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


def gcd_prime_factors(x, y):
    i = 2
    gcd = 1
    while x > i or y > i:
        while isDivisible(x, i) and isDivisible(y, i):
            gcd *= i
            x //= i
            y //= i
        i += 1
    return gcd


def gcd_brute_force(x, y):
    gcd = min(x, y)
    while not isDivisible(x, gcd) or not isDivisible(y, gcd):
        gcd -= 1
    return gcd


if __name__ == '__main__':
    tests = [
        (18, 12),
        (30, 17),
        (45, 70),
        (255, 300),
        (255, 177),
        (101, 301),
        (4137524, 1227244),
        # (294733, 10383680172),
        (4 ** 4, 6 ** 4),
        # (2 ** 50, 4 ** 20),
        (6 ** 3, 3 ** 7)
        # (12345665434562,57658787675842)
    ]
    for test in tests:
        x = test[0]
        y = test[1]
        print("\nx={},y={}".format(x, y))

        print("Start Eucliden GCD")
        start = time.time()
        gcd = gcd_euclidean(x, y)
        end = time.time()
        print("Time elapsed: {} seconds".format(end - start))
        print("Gcd is {}\n".format(gcd))

        print("Start Prime Factorization GCD")
        start = time.time()
        gcd = gcd_prime_factors(x, y)
        end = time.time()
        print("Time elapsed: {} seconds".format(end - start))
        print("Gcd is {}\n".format(gcd))

        print("Start Brute Force GCD")
        start = time.time()
        gcd = gcd_brute_force(x, y)
        end = time.time()
        print("Time elapsed: {} seconds".format(end - start))
        print("Gcd is {}\n".format(gcd))
        print("---------------------------\n")
