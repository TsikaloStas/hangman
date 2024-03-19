import random
from catchwords import dict_words

def hangman():
    print('Welcome to the Hangman game!')

    # select a random category from the dictionary
    random_key = random.choice(list(dict_words))

    # generate a list of words from this category
    list_magic_words = dict_words.get(random_key)
    print(f'Your word from the category - {random_key}')

    # choose a magic word
    magic_word = random.choice(list_magic_words)
    enigma_word = ['_' for _ in range(len(magic_word))]

    # pick a random open letter
    random_letter = [char for char in magic_word if magic_word.count(char) == 1]
    el = random.choice(random_letter)

    # replace an empty value in the riddle word with an open letter
    for i, k in enumerate(enigma_word):
        for j, v in enumerate(magic_word):
            if el == magic_word[j]:
                if i == j:
                    enigma_word[i] = el

    n = len(magic_word)
    print(f'Number of attempts to guess a word - {n}')

    # tally counter
    counter = 0
    win_flag = True

    while win_flag:
        print('Your target word: ', *enigma_word)
        element = input(f"Your {counter+1} attempt: ")

        # if letters in the word = 1, find the index and replace the letter by position
        if magic_word.count(element) == 1:
            index = magic_word.index(element)
            enigma_word[index] = element
            counter += 1
            print(f'Yay, you guessed the letter {element}')

        # if letters in the word > 1, find all indexes of such letter and write them to the list
        elif magic_word.count(element) > 1:
            index_list = []

            for i, v in enumerate(magic_word):
                if v == element:
                    index_list.append(i)

            for z in index_list:
                enigma_word[z] = magic_word[z]

            counter += 1
            print(f'Yay, you guessed the letter {element}')

        else:
            counter += 1
            print('Oops! You guessed wrong.....')

        # if there are no blanks left in the riddled word - report victory
        if '_' not in enigma_word:
            print(f'Congratulations. You guessed the word - {magic_word}\U0001F917 Yay!!!')
            win_flag = False

        # prescribe a situation where we guess a word on the last try
        if counter == n:
            if enigma_word.count('_') != 0:
                print('Unfortunately, you\'ve lost. The number of attempts has expired.. You have been hanged\U0001F62A')
                win_flag = False

hangman()