"""
　英語の文章を入力としてとり棒グラフもどき生成のコードを実行する。
また、文章を他のラテン語系の言語(今回はスペイン語)に変換し、
棒グラフもどき生成のコードを再実行して、結果を比べる。

　異なる入力を直接比較できるように、アルファベットの全ての文字を辞書のキーとして、
値がなくても表示されるように、コードを変更する。
"""

from googletrans import Translator
import pprint
import re

translator = Translator()

def main():
    while True:
        print('\n↓Input sentence！↓')
        sentence_src = input('\n')
        # グーグル翻訳を使って、スペイン語に翻訳
        sentence_dst = translator.translate(sentence_src, dest='es').text
        # 翻訳元(英語)のリスト, キーはアルファベットの全ての文字で、値は空のリスト
        alphabet_dict_src = {chr(code): list() for code in range(ord('a'), ord('z')+1)}
        # 翻訳先(スペイン語)のリスト
        alphabet_dict_dst = {chr(code): list() for code in range(ord('a'), ord('z')+1)}

        for i, c in enumerate(sentence_src):
            if re.match('[a-zA-Z]', c):
                alphabet_dict_src[c.lower()].append(c.lower())

        for i, c in enumerate(sentence_dst):
            if re.match('[a-zA-Z]', c):
                alphabet_dict_dst[c.lower()].append(c.lower())

        print('alphabet_dict_src\n')
        pprint.pprint(alphabet_dict_src)
        print('\n\n' + sentence_dst)
        print('\nalphabet_dict_dst\n')
        pprint.pprint(alphabet_dict_dst)
        print('\n\n')

        try_again = input('Try again? (Press Enter else n to quit)\n')
        if try_again.lower() == 'n':
            break

if __name__ == '__main__':
    main()


"""
出力結果
----------------------

$ python ETAOIN_practice_Spanish_ver.py

↓Input sentence！↓

Like the castle in its corner in a medieval game, I foresee terrible trouble and I stay here just the same.
alphabet_dict_src

{'a': ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
 'b': ['b', 'b'],
 'c': ['c', 'c'],
 'd': ['d', 'd'],
 'e': ['e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e'],
 'f': ['f'],
 'g': ['g'],
 'h': ['h', 'h', 'h'],
 'i': ['i', 'i', 'i', 'i', 'i', 'i', 'i', 'i'],
 'j': ['j'],
 'k': ['k'],
 'l': ['l', 'l', 'l', 'l', 'l'],
 'm': ['m', 'm', 'm'],
 'n': ['n', 'n', 'n', 'n'],
 'o': ['o', 'o', 'o'],
 'p': [],
 'q': [],
 'r': ['r', 'r', 'r', 'r', 'r', 'r', 'r'],
 's': ['s', 's', 's', 's', 's', 's'],
 't': ['t', 't', 't', 't', 't', 't', 't', 't'],
 'u': ['u', 'u'],
 'v': ['v'],
 'w': [],
 'x': [],
 'y': ['y'],
 'z': []}


Como el castillo en su esquina en un juego medieval, preveo problemas terribles y me quedo aquí de todos modos.

alphabet_dict_dst

{'a': ['a', 'a', 'a', 'a', 'a'],
 'b': ['b', 'b'],
 'c': ['c', 'c'],
 'd': ['d', 'd', 'd', 'd', 'd'],
 'e': ['e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e',
       'e'],
 'f': [],
 'g': ['g'],
 'h': [],
 'i': ['i', 'i', 'i', 'i'],
 'j': ['j'],
 'k': [],
 'l': ['l', 'l', 'l', 'l', 'l', 'l'],
 'm': ['m', 'm', 'm', 'm', 'm'],
 'n': ['n', 'n', 'n', 'n'],
 'o': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
 'p': ['p', 'p'],
 'q': ['q', 'q', 'q'],
 'r': ['r', 'r', 'r', 'r'],
 's': ['s', 's', 's', 's', 's', 's', 's'],
 't': ['t', 't', 't'],
 'u': ['u', 'u', 'u', 'u', 'u', 'u'],
 'v': ['v', 'v'],
 'w': [],
 'x': [],
 'y': ['y'],
 'z': []}



Try again? (Press Enter else n to quit)
n

--------------------
上記の結果から、スペイン語の文章には、uが3倍現れている。
さらに、英語の文章にはないpとqが現れている。

"""
