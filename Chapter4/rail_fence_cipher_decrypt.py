r"""南北戦争の「レールフェンス」型暗号を復号する。
これは短いメッセージの「2レール」フェンス暗号のためのものである。
暗号化するテキストの例：「Buy more Maine potates」
レールフェンススタイル：B Y O E A N P T T E
                     U M R M I E O A O S
ジグザグに読む：       \/\/\/\/\/\/\/\/\/\
暗号化後：BYOEA NPTTE UMRMI EOAOS
"""

import math
import itertools

#----------------------------------------------------------------------------
# ユーザー入力：

# 復号する文字列（引用符の間に貼り付ける）：
ciphertext = """LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES"""

# ユーザー入力の終わり - この行より下は編集しないこと！
#----------------------------------------------------------------------------



def main():
    """2レールのレールフェンス暗号を復号するプログラムを実行する。"""
    message = prep_ciphertext(ciphertext)
    row1, row2 = split_rails(message)
    decrypt(row1, row2)

def prep_ciphertext(ciphertext):
    """空白を取り除く。"""
    message = ''.join(ciphertext.split())
    print("\nciphertext = {}".format(ciphertext))
    return message

def split_rails(message):
    """メッセージを2つに分割し、常に１つ目の行に切り上げる"""
    row_1_len = math.ceil(len(message)/2)
    row1 = message[:row_1_len].lower()
    row2 = message[row_1_len:].lower()
    return row1, row2

def decrypt(row1, row2):
    """2つの文字列から交互に文字をとってリストを作り、表示する。"""
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1)
        plaintext.append(r2)
    if None in plaintext:
        plaintext.pop()

    print("\nrail 1 = {}".format(row1))
    print("\nrail 2 = {}".format(row2))
    print("\nplaintext = {}".format(''.join(plaintext)))


if __name__ == '__main__':
    main()


"""
出力結果
ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
$ python rail_fence_cipher_decrypt.py

ciphertext = LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES

rail 1 = ltsrsoeteieadetnetehdotere

rail 2 = eucosvrhrvrnrsudrhsaefhtes

plaintext = letuscrossovertheriverandrestundertheshadeofthetrees
"""
