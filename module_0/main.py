#!/usr/bin/env python3
import numpy as np

def game_core_v2(number): 
    count = 0
    left, right = 1, 100
    while True:
        count += 1
        value = left + (right - left) // 2
        if value == number: 
            return count
        if value > number: 
            right = value - 1

        if value < number: 
            left = value + 1

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
        Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
      count+=1
      predict = np.random.randint(1,101) # предполагаемое число
      if number == predict: 
          return(count) # выход из цикла, если угадали
      
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!  
    np.random.seed(1)  
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


if __name__ == "__main__":
    score_game(game_core_v2)
