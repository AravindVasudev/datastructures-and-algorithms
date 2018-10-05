def merge(left, right):
    result = []
    i, j = 0, 0

    while len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def mergesort(arr):
    if len(arr) <= 1: return arr
    middle = int(len(arr) / 2)

    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])

    return merge(left, right)

if __name__ == '__main__':
    print(mergesort([5, 4, 3, 2, 1]))