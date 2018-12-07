setup = '''
def partition(arr,low,high):
    i = (low -1) #smaller index numbers
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi -1)
        quickSort(arr, pi + 1 , high)

def measureThis(size):
    mylist = []
    for i in range(size):
        mylist.add(random.randint(0, size))
def measureThis1(size):
    mylist = []
    for i in range(size):
        mylist.add(random.randint(10, size))
def measureThis2(size):
    mylist = []
    for i in range(size):
        mylist.add(random.randint(1000, size))





'''

import timeit
print(timeit.timeit(setup=setup,stmt="measureThis"))
print(timeit.timeit(setup=setup,stmt="measureThis1"))
print(timeit.timeit(setup=setup,stmt="measureThis2"))


