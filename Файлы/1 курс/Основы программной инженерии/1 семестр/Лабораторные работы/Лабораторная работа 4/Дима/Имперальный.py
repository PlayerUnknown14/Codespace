# Вариант с библиотеками


# from random import randint
# import os
# words = []
# with open ('slovar.txt', encoding='utf-8') as t:
#     lines = t.readlines()
#     for line in lines:
#         words.append(line.strip().split(' -'))
# #Общий цикл, в котором будут задаваться слова
# while True:
#     action = input('Введите (1) для начала игры, (0) для полного выхода из игры\nВвод: ')
#     os.system('cls')
#     match action.split():
#         case['1']:
#             worddef = words[randint(0,len(words)-1)]
#             word = worddef[0]
#             definition = worddef[1]
#             wordmass = []
#             wordgame = []

#             for letter in word:
#                 wordmass.append(letter)

#             for i in range(len(wordmass)):
#                 wordgame.append('*')
# #Цикл для слова. Содержит процесс игры
#             while True:
#                 print('-----------------Определение слова-----------------')
#                 print(definition)
#                 print('---------------------------------------------------')
#                 print(wordgame)
#                 letter = input('Введите букву: ')
#                 os.system('cls')

#                 if letter in wordmass:
#                     os.system('cls')
#                     print('Такая буква есть')
#                     for i in range(len(wordmass)):
#                         if letter == wordmass[i]:
#                             wordgame[i] = letter

#                 else:
#                     os.system('cls')
#                     print('Такой буквы нет')
#                 if wordgame == wordmass:
#                     os.system('cls')
#                     print('Слово: ', word)
#                     print('------------')
#                     print('Вы победили')
#                     print('------------')
#                     break
#         case['0']:
#             print('Вы вышли из игры')
#             break

#Вариант без библиотек

words = []
with open ('slovar.txt', encoding='utf-8') as t:
    lines = t.readlines()
    for line in lines:
        words.append(line.strip().split(' -'))
#Общий цикл, в котором будут задаваться слова
while True:
    action = input('Введите (1) для начала игры, (0) для полного выхода из игры\nВвод: ')
    match action.split():
        case['1']:
            index = int(input('Введите число от 0 до 999\nВвод: '))
            worddef = words[index]
            word = worddef[0]
            definition = worddef[1]
            wordmass = []
            wordgame = []

            for letter in word:
                wordmass.append(letter)

            for i in range(len(wordmass)):
                wordgame.append('*')
#Цикл для слова. Содержит процесс игры
            while True:
                print('-----------------Определение слова-----------------')
                print(definition)
                print('---------------------------------------------------')
                print(wordgame)
                letter = input('Введите букву: ')

                if letter in wordmass:
                    print('Такая буква есть')
                    for i in range(len(wordmass)):
                        if letter == wordmass[i]:
                            wordgame[i] = letter

                else:
                    print('Такой буквы нет')
                if wordgame == wordmass:
                    print('Слово: ', word)
                    print('------------')
                    print('Вы победили')
                    print('------------')
                    break
        case['0']:
            print('Вы вышли из игры')
            break

