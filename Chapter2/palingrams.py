"""辞書ファイルにある単語のペアの回文をすべて見つける。"""
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

# 単語のペアの回文を見つける
def find_palingrams():
    """辞書の回文をみつける"""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))

    return pali_list

palingrams = find_palingrams()

palingrams_sorted = sorted(palingrams)

# 回文のリストを表示する
print('\nNumber of palingrams = {}'.format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print('{} {}'.format(first, second))
