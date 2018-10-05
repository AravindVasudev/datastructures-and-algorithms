def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            '''
            gets the next minimum from the left of the current element
            '''
            if arr[j] < arr[mini]:
                mini = j
        if mini != i:
            arr[mini], arr[i] = arr[i], arr[mini] # swap current element with mini

    return arr

if __name__ == '__main__':
    arr = list(map(int, input('Enter the numbers:').split(' ')))
    print(*selectionSort(arr))
