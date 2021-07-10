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

def partition(array, pivot_func):
        if len(array) == 1:
            return (array, [], [])
        pivot_index = pivot_func(array)
        pivot = array.pop(pivot_index)
        i = 0
        for j in range(len(array)):
            if array[j] < pivot:
                array[j], array[i] = array[i], array[j]
                i = i + 1
        return (array[:i], [pivot], array[i:])

def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        less_pivot, pivot, greater_pivot = partition(l, median_of_three)
        return quick_sort(less_pivot) + pivot + quick_sort(greater_pivot)


def first_element(l):
    return 0

def last_element(l):
    return len(l) - 1

def median_of_three(l):
    if len(l) < 3:
        return 0
    else:
        temp = [l[0], l[(len(l)-1)//2], l[-1]]
        temp.sort()
        return l.index(temp[1])

def comparison_number(l, func=first_element):
    if len(l) <= 1:
        return 0
    else:
        count = len(l) - 1
        less_pivot, pivot, greater_pivot = partition(l, func)
        return count + comparison_number(less_pivot, func) + comparison_number(greater_pivot, func)


def load_list(path):
    out = []
    with open(path, 'r') as f:
        for line in f:
            out.append(int(line))
    return out