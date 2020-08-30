"""
wordsmith(https://wordsmith.org/anagram/)の
自動アナグラムジェネレータを真似たPythonプログラムを書く(未完)
"""

import sys
from collections import Counter
import load_dictionary

def main():
    ini_name = input('Enter a name: ')
    dict_file = load_dictionary.load('2of4brif.txt')
    dict_file.append('a')
    dict_file.append('I')
    ini_word_list = dict_file

    name = ''.join(ini_name.lower().split())
    name = name.replace('-', '')
    phrase = ''
    ini_name_anagrams = []
    not_ini_anagrams = []

    for i in range(10000):
        ini_anagram = ''
        ini_anagram = create_anagram_list(name, phrase, dict_file, ini_name_anagrams, ini_anagram, ini_word_list, not_ini_anagrams)
        if ini_anagram != '' and ini_anagram in ini_word_list:
            ini_word_list.remove(ini_anagram)
        print(ini_name_anagrams)
    print(ini_name_anagrams[:500])

def find_ini_anagram(name, word_list, not_ini_anagrams):
    name_letter_map = Counter(name)

    for word in word_list:
        if word not in not_ini_anagrams:
            test = ''
            word = word.lower()
            word_letter_map = Counter(word)
            for letter in word:
                if word_letter_map[letter] <= name_letter_map[letter]:
                    test += letter
            if Counter(test) == word_letter_map:
                anagram = word
                return anagram

def find_anagram(name, word_list):
    name_letter_map = Counter(name)

    for word in word_list:
        test = ''
        word = word.lower()
        word_letter_map = Counter(word)
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagram = word
            return anagram


def get_nameleft_phrase(name, phrase, anagram):
    left_over_list = list(name)

    for letter in anagram:
        left_over_list.remove(letter)
    name = ''.join(left_over_list)
    phrase += anagram + ' '

    return name, phrase


def create_anagram_list(name, phrase, word_list, ini_name_anagrams, ini_anagram, ini_word_list, not_ini_anagrams):
    if name != '':
        if ini_anagram == '':
            ini_anagram = find_ini_anagram(name, ini_word_list, not_ini_anagrams)
            anagram = ini_anagram
        else:
            anagram = find_anagram(name, word_list)
        if anagram != None:
            name, phrase = get_nameleft_phrase(name, phrase, anagram)
            return create_anagram_list(name, phrase, word_list, ini_name_anagrams, ini_anagram, ini_word_list, not_ini_anagrams)
        elif anagram == None:
            first_word = phrase.split()[0]
            not_ini_anagrams.append(first_word)
            return ''

    elif name == '':
        first_word = phrase.split()[0]
        not_ini_anagrams.append(first_word)
        ini_name_anagrams.append(phrase.title().rstrip())
        return ini_anagram


if __name__ == '__main__':
    main()
