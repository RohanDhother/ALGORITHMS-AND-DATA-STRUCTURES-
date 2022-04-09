import random
import time
def randomIntArray(s,n):
    array = []
    for i in range(s):
        array.append(random.randint(0,n))
    return array
def quickSort(A):
     quickSortRec(A,0,len(A))
def quickSortRec(A, lo, hi):
# sorts A[lo:hi]
     if hi-lo <= 1:
         return
     iPivot = partition(A,lo,hi)
     quickSortRec(A,lo,iPivot)
     quickSortRec(A,iPivot+1,hi)
def partition(A, lo, hi):
    pivot = A[lo]
    B = [0 for i in range(lo,hi)]
    loB = 0
    hiB = len(B)-1
    for i in range(lo+1,hi):
        if A[i] < pivot:
            B[loB] = A[i]
            loB += 1
        else:
            B[hiB] = A[i]
            hiB -= 1
    B[loB] = pivot
    for i in range(len(B)):
        A[lo+i] = B[i]
    return lo+loB
def sortTime(A):
    t = time.time()
    quickSort(A)
    t = time.time()-t
    return t
print("100: ", sortTime(randomIntArray(100,5)))
print("1000: ", sortTime(randomIntArray(1000,5)))
print("10000: ", sortTime(randomIntArray(10000,5)))
print("100000: ", sortTime(randomIntArray(100000,5)))
