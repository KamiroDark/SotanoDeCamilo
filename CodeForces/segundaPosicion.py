def find_w(n, c, sizes):
    left, right = 1, 10**9  
    while left < right:
        mid = (left + right) // 2
        total_area = sum((s + 2 * mid) ** 2 for s in sizes)
        if total_area == c:
            return mid
        elif total_area < c:
            left = mid + 1
        else:
            right = mid
    return left


t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    sizes = list(map(int, input().split()))
    print(find_w(n, c, sizes))