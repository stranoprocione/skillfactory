import numpy as np

try_count = 0  # attempt counter
print("Загадано число от 1 до 100")


def game_core(number):
    """Set random number and border for it. Every iteration change border"""
    try_count = 1
    predict = np.random.randint(1, 101)
    over_number = 101
    less_number = 1

    while number != predict:
        try_count += 1
        if number > predict:
            less_number = predict
        elif number < predict:
            over_number = predict
        predict = np.random.randint(less_number, over_number)

    return try_count  # break if guess


def score_game(core):
    """To know how quickly the program guess answer run the game 1000 times"""
    count_ls = []
    np.random.seed(1)  # fix RANDOM SEED for reproducible experiment!
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return score


# Check
score_game(game_core)

