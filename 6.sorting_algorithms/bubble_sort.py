
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))

def swap(arr, index1, index2):
    tmp = arr[index1]
    arr[index1] = index2
    arr[index2] = tmp

def bubble_sort_unoptimized(arr):
    iter_count = 0
    for item in arr:
        for i in range(len(arr) - 1):
            iter_count+=1
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
    # iteration_count = 0
    # for el in arr:
    #     for index in range(len(arr) - 1):
    #         iteration_count += 1
    #         if arr[index] > arr[index + 1]:
    #             swap(arr, index, index + 1)
    print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iter_count))

def bubble_sort(arr):
    iter_count = 0
    for i in range(len(arr)):
        # iterate through unplaced elements
        for idx in range(len(arr) - i - 1):
            # iteration_count += 1
            if arr[idx] > arr[idx + 1]:
                # replacement for swap function
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

    print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iter_count))

bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)
print("POST SORT: {0}".format(nums))

