def binary_search(ar,key,low,high):
    if low >high:
        return -1
    else :
        mid =int((low+high)/2)
        if ar[mid]==key:
            return mid
        elif key>ar[mid]:
            low=mid+1
        else:
            high=mid-1
        binary_search(ar,key,low,high)
ar=[1,2,3,4,5,6,7,8,9]
key=int(input('Enter no.:'))
print(binary_search(ar,key,0,len(ar)-1))