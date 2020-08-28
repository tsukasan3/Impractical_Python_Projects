"""リストにある一文字の単語はaかeでなければ削除する"""

word_list = ['stick', 'odd', 'b', 'g', 'a', 'e']
word_cleanup_list = []

permissible = ('a', 'e')

# 一文字の単語はaかeでなければ削除する
for word in word_list:
    if len(word) > 1:
        word_cleanup_list.append(word)
    elif len(word) == 1 and word in permissible:
        word_cleanup_list.append(word)
    else:
        continue

print(word_list, '\n')
print(word_cleanup_list)
