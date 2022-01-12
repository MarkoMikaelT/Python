#Finding the first and last index in a sorted array
#if indexes cant be found return [-1, -1]

exampleArr = [1, 2, 3, 3, 3, 3, 3, 4]
exampleTarget = 3

def main():
    result = IndexFirstAndLast(exampleArr, exampleTarget)
    print(result)

    result1 = FirstAndLast(exampleArr, exampleTarget)
    print(result1)



def IndexFirstAndLast(exampleArr, exampleTarget):

    for i in range(len(exampleArr)):
        if exampleArr[i] == exampleTarget:
            firstIndex = i
            while i+1 < len(exampleArr) and exampleArr[i+1] == exampleTarget:
                i += 1
            return [firstIndex, i]

    return [-1, -1]

#binary search
def FindStart(exampleArr, exampleTarget):
    if exampleArr[0] == 0:
        return 0

    left, right = 0, len(exampleArr)-1

    while left <= right:
        mid = left + (right - left) // 2 

        if exampleArr[mid] == exampleTarget and exampleArr[mid-1] < exampleTarget:
            return mid
        elif exampleArr[mid] < exampleTarget:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def FindEnd(exampleArr, exampleTarget):
    if exampleArr[-1] == exampleTarget:
        return len(exampleArr)-1

    left, right = 0, len(exampleArr)-1

    while left <= right:
        mid = left + (right - left) // 2

        if exampleArr[mid] == exampleTarget and exampleArr[mid+1] > exampleTarget:
            return mid 
        elif exampleArr[mid] < exampleTarget:
            right = mid - 1
        else: 
            left = mid + 1 

    return -1

def FirstAndLast(exampleArr, exampleTarget):
    if len(exampleArr) == 0 or exampleArr[0] > exampleTarget or exampleArr[-1] < exampleTarget:
        return [-1, -1]
    first = FindStart(exampleArr, exampleTarget)
    last = FindEnd(exampleArr, exampleTarget)

    return [first, last]

main()