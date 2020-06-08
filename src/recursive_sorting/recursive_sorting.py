# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    while elements is not len(elements) - 1: 
        elements_combined = arrA + arrB
        elements_val = elements_combined[0]
        elements += 1 
        merged_arr = elements_val  
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) > 1: 
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1 
            else: 
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i+= 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j+= 1
            k += 1 

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1

    if (arr[mid] <= arr[start2]):
        return 
    while (start <= mid and start2 <= end): 
        if (arr[start] <= arr[start2]):
            start += 1
        else: 
            value = arr[start2]
            index = start2
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1 
            arr[start] = value 

            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r): 
        m  = l + (r -1) // 2

        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
