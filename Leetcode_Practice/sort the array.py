import re
import itertools
import os
#
# Complete the 'groupSort' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#1. [[value, frequency], [val, freq]] descending by frequency
#2. for items with the same freq, ascending by val

def groupSort(arr):
    # Write your code here
    freq = 0
    res = []
    sarr = [str(i) for i in arr]
    s = ""
    one_time_arr = list(dict.fromkeys(arr))
    one_time_sarr = [str(i) for i in one_time_arr]
    for i in sarr:
        s+="{}".format(i)
    print(s)
    for i in one_time_sarr:
        pattern = re.compile("".join(i))
        m = re.search(pattern,s)
        while m:
            m = pattern.search(str(s), m.start()+1)
            freq+=1
        res.append([int(i), freq])
        freq = 0
    print(res)
    # decesending by freq
    helpdict = {}
    newRes = []
    l = []
    for val, freq in res:
        if freq not in helpdict.keys():
            helpdict[freq] = [val]
        else:
            helpdict[freq].append(val) # helpdict = {freq: [val1, val2...]}

    freqlist = list(helpdict.keys())
    freqlist.sort()
    des_freq = [freqlist[i] for i in range(len(freqlist)-1, -1, -1)] # descending freq list
    tmpRes = [[helpdict[i],i] for i in des_freq]# [[freq, valist],.....] descending freq
    print(tmpRes)
    for item in tmpRes:
        item[0].sort()
        l.append(item[1])
        print(item[0], l)
        newRes.extend(list(itertools.product(item[0],l)))
        l = []

    for i in newRes:
        i = list(i)
    return newRes






    # helpdict = {freq:[].append(val) for val, freq in res if freq in dict.keys }

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # arr_count = int(input().strip())

    arr = [1,2,3,4,3,2,6,7,8,9]

    # for _ in range(arr_count):
    #     arr_item = int(input().strip())
    #     arr.append(arr_item)

    result = groupSort(arr)
    print(result)
    # fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    # fptr.write('\n')
    #
    # fptr.close()



############
