from random import randint
import os
class Game():
    # Функция проверки вводимых данных
    def check():
        while True:
            try:
                index = int(input('Введите число от 0 до 999\nВвод:  '))
                testmass = ['*']*999
                testword = testmass[index]
                break
            except TypeError:
                print('Вы ввели символ неверного типа')
            except ValueError:
                print('Число введено неверно')
            except NameError:
                print('Тип введённых символов не подходит')
            except IndexError:
                print('Число не входит в промежуток [0;999]')
        return index


    words = []
    with open ('slovar.txt', encoding='utf-8') as t:
        lines = t.readlines()
        for line in lines:
            words.append(line.strip().split(' -'))
    #Общий цикл, в котором будут задаваться слова
    while True:
        action = input('Введите (1) для начала игры, (0) для полного выхода из игры\nВвод: ')
        os.system('cls')
        match action.split():
            case['1']:
                worddef = words[randint(0,len(words)-1)]
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
                    os.system('cls')

                    if letter in wordmass:
                        os.system('cls')
                        print('Такая буква есть')
                        for i in range(len(wordmass)):
                            if letter == wordmass[i]:
                                wordgame[i] = letter

                    else:
                        os.system('cls')
                        print('Такой буквы нет')
                    if wordgame == wordmass:
                        os.system('cls')
                        print('Слово: ', word)
                        print('------------')
                        print('Вы победили')
                        print('------------')
                        break
            case['0']:
                print('Вы вышли из игры')
                break
        