from collections import defaultdict, deque

def determine_order(words):

    graph = defaultdict(set)
    in_degree = defaultdict(int)
    all_chars = set()

    for word in word:
        for char in word:
            all_chars.add(char)

    for i in range(len(words)-1):
        word1, word2 = words[i], words[i+1]
        min_length = min(len(word1), len(word2))
        for j in range(min_length):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
    queue = deque([char for char in all_chars if in_degree[char] == 0])
    order = []
    
    while queue:
        char = queue.popleft()
        order.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Verificar si se encontró un orden válido
    if len(order) == len(all_chars):
        return "".join(order)
    else:
        return "There is a cycle, no valid order."

words = []
while True:
    word = input().strip()
    if word == "#":
        break
    words.append(word)

# Determinar el orden y mostrar la salida
print(determine_order(words))        