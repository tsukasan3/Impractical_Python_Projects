import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

# アナグラムを保持する空のリストを作る
anagram_list = []

# アナグラムを見つけるために、単語や名前を入力する
name = input('Input name is\n')
name = name.lower()
print('Using name is {}'.format(name))

# name をソートしてアナグラムを見つける
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

if len(anagram_list) == 0:
    print('You need a larger dictionary or a new name!')
else:
    print('Anagrams =', *anagram_list, sep='\n')
