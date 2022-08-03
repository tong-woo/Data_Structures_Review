from random import randrange, shuffle #For quick sort
def Binary_Search(sorted_list, left, right, target):
    if left >= right:
        return "Not found"
    midIdx = (left + right) // 2
    midVal = sorted_list[midIdx]

    if midVal == target:
        return midIdx
    elif midVal > target:
        return Binary_Search(sorted_list, left, midIdx, target)
    elif midVal < target:
        return Binary_Search(sorted_list, midIdx+1, right, target)


def bubble_sort(arr):
    for i in range(len(arr)):
        for idx in range(len(arr)-1-i):
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
    return arr


def merge(left, right):
    result = []
    while left and right:
        if left[0]<right[0]:
            result.append(left)
            left.pop(0)
        else:
            result.append(right)
            right.pop(0)
    if left:
        result.extend(left)
    if right:
        result.extend(right)

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    midIdx = (0+len(arr))//2
    left_split  = arr[:midIdx]
    right_split = arr[midIdx+1:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)

def quick_sort(arr, start, end):
    if start >= end:
        return arr

    pivot_idx = randrange(start, end+1)
    pivot_element = arr[pivot_idx]

    arr[pivot_idx] , arr[end] = arr[end], arr[pivot_idx]

    less_than_pointer = start

    for i in range(start, end):
        if arr[i]<pivot_element:
            arr[i], arr[less_than_pointer] = arr[less_than_pointer], arr[i]
            less_than_pointer+=1
        arr[less_than_pointer], arr[end] = arr[end], arr[less_than_pointer]

    quick_sort(arr, start, less_than_pointer-1)
    quick_sort(arr, less_than_pointer+1, end)

    return arr


def insertsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j] = key
    return arr

unsorted_list = [3,7,12,24,36,42]

# use quicksort to sort the list, then print it out!

sorted_list = insertsort(unsorted_list)
print(sorted_list)