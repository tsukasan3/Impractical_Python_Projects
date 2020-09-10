"""暗号文を読み込み、ETAOINの割合を使って暗号の種類を特定する。"""
import sys
from collections import Counter

# 英語で最も出てくる６文字の割合の閾値を任意に設定する
# 設定値以上だったら暗号文は転置式暗号だとみなす
CUTOFF = 0.5

# 暗号文を読み込む
def load(filename):
    """テキストファイルを開いてリストを返す。"""
    with open(filename) as f:
        return f.read().strip()


try:
    ciphertext = load("cipher_b.txt")
except IOError as e:
    print("{}. Terminating program.".format(e),
         file=sys.stderr)
    sys.exit(1)

# 最もよく出てくる６文字が暗号文にどれだけあるか数える
six_most_frequent = Counter(ciphertext.lower()).most_common(6)
print("\nSix most-frequently-used letters in English = ETAOIN")
print("\nSix most frequent used letters in ciphertext =")
print(*six_most_frequent, sep="\n")

# 比較のためタプルのリストを文字のセットに変換する
cipher_top_6 = [i[0] for i in six_most_frequent]

TARGET = "etaoin"
count = 0
for letter in TARGET:
    if letter in cipher_top_6:
        count += 1

if count/len(TARGET) >= CUTOFF:
    print("\nThis ciphertext most-likely produced by a TRANSPOSITION cipher")
else:
    print("\nThis ciphertext most-likely produced by a SUBSTITUTION cipher")

"""
cipher_a.txt
-------------------------
$ python identify_cipher_type_ans.py

Six most-frequently-used letters in English = ETAOIN

Six most frequent used letters in ciphertext =
('e', 165)
('t', 126)
('a', 102)
('o', 93)
('h', 80)
('r', 79)

This ciphertext most-likely produced by a TRANSPOSITION cipher
-------------------------

cipher_b.txt
-------------------------
$ python identify_cipher_type_ans.py

Six most-frequently-used letters in English = ETAOIN

Six most frequent used letters in ciphertext =
('g', 81)
('p', 77)
('c', 76)
('s', 61)
('r', 60)
('v', 60)

This ciphertext most-likely produced by a SUBSTITUTION cipher
-------------------------
"""
