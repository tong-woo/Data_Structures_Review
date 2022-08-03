def swap(arr, i , j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr

def performOperations(arr, operations):
    # Write your code here
    arrNew= []
    total = int(len(operations))
    opTimes = [k+1 for k in range(len(operations)-1,0, -1)]
    print(opTimes)
    for i in range(1,total):
        if opTimes[i-1]%2 != 0:
            print(operations[i][0])
            arrNew = swap(arr, len(arr)-1-operations[i][0], operations[i][0])
            print(arrNew)
    return arrNew

arr=[1,2,3]
operations = [[0,2],[1,2],[0,2]]
# arr=[9,8,7,6,5,4,3,2,1,0]
# operations = [[0,9],[4,5],[3,6],[2,7],[1,8],[0,9]]
print(arr)
print(performOperations(
    arr, operations
))
