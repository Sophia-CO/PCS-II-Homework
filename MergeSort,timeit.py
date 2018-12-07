setup = '''
def MergeSort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = MergeSort(x[:mid])
    z = MergeSortt(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
            return result

def measureThis10(size):
    mylist = []
    for i in range(size):
        mylist.add(random.randint(1000, size))
def measureThis11(size):
    mylist = []
    for i in range(size):
        mylist.add(random.randint(100000, size))
def measureThis12(size):
    mylist = []
    for i in range(size):
        mylist.add(random.randint(10, size))


'''


import timeit
print(timeit.timeit(setup=setup,stmt="measureThis10"))
print(timeit.timeit(setup=setup,stmt="measureThis11"))
print(timeit.timeit(setup=setup,stmt="measureThis12"))
