# The very first stage is if we have two sorted arrays, then we need to merge them and create a sorted array.
# arr1 = [2, 5, 7, 12, 20, 24, 29]
# arr2 = [6, 9, 10, 14, 15, 19]
def merge_sorted_arrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    merged_array = []
    i, j, k = 0, 0, 0
    while (i < n and j < m):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
        k += 1
    while (i < n):
        merged_array.append(arr1[i])
        i += 1
        k += 1
    while (j < m):
        merged_array.append(arr2[j])
        j += 1
        k += 1
    return merged_array

arr1 = [2, 5, 7, 12, 20, 24, 29]

arr2 = [6, 9, 10, 14, 15, 19]

print(merge_sorted_arrays(arr1, arr2))

#I think the next part is merging two sorted parts in the same array, let us say we have an array
# arr = [8, 1, 3, 6, 11, 2, 4, 9, 7, 6], Here from 3, 6, 11 and 2, 4, 9 are sorted parts of the arr.
# Now after sorting these parts we get arr = [8, 1, 2, 3, 4, 6, 9, 11, 7, 6].

def merge_in_array(arr, l, y, r):
    c = [0] * (r-l + 1)
    i = l
    j = y
    k = 0
    while (i < y and j <= r):
        if arr[i] < arr[j]:
            c[k] = arr[i]
            i += 1
            k += 1
        else:
            c[k] = arr[j]
            j += 1
            k += 1
    while(i < y):
        c[k] = arr[i]
        i += 1
        k += 1
    while (j <= r):
        c[k] = arr[j]
        j += 1
        k += 1

    for i in range(l, r + 1):
        arr[i] = c[i - l]
    return arr

arr = [8, 1, 3, 6, 11, 2, 4, 9, 7, 6]
# print(merge_in_array(arr, 2, 5,7))

# Now finally mergeSort algorithm which uses the mergeing two sorted parts of the array

def merge_sort(arr):
    def merge(arr, l, r):
        if (l == r):
            return
        mid = (l + r) // 2
        merge(arr, l, mid)
        merge(arr, mid + 1, r)
        merge_in_array(arr, l, mid + 1, r)
    l = 0
    r = len(arr) - 1
    merge(arr, l, r)
    return arr
print(merge_sort(arr))





