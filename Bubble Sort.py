def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for k in range(i):
            if nums[k]>nums[k+1]:
                temp=num[k]
                num[k]=num[k+1]
                num[k+1]=temp



num=[5,6,3,2,1,8,9,7,4]
sort(num)
print(num)