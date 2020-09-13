"""北軍のルート暗号の経路を総当たりで復号する

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

必要な入力　ー　テキストメッセージ、列数、行数
鍵を生成するのに自作の"perms"モジュールが必要
使った鍵と変換後の平文を表示する
"""
import sys
import perms

#==========================================================================
# ユーザー入力：

# 復号する文字列（三重の引用符で挟んで手入力かペーストする）：
ciphertext = """REST TRANSPORT YOU GODWIN VILLAGE ROANOKE WITH
ARE YOUR IS JUST SUPPLIES FREE SNOW HEADING TO GONE TO SOUTH FILLER"""

# 転置表の列数
COLS = 4

# 転置表の行数
ROWS = 5

# ユーザーの入力終わり　ー　この行より下は編集しないこと
#==========================================================================

def main():
    """暗号文をリストに変換し、検証・復号の関数を呼び出す"""
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    decrypt(cipherlist)


def validate_col_row(cipherlist):
    """入力した列数と行数をメッセージの長さに対してチェックする"""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):
        if len_cipher % i == 0:
            factors.append(i)
    print("\nLength of cipher = {}".format(len_cipher))
    print("Acceptable column/row values include: {}".format(factors))
    print()
    if ROWS * COLS != len_cipher:
        print("\nError - Input columns & rows not factors of length "
              "of cipher. Terminating program.", file=sys.stderr)
        sys.exit(1)


def decrypt(cipherlist):
    """列をリストのリストの要素に変換し、暗号文を復号する"""
    col_combos = perms.perms(COLS)
    for key in col_combos:
        translation_matrix = [None] * COLS
        plaintext = ""
        start = 0
        stop = ROWS
        for k in key:
            if k < 0:   # 列を下から上に読む
                col_items = cipherlist[start:stop]
            elif k > 0: # 列を上から下に読む
                col_items = list(reversed(cipherlist[start:stop]))
            translation_matrix[abs(k) - 1] = col_items
            start += ROWS
            stop += ROWS

        for i in range(ROWS):
            for matrix_col in translation_matrix:
                word = str(matrix_col.pop())
                plaintext += word + " "

        print("\n使用する鍵 = {}".format(key))
        print("変換結果 = {}".format(plaintext))

    print("\n鍵の数 = {}".format(len(col_combos)))


if __name__ == "__main__":
    main()
