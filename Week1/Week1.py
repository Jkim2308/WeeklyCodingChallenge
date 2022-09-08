def largestGap(arr):
    arr.sort()
    print (arr[len(arr)-1] - arr[0])

largestGap([3, 10, 6, 7])
largestGap([-3, -1, 6, 7, 0])
largestGap([90, 10, 30, 50, 40])
largestGap([-10, 5, 25, 15, -5])
