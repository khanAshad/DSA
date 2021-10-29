def lsearch(arr,n,key):
    i = 0
    while(i<n):
        if arr[i]==key:
            return i+1
        i=i+1
    return -1
n=int(input("Enter size of array "))
arr=list(map(int,input("Enter the array: ").split()))
key=int(input("Enter element to search "))
print(lsearch(arr,n,key))