import random

def hangman(word):
    p = 'Да'
    while p == 'Да' or p =='да':
        print('Хочешь поиграть, напиши (да,нет)')
        p = input()
        if p == 'Да' or p == 'да':
            sttr  = ['собака','стол','кот','бык','дом','игра','веселица']
            r_n = random.randint(0,6)
            word = sttr[r_n]
            wrong = 0
            stages = ['',
                      '_________        ',
                      '|                ',
                      '|         |      ',
                      '|         0      ',
                      '|       / | \    ',
                      '|        / \     ',
                      '                 '
                      ]
            rletters = list(word)
            board = ['_'] * len(word)
            win = False
            print('Добро пожаловать на казнь!!!')
            while wrong < len(stages) - 1:
                print('\n')
                msg = 'Введите букву: '
                char = input(msg)
                if char in rletters:
                    cind = rletters.index(char)
                    board[cind] = char
                    rletters[cind] = '$'
                else:
                    wrong += 1
                print(('_'.join(board)))
                e = wrong + 1
                print('\n'.join(stages[0: e]))
                if '_' not in  board:
                    print('Вы выиграли! Было загадано слово: ')
                    print(''.join(board))
                    win = True
                    break
            if not win:
                print('\n'.join(stages[0: wrong]))
                print('Вы проиграли! Было загадано слово: {}.'.format(word))


sttr  = ['собака','стол','кот','бык','дом','игра','веселица']

hangman('кот')
