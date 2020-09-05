"""エイブラハム・リンカーンが実際に送ったルート暗号化されたメッセージ、

THIS OFF DETAINED ASCERTIN WAYLAND CORRESPONDENTS OF AT WHY AND IF
    FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEN CAN UP

をプログラムroute_cipher_decrypt.pyを使って復号する。

ただし、符号語の定義は以下の通りである.
WAYLAND -> cuptured
NEPTUNE -> Richmond

ANSWER:
Correpodents of the tribuen captured.
Please ascertin why ther are detained and get then off.
Can this fills it up?

「トリビューン新聞社が逮捕されたことが確認された。
彼らが拘留された理由を明らかにし、その後退避してください。
できそうですか？
"""

import sys

#==============================================================================
# ユーザー入力:

# 復号する文字列（三重の引用符で挟んでペーストするか手打ちする）:
ciphertext = """THIS OFF DETAINED ASCERTIN WAYLAND CORRESPONDENTS OF AT WHY \
AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEN CAN UP"""

# 転置表の列数:
COLS = 4

# 転置表の行数:
ROWS = 6

# 空白区切りの数の鍵、負の数は列を上方向に進む （例= -1 2 -3 4):
key = """ 4 -3 2 -1 """

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
試行１　６×４　左下
***********************************
とりあえず、適当なパラメータでコードを実行してみる

ーーーーーーーーーーーーーーーーーーーーー
$ python practice_route_cipher_decrypt.py

Ciphertext = THIS OFF DETAINED ASCERTIN WAYLAND CORRESPONDENTS OF AT WHY AND IF
FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEN CAN UP

Trying 4 columns

Trying 6 rows

Trying key =  -1 2 -3 4

Length of cipher = 24
Acceptable column/row values include: [2, 3, 4, 6, 8, 12]

Plaintext = CORRESPONDENTS OF THE TRIBUNE WAYLAND AT NEPTUNE PLEASE ASCERTIN
WHY THEY ARE DETAINED AND GET THEN OFF IF YOU CAN THIS FILLS IT UP
ーーーーーーーーーーーーーーーーーーーーー

ダミーの６行めの単語を除く、符号語を元の単語に戻す
 OF THE TRIBUNE cptured AT Richmond PLEASE ASCERTIN
WHY THEY  AND GET THEN OFF IF YOU CAN THIS FILLS IT

・　意味をなしていない
***********************************

試行２　６×４　左上
***********************************
とりうる行数は2, 3, 4, 6, 8, 12である
2, 3列の表を使うとは考えづらいので、現実的には4×６か６×４の配置を扱うことになる。
今回のような交互に連続した経路をとった場合の暗号文は、隣り合う結びつきのありそうな単語が
見られるはずである。4×６と６×４の２つの場合について隣り合う単語を「」で括る

・6×4
THIS OFF DETAINED ASCERTIN WAYLAND 「CORRESPONDENTS OF」 AT WHY AND IF
「FILLS IT」 YOU GET THEY NEPTUNE 「THE TRIBUNE」 PLEASE ARE THEN CAN UP

いずれも結びつきのありそうな単語である

・４×６
THIS OFF DETAINED 「ASCERTIN WAYLAND」 CORRESPONDENTS OF 「AT WHY」 AND IF
「FILLS IT」 YOU GET 「THEY NEPTUNE」 THE TRIBUNE 「PLEASE ARE」 THEN CAN UP

結びつきがありそうなのは、FILLS ITだけである

以上より、はじめに６×４の配置と仮定して、４通りの経路を試す。試行１で左下からの出発を既に
行っているので、試行２で左上、３で右下、４で右上からの出発を試す。

出力
-----------------------------------
$ python practice_route_cipher_decrypt.py

Ciphertext = THIS OFF DETAINED ASCERTIN WAYLAND CORRESPONDENTS OF AT WHY AND
IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEN CAN UP

Trying 4 columns

Trying 6 rows

Trying key =  1 -2 3 -4

Length of cipher = 24
Acceptable column/row values include: [2, 3, 4, 6, 8, 12]

Plaintext = THIS FILLS IT UP OFF IF YOU CAN DETAINED AND GET THEN ASCERTIN
WHY THEY ARE WAYLAND AT NEPTUNE PLEASE CORRESPONDENTS OF THE TRIBUNE
-----------------------------------

ダミーの６行めの単語を除く、符号語を元の単語に戻す
THIS FILLS IT UP OFF CAN DETAINED AND GET THEN ASCERTIN
WHY THEY ARE cuptured PLEASE CORRESPONDENTS OF THE TRIBUNE

意味はなさないし、重要であるはずの符号語が除かれている
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

試行２　６×４　右下:key = -4, 3, -2, 1
***********************************
-----------------------------------
$ python practice_route_cipher_decrypt.py

Ciphertext = THIS OFF DETAINED ASCERTIN WAYLAND CORRESPONDENTS OF AT WHY AND
IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEN CAN UP

Trying 4 columns

Trying 6 rows

Trying key =  -4 3 -2 1

Length of cipher = 24
Acceptable column/row values include: [2, 3, 4, 6, 8, 12]

Plaintext = TRIBUNE THE OF CORRESPONDENTS PLEASE NEPTUNE AT WAYLAND ARE THEY
 WHY ASCERTIN THEN GET AND DETAINED CAN YOU IF OFF UP IT FILLS THIS
-----------------------------------

ダミーの６行めの単語を除く、符号語を元の単語に戻す
THE OF CORRESPONDENTS PLEASE Richmond AT cuptured ARE THEY
 WHY GET AND DETAINED CAN YOU IF OFF UP IT FILLS

意味をなさない
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

試行２　６×４　右上:key = 4, -3, 2, -1
***********************************
-----------------------------------
$ python practice_route_cipher_decrypt.py

Ciphertext = THIS OFF DETAINED ASCERTIN WAYLAND CORRESPONDENTS OF AT WHY AND
IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEN CAN UP

Trying 4 columns

Trying 6 rows

Trying key =  4 -3 2 -1

Length of cipher = 24
Acceptable column/row values include: [2, 3, 4, 6, 8, 12]

Plaintext = "UP IT FILLS THIS CAN YOU IF OFF THEN GET AND DETAINED ARE THEY
 WHY ASCERTIN PLEASE NEPTUNE AT WAYLAND TRIBUNE THE OF CORRESPONDENTS"
-----------------------------------

逆にしてみる
' '.join(list(reversed(Plaintext.split()))) =
"CORRESPONDENTS OF THE TRIBUNE WAYLAND AT NEPTUNE PLEASE ASCERTIN WHY THEY ARE
DETAINED AND GET THEN OFF IF YOU CAN THIS FILLS IT UP"

意味が通りそうである

ダミーの６行めの単語を除く、符号語を元の単語に戻す
"CORRESPONDENTS OF THE TRIBUNE caputured PLEASE ASCERTIN WHY THEY ARE
DETAINED AND GET THEN OFF CAN THIS FILLS IT UP"

Correpodents of the tribuen captured.
Please ascertin why ther are detained and get then off.
Can this fills it up?

翻訳してみると、
「トリビューン新聞社が逮捕されたことが確認された。
彼らが拘留された理由を明らかにし、その後退避してください。
できそうですか？」

おそらくこれが暗号化前のメッセージであろう。

"""
