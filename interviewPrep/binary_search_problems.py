def searchInsert(A, B):
    n = len(A)
    s = 0
    e = n-1
    while(s<=e):
        mid = s+(e-s//2)
        if A[mid] == B:
            print(mid)
            break
        elif A[mid] < B:
            s = mid+1
        else:
            e = mid-1
    print(s)
searchInsert(A=[1, 3, 5, 6],B=5)