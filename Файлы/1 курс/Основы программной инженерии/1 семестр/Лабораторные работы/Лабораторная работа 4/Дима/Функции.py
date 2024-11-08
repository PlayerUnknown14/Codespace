def check():
    # Функция проверки вводимых данных
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
    match action.split():
        case['1']:
            index = check()
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

