"""テキストファイルをリストとして読み込む

Arguments:
- テキストファイル名

Exceptons:
- ファイルが見つからなかった時の IOError

Returns:
- テキストファイルにある全ての単語を小文字にしたリスト

import sys が必要.

"""

import sys

def load(file):
    """テキストファイルを開いて、内容を小文字の文字列のリスト型に変換する。"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [w.lower() for w in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)
