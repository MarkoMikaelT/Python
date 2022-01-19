import heapq

#kth largest elemnt in an array
arr = [1, 7, 4, 5, 2, 6, 7, 12]     #sorted [1, 2, 4, 5, 6, 7, 7, 12]
k = 3

def Main():
    arr1 = arr
    print(KthLargest(arr, k))
    print(KthLargestPriority(arr1, k))

def KthLargest(arr, k):
    arr.sort()
    answer = arr[len(arr) - k]
    return answer

#priority queue -> faster cause time complexity is 0(n) when k is near 0 
def KthLargestPriority(arr1, k):
    arr1 = [-elem for elem in arr1]
    heapq.heapify(arr1)

    for i in range(k-1):
        heapq.heappop(arr1)

    answer = -heapq.heappop(arr1)

    return answer

Main()