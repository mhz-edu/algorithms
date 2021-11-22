import random, copy

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

def dist(pair):
    p1, p2 = pair
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def closest_split_pair(qx, rx, qy, ry, delta):
    sy = []
    middlex = qx[-1][0]
    for point in (qy + ry):
        if abs(point[0] - middlex) <= delta:
            sy.append(point)
    best = delta
    best_pair = ((30,30), (-30, -30))
    for i in range(len(sy) - 1):
        for j in range(1, min(7, len(sy) - i)):
            if dist((sy[i], sy[i+j])) < best:
                best = dist((sy[i], sy[i+j]))
                best_pair = (sy[i], sy[i+j])
    return best_pair
        

def closest_pair_three(l):
    pairs = [(l[0], l[1]), (l[1], l[2]), (l[0], l[2])]
    dists = list(map(dist, pairs))
    ind = dists.index(min(dists))
    return pairs[ind]

def closest_pair_core(px, py):
    if len(px) == 2:
        return (px[0], px[1])
    elif len(px) == 3:
        return closest_pair_three(px)
    else:
        middlex = len(px) // 2
        x_in_middlex = px[middlex][0]
        qx = px[:middlex]
        rx = px[middlex:]
        qy = []
        ry = []
        for point in py:
            if point[0] < x_in_middlex:
                qy.append(point)
            else:
                ry.append(point)
        left_pair = closest_pair_core(qx, qy)
        right_pair = closest_pair_core(rx, ry)
        delta = min(dist(left_pair), dist(right_pair))
        split_pair = closest_split_pair(qx, rx, qy, ry, delta)
        
        pairs = [left_pair, right_pair, split_pair]
        dists = list(map(dist, pairs))
        ind = dists.index(min(dists))
        return pairs[ind]

def closest_pair(points):
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    return closest_pair_core(px, py)


def random_pivot(l):
    return random.randint(0, len(l)-1)

def randomized_select(l, order):
    if len(l) == 1:
        return l[0]
    else:
        less_pivot, pivot, greater_pivot = partition(l, random_pivot)
        if len(less_pivot) == order - 1:
            return pivot[0]
        elif len(less_pivot) > order - 1:
            return randomized_select(less_pivot, order)
        else:
             return randomized_select(greater_pivot, (order - 1) - len(less_pivot))

def median_of_median(l):
    median_array = []
    if len(l) < 5:
        median_array.append(sorted(l)[len(l)//2])
    else:
        d = 1 if (len(l) % 5 != 0) else 0
        for i in range(d + (len(l) // 5)):
            median_array.append(sorted(l[(i * 5):(i + 1) * 5])[2])
    return median_array

def deterministic_select(l, order):
    if len(l) == 1:
        return l[0]
    else:
        c = median_of_median(l)
        selected_pivot = deterministic_select(c, len(l)//10)
        pivot_index = l.index(selected_pivot)
        less_pivot, pivot, greater_pivot = partition(l, lambda x: pivot_index)
        if len(less_pivot) == (order - 1):
            return pivot[0]
        elif len(less_pivot) > (order - 1):
            return deterministic_select(less_pivot, order)
        else:
             return deterministic_select(greater_pivot, (order-1) - len(less_pivot))

def karger_mincut(graph):
    trials = len(graph) ** 2
    min_cut_length = len(graph)
    for t in range(trials):
        trial_graph = copy.deepcopy(graph)
        random.seed(t)
        min_cut(trial_graph)
        if len(trial_graph[list(trial_graph)[0]]) < min_cut_length:
            min_cut_length = len(trial_graph[list(trial_graph)[0]])
            cut = trial_graph
    return cut
        
def min_cut(trial_graph):
    while (len(trial_graph)>2):
            node = random.choice(list(trial_graph))
            edge = (node, random.choice(trial_graph[node]))
            merge_nodes(trial_graph, edge)
            remove_loops(trial_graph)
    return trial_graph

def merge_nodes(graph, edge):
    graph[edge[0]] = graph[edge[0]] + graph[edge[1]]
    graph[edge[0]].remove(edge[0])
    graph[edge[0]].remove(edge[1])
    del graph[edge[1]]
    if (edge[0] in graph[edge[0]] and edge[1] in graph[edge[0]]):
        graph[edge[0]].remove(edge[1])
    for key in graph.keys():
        while (graph[key].count(edge[1]) > 0):
            graph[key].remove(edge[1])
            graph[key].append(edge[0])

def remove_loops(graph):
    for node in graph.keys():
       while (graph[node].count(node) > 0):
            graph[node].remove(node)



def load_graph(path):
    out = {}
    with open(path, 'r') as f:
        for line in f:
            numbers = [int(n) for n in line.split('\t') if n.isnumeric()]
            out[numbers[0]] = numbers[1:]
    return out


def load_list(path):
    out = []
    with open(path, 'r') as f:
        for line in f:
            out.append(int(line))
    return out