import random

def hangman():
    print('Добро пожаловать в игру "Виселица"!')

    dict_words = {'цвет': ['красный', 'синий', 'жёлтый', 'зелёный'],
                  'работа': ['врач', 'столяр', 'учитель', 'продавец'],
                  'фигура': ['треугольник', 'круг', 'квадрат'],
                  'еда': ['бургер', 'макароны', 'суп', 'каша']}

    random_key = random.choice(list(dict_words))
    random_lists_v = dict_words.get(random_key)
    print(f'Вы угадываете слово в категории - {random_key}')

    magic_word = random.choice(random_lists_v)
    new_list = ['_' for _ in range(len(magic_word))]

    lst_mag_w = [char for char in magic_word if magic_word.count(char) == 1]
    el = random.choice(lst_mag_w)

    for i, k in enumerate(new_list):
        for j, v in enumerate(magic_word):
            if el == magic_word[j]:
                if i == j:
                    new_list[i] = el

    n = len(magic_word)
    print(f'Количество попыток на угадывание слова - {n}')

    counter = 0
    win_flag = True

    while win_flag:
        print('Ваше загаданное слово: ', *new_list)
        element = input(f"Ваша {counter+1} попытка: ")

        if magic_word.count(element) == 1:
            indx = magic_word.index(element)
            new_list[indx] = element
            counter += 1
            print(f'Ура, вы угадали букву {element}')

        elif magic_word.count(element) > 1:
            lst_ = []

            for i, v in enumerate(magic_word):
                if v == element:
                    lst_.append(i)

            for z in lst_:
                new_list[z] = magic_word[z]

            counter += 1
            print(f'Ура, вы угадали букву {element}')
        else:
            counter += 1
            print('Упс! Вы не угадали...')

        if '_' not in new_list:
            print(f'Поздравляем. Вы угадали слово - {magic_word}\U0001F917 Ураааа!!!')
            win_flag = False

        if counter == n:
            if new_list.count('_') != 0:
                print('К сожалению, вы проиграли. Количество попыток закончилось.. Вас повесили\U0001F62A')
                win_flag = False

hangman()