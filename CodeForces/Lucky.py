def lucky():
    t = int(input())

    for i in range(t):
        ticket = input()
        primera_mitad = sum(map(int, ticket[:3]))
        segunda_mitad = sum(map(int, ticket[3:]))
        if primera_mitad == segunda_mitad:
            print("YES")
        else:
            print("NO")
