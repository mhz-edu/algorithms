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

# print(karatsuba_mult('3141592653589793238462643383279502884197169399375105820974944592',
#                      '2718281828459045235360287471352662497757247093699959574966967627'))

# print(karatsuba_mult('1234','5678'))

def inversions_number(l):
    def inversions_split(left, right, n):
        i = 0
        j = 0
        out = []
        inv_count = 0
        for k in range(n):
            if i == len(left):
                out.extend(right[j:])
                break
            if j == len(right):
                out.extend(left[i:])
                break
            if left[i] < right[j]:
                out.append(left[i])
                i = i + 1
            else:
                inv_count = inv_count + len(left) - i
                out.append(right[j])
                j = j + 1
        return (out, inv_count)
    def recursive_call(l):
        if len(l) == 1:
            return (l, 0)
        else:
            middle_index = len(l)//2
            left_part = l[:middle_index]
            right_part = l[middle_index:]
            left_sorted, inv_l = recursive_call(left_part)
            right_sorted, inv_r = recursive_call(right_part)
            sorted, inv_s = inversions_split(left_sorted, right_sorted, len(l))
        return (sorted, inv_l + inv_r + inv_s)

    a, b = recursive_call(l)
    return b

def load_list(path):
    out = []
    with open(path, 'r') as f:
        for line in f:
            out.append(int(line))
    return out

test = [1, 3, 5, 2, 4, 6]
print(inversions_number(test))
print(inversions_number(load_list('IntegerArray.txt')))