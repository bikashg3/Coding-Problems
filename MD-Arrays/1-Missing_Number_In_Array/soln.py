
def FindMissNum(arr,n):
    sum_n = n*(n+1)/2
    arr_sum = sum(arr)
    return int(sum_n-arr_sum)

t = int(input())

while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    print(FindMissNum(arr,n))
    t=t-1
    
