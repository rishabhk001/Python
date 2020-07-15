def isSorted(A):
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isSorted(A[ 1:])
A= [1271,220, 246, 277, 321, 454, 534, 565, 933]
print(isSorted(A)) 
