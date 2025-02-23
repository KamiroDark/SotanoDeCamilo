def stones_colors(stones):
    remove_stones=0
    for i in range(1,len(stones)):
        if stones[i] == stones[i-1]:
            remove_stones +=1
    return remove_stones


n = int(input())
stones = input()
print(stones_colors(stones))
