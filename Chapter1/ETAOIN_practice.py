"""文字列を入力としてとり、その中に含まれるローマ字を数え上げて、
その結果を単純な棒グラフ型の表示で返す"""
import re
from collections import defaultdict
import pprint

def main():
    """文字列を入力としてとり、その中に含まれるローマ字を数え上げて、
    その結果を単純な棒グラフ型の表示で返す"""
    while True:
        sentence = input()
        alphabet_dict = defaultdict(list)

        for i, c in enumerate(sentence):
            if re.match('[a-zA-Z]', c):
                alphabet_dict[c.lower()].append(c.lower())

        pprint.pprint(alphabet_dict)

        try_again = input("\n\nTry again? (Press Enter else n to quit)")
        if try_again.lower() == 'n':
            break

if __name__ == '__main__':
    main()

# テスト
"""
$ python ETAOIN_practice.py
Like the castle in its corner in a medieval game, I foresee terrible trouble and I stay here just the same.
defaultdict(<class 'list'>,
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
             'r': ['r', 'r', 'r', 'r', 'r', 'r', 'r'],
             's': ['s', 's', 's', 's', 's', 's'],
             't': ['t', 't', 't', 't', 't', 't', 't', 't'],
             'u': ['u', 'u'],
             'v': ['v'],
             'y': ['y']})


Try again? (Press Enter else n to quit)n
"""
