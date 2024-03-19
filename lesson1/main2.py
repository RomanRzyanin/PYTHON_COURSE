# My first game
import random
res = True
while res:
    x = random.randint(0, 100)
    print(x)
    while res:
        print('Добрый день игрок! Угадайте число')
        answer = int(input('Введите ваш ответ: '))
        if answer > x:
            print('Слишком много, поробуйте еще.\n')
        elif answer < x:
            print('Слишком мало, поробуйте еще.\n')
        elif answer == x:
            print(f'Правильно! Ответ = {x}\n')
            res = False
    game = input('Хотите сыграть еще, да/нет:')
    if game == 'да':
        res = True
    else:
        print('До свидания')
        res = False