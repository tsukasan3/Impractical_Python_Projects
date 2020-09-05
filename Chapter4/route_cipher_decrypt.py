"""北軍のルート暗号の経路を復号する

行数や列数が異なる単語単位の転置式暗号のためにデザインされている。
暗号化は列の上端か下端から始まることを想定している。
鍵が、読む列の順序や進む方向を示す。
負の列番号は下端から上に進むことを示す。
正の列番号は上端から下に進むことを示す。
以下の例は4x4の行列で、鍵が -1 2 -3 4になっている。
「０」は許容されないことに注意する。
矢印は暗号化の経路を示しており、負の値は上方向に進む。

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | メッセージは
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | 各行にまたがり
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | このように書かれる
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | 最後の行はダミーの単語で埋める
|_|_|_v_|_|_|_v_|
START        END

必要な入力　ー　テキストメッセージ、列数、行数、鍵の文字列

変換後の平文を表示する
"""
import sys

#==============================================================================
# ユーザー入力:

# 復号する文字列（三重の引用符で挟んでペーストするか手打ちする）:
ciphertext = """16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19
"""

# 転置表の列数:
COLS = 4

# 転置表の行数:
ROWS = 5

# 空白区切りの数の鍵、負の数は列を上方向に進む （例= -1 2 -3 4):
key = """ -1 2 -3 4 """

# ユーザー入力の終わり　ー　この行より下は編集しないこと!
#==============================================================================





def main():
    """プログラムを実行して復号した平文を表示する"""
    print('\nCiphertext = {}'.format(ciphertext))
    print('\nTrying {} columns'.format(COLS))
    print('\nTrying {} rows'.format(ROWS))
    print('\nTrying key = {}'.format(key))

    # 要素を文字ごとではなく単語ごとに分割する
    cipherlist = list(ciphertext.split())

    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print("Plaintext = {}".format(plaintext))

def validate_col_row(cipherlist):
    """入力した列数と行数をメッセージの長さに対してチェックする。"""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher): # 1列の暗号は除外する
        if len_cipher % i == 0:
            factors.append(i)
    print("\nLength of cipher = {}".format(len_cipher))
    print("Acceptable column/row values include: {}".format(factors))
    print()
    if ROWS * COLS != len_cipher:
        print("\nError - Input columns & rows not factors of length "
              "of cipher. Terminating program.", file=sys.stderr)
        sys.exit(1)

def key_to_int(key):
    """鍵を整数のリストにして妥当性をチェックする。"""
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
        or 0 in key_int:
        print("\Error - Problem with key. Terminating.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int

def build_matrix(key_int, cipherlist):
    """リストのn要素ごとに、リストのリストにいれる。"""
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for k in key_int:
        if k < 0:
            col_items = cipherlist[start:stop]
        elif k > 0:
            col_items = list(reversed(cipherlist[start:stop]))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix

def decrypt(translation_matrix):
    """入れ子のリストをループし、最後の要素を取り出して文字列にする"""
    plaintext = ''
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = matrix_col.pop()
            plaintext += word + ' '
    return plaintext

if __name__ == '__main__':
    main()


"""
出力結果
ーーーーーーーーーーーーーーーーーーーーー
$ python route_cipher_decrypt.py

Ciphertext = 16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19


Trying 4 columns

Trying 5 rows

Trying key =  -1 2 -3 4

Length of cipher = 20
Acceptable column/row values include: [2, 4, 5, 10]

Plaintext = 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
"""
