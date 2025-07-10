def print_numbers(word_1, word_2) -> int:
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(word_1 + word_2)
        elif i % 5 == 0:
            print(word_2)
        elif i % 3 == 0:
            print(word_1)
        else:
            print(i)
            count += 1
    return count

print(print_numbers("Texto 1","Texto 2"))
