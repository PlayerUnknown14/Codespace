#Имперальный с системой жизни и сохранением введённых букв
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
            index = int(input('\nВведите число от 0 до 999\nВвод: '))
            worddef = words[index]
            word = worddef[0]
            definition = worddef[1]
            wordmass = []
            wordgame = []

            life = 10
            massletters = []


            for letter in word:
                wordmass.append(letter)

            for i in range(len(wordmass)):
                wordgame.append('*')
#Цикл для слова. Содержит процесс игры
            while True:
                print('\n-----------------Определение слова-----------------')
                print(definition)
                print('---------------------------------------------------\n')
                print(wordgame)
                print('Количество жизней: ', life)
                letter = input('\nВведите букву: ')

                if letter in massletters:
                    print('Такая буква уже была введена.')
                    life -= 1
                    print('Количество жизней: ',life)
                elif letter in wordmass:
                    print('Такая буква есть')
                    for i in range(len(wordmass)):
                        if letter == wordmass[i]:
                            wordgame[i] = letter

                else:
                    life -= 1
                    print('Количество жизней: ',life)
                    print('Такой буквы нет')
                    
                massletters.append(letter)

                if wordgame == wordmass:
                    print('\nСлово: ', word)
                    print('------------')
                    print('Вы победили')
                    print('------------')
                    break
                if life == 0:
                    print('Вы проиграли\n')
                    break
        case['0']:
            print('Вы вышли из игры')
            break

