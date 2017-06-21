def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def bubbleSortWithFlag(arr):
    changed = True
    while changed:
        changed = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                changed = True

    return arr

if __name__ == '__main__':
    arr = list(map(int, input('Enter the numbers:').split(' ')))
    print(*bubbleSort(arr))
    print(*bubbleSortWithFlag(arr))
