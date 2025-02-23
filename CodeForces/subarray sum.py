def max_array(arr):

    max_far = 0
    max_here = 0

    for i in range(1, len(arr)):
        max_here = max(arr[i], max_here + arr[i])
        max_far = max(max_far, max_here)

    return max_far

    
n = int(input()) 
arr = list(map(int, input().split()))
print(max_array(arr))