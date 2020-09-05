r"""南北戦争の「レールフェンス」型暗号を暗号化する。
これは短いメッセージの「２ レール」フェンス暗号のためのものである。
暗号化するテキストの例：「Buy more Maine potatoes」
レールフェンススタイル：B Y O E A N P T T E
                     U M R M I E O A O S
ジグザグに読む：       \/\/\/\/\/\/\/\/\/\
暗号化後：BYOEA NPTTE UMRMI EOAOS
"""

#----------------------------------------------------------------------------
# ユーザー入力：

# 暗号化する文字列（引用符の間に貼り付ける）：
plaintext = """Let us cross over the river and rest under the shade of
the trees"""

# ユーザー入力の終わり - この行より下は編集しないこと！
#----------------------------------------------------------------------------




def main():
    """2 レールのレールフェンス暗号でメッセージを暗号化するプログラムを実行する"""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)

def prep_plaintext(plaintext):
    """plaintext内の空白を取り除き、文字をすべて大文字にする"""
    message = ''.join(plaintext.split())
    message = message.upper()
    print('\nplaintext = {}'.format(plaintext))
    return message

def build_rails(message):
    """メッセージの文字を交互に使って文字列を作る"""
    evens  = message[::2]
    odds = message[1::2]
    rails = evens + odds
    return rails

def encrypt(rails):
    """暗号文の文字を５個ずつの塊にして、文字列を作る"""
    ciphertext = ' '.join(rails[i:i+5] for i in range(0, len(rails), 5))
    print("\nciphertext = {}".format(ciphertext))

if __name__ == "__main__":
    main

"""
出力結果
ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
$ python rail_fence_cipher_encrypt.py

plaintext = Let us cross over the river and rest under the shade of
the trees

ciphertext = LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES
"""
