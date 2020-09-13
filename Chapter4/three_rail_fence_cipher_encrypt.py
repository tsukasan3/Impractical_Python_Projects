r"""南北戦争の「レールフェンス」型暗号を暗号化する。
これは短いメッセージの「3 レール」フェンス暗号のためのものである。
暗号化するテキストの例：「Buy more Maine potatoes」
レールフェンススタイル：B   O   A   P   T
                     U M R M I E O A O S
                      Y   E   N   T   E
ジグザグに読む：       \  /\  /\  /\  /\
                     \/  \/  \/  \/  \/
暗号化後：BOAPT UMRMI EOAOS YENTE
"""

#----------------------------------------------------------------------------
# ユーザー入力：

# 暗号化する文字列（引用符の間に貼り付ける）：
plaintext = """Let us cross over the river and rest under the shade of
the trees"""

# ユーザー入力の終わり - この行より下は編集しないこと！
#----------------------------------------------------------------------------




def main():
    """3 レールのレールフェンス暗号でメッセージを暗号化するプログラムを実行する"""
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
    """メッセージの文字を
    1,3レールでは4文字ごとに
    2レールでは２文字ごとに取得して、その後文字列を連結する"""
    rail1 = message[::4]
    rail2 = message[1::2]
    rail3 = message[2::4]
    rails = rail1 + rail2 + rail3
    return rails

def encrypt(rails):
    """暗号文の文字を５個ずつの塊にして、文字列を作る"""
    ciphertext = ' '.join(rails[i:i+5] for i in range(0, len(rails), 5))
    print("\nciphertext = {}".format(ciphertext))

if __name__ == "__main__":
    main()


"""
出力
ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
$ python three_rail_fence_cipher_encrypt.py

plaintext = Let us cross over the river and rest under the shade of
the trees

ciphertext = LSSEE EDTEE DTREU COSVR HRVRN RSUDR HSAEF HTEST ROTIA ENTHO EE
"""
