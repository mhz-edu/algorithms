def recursive_mult(x, y):
    half_x = int(len(x) / 2)
    half_y = int(len(y) / 2)
    if (half_x == 0) or (half_y == 0):
        return int(x) * int(y)
    else:
        a = x[:half_x]
        b = x[half_x:]
        c = y[:half_y]
        d = y[half_y:]
        s = recursive_mult(a, c) * pow(10, (half_x + half_y)) + \
            recursive_mult(a, d) * pow(10, half_x) + \
            recursive_mult(b, c) * pow(10, half_y) + \
            recursive_mult(b, d)
        return s

def karatsuba_mult(x, y):
    assert (len(x) == len(y))
    if (len(x) == 1):
        return int(x) * int(y)
    else:
        assert (len(x) % 2 == 0)
        half = int(len(x) / 2)
        a = x[:half]
        b = x[half:]
        c = y[:half]
        d = y[half:]
        step1 = karatsuba_mult(a, c)
        step2 = karatsuba_mult(b ,d)
        step3 = (int(a) + int(b))*(int(c) + int(d)) - step1 - step2
        s =  step1 * pow(10, 2 * half) + (step3 * pow(10, half)) + step2
        return s

print(karatsuba_mult('3141592653589793238462643383279502884197169399375105820974944592',
                     '2718281828459045235360287471352662497757247093699959574966967627'))

print(karatsuba_mult('1234','5678'))