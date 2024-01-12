#find missing number from the list
def missing_num():
    x = [1, 2, 4, 5, 6, 7]
    n = x[-1]
    summation = n*(n+1)//2
    missnig = summation-sum(x)
    print(missnig)
missing_num()

#