def main():
    
    n, k, e = map(int, input().split())
    
    
    l = e
    r = n - k - e
    
    
    dp = [[False] * (r + 1) for _ in range(l + 1)]
    
    
    dp[0][0] = True
    
    
    for length in range(1, n + 1):
        if length != k:  
            for i in range(l, -1, -1):
                for j in range(r, -1, -1):
                    if length <= i:
                        dp[i][j] |= dp[i - length][j]
                    if length <= j:
                        dp[i][j] |= dp[i][j - length]
    
    ans = k  
    for i in range(l + 1):
        for j in range(r + 1):
            if dp[i][j]:
                ans = max(ans, i + j + k)
    
    print(n - ans)

if __name__ == "__main__":
    main()