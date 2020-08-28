"""辞書ファイルにある単語のペアの回文をすべて見つける。"""
import load_dictionary
import time

start_time = time.time()
word_list = load_dictionary.load('2of4brif.txt')

# 単語のペアの回文を見つける
def find_palingrams():
    """辞書の回文をみつける"""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))

    return pali_list

start_time = time.time()
palingrams = find_palingrams()
end_time = time.time()

palingrams_sorted = sorted(palingrams)

# 回文のリストを表示する
print('\nNumber of palingrams = {}'.format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print('{} {}'.format(first, second))


print('Runtime for this program was {} seconds.'.format(end_time - start_time))
