def qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = list(filter(lambda x: x <= pivot, arr[1:]))
    right = list(filter(lambda x: x > pivot, arr[1:]))

    return qsort(left) + [pivot] + qsort(right)

def main():
    print(qsort([5, 4, 3, 2, 1]))
    print(qsort([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    main()
