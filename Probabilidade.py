import random

def roll_dice():
    return random.randint(1, 6)

def probability_of_rolling_number(num, num_rolls):
    count = 0
    for i in range(num_rolls):
        if roll_dice() == num:
            count += 1
    return count / num_rolls

# Exemplo: qual é a probabilidade de obter o número 4 em 50 jogadas do dado?
print(probability_of_rolling_number(4, 50))
