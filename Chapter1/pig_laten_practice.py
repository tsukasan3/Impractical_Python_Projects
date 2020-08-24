"""入力した英単語をピッグラテン（なんちゃってラテン語）に変換して返す"""

def pig_laten():
    """入力した英単語をピッグラテン（なんちゃってラテン語）に変換して返す"""
    while True:
        word = input()
        # 母音で始まる単語の場合
        if word[0] in ['a', 'e', 'i', 'u', 'o']:
            # 単語の最後に「way」 をたす
            word += 'way'
            print(word)
        # 子音で始まる単語の場合
        else:
            # 先頭の子音を末尾に移動し、「ay」 を単語の最後に足す
            word = word[1:] + word[0] + 'ay'
            print(word)

        try_again = input('\n\nTry again? (Press Enter else n to quit)\n')
        if try_again.lower() == 'n':
            break

if __name__ == '__main__':
    pig_laten()

#pylint --max-line-length=79 pig_laten_practice.py
#
#-------------------------------------------------------------------
#Your code has been rated at 10.00/10 (previous run: 8.57/10, +1.43)
