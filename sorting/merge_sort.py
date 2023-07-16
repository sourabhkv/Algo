def mergesort(x: list):
    if len(x) > 1:
        mid = len(x) // 2
        left = x[:mid]
        right = x[mid:]

        mergesort(left)
        mergesort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                x[k] = left[i]
                i += 1
            else:
                x[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1




x = [2,-1,5,6,8,4]
mergesort(x)
print(x)