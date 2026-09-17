


def binary_search(arr,target):

    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = (start+end)//2
        if(target==arr[mid]):
            return (f"element {arr[mid]} found in posintion {mid+1}")
        elif(target<arr[mid]):
            end = mid-1
        elif(target>arr[mid]):
            start = mid+1
    return "Element NOT found"

status = binary_search([1,4,6,7,8,9,14,55,66,78,98],8)

print(status)