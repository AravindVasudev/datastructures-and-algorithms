def insertionSort(arr):
    for i in range(1, len(arr)): # iterate from 1..n
        element  = arr[i] # current element
        j = i # current index
        while j > 0 and arr[j - 1] > element:
            '''
            compare with the sorted list on the right and shift those elements
            one place right until the current element is smaller than it's
            left side element
            '''
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = element # place the element

    return arr

def insertionSort2(arr):
    for i, element in enumerate(arr):
        while i > 0 and arr[i - 1] > element:
            arr[i], i = arr[i - 1], i - 1
        arr[i] = element

    return arr

if __name__ == '__main__':
    arr = list(map(int, input('Enter the numbers:').split(' ')))
    print(*insertionSort(arr))
    print(*insertionSort2(arr))
