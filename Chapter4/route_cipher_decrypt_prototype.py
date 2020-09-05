ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

#  要素を文字ごとではなく単語ごとに分割する
ciphertext = list(ciphertext.split())

# 変数の初期化
COLS = 4
ROWS = 5
key = '-1 2 -3 4' # 負の数は列を下から上に読むことを表す
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

# key を整数のリストにする
key_int = [int(i) for i in key.split()]

# 列をリストのリストにする
for k in key_int:
    if k < 0:
        col_items = ciphertext[start:stop]
    elif k > 0:
        col_items = list(reversed(ciphertext[start:stop]))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS

print('\nciphertext = {}'.format(ciphertext))
print('\ntranslation_matrix = {}'.format(translation_matrix))
print('\nkey length = {}'.format(len(key_int)))

# 入れ子になったリストをループし、pop()メソッドを使って最後の要素を削除して取り出す
for i in range(ROWS):
    for col_items in translation_matrix:
        word = col_items.pop()
        plaintext += word + ' '

print('\nplaintext = {}'.format(plaintext))         
