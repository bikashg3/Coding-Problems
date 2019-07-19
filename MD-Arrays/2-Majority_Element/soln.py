#code
def majority(arr,n):
    majority_index = 0
    count = 1
    for i in range(1,n):
        if (arr[i]==arr[majority_index]):
            count += 1
        else:
            count -= 1
        if count == 0:
            majority_index = i
            count = 1
    # print("majority index is: ", majority_index)
    # print("count is: ", count)
    count = 0
    for i in range(0,n):
        if (arr[i] == arr[majority_index]):
            count += 1

    if (count > (n/2)):
            
        return arr[majority_index]
    else:
        return -1


t= int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split()))
    print(majority(arr,n))
    t = t-1
