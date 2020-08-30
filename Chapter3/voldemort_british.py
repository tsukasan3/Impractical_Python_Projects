import sys
from itertools import permutations
from collections import Counter
import load_dictionary

def main():
    """ファイルを読み込み、フィルタをかけ、
    ユーザーが最初の１文字でアナグラムをみられるようにする。"""

    name = 'tmvoorlde'

    word_list_ini = load_dictionary.load('2of4brif.txt')

    trigrams_filtered = load_dictionary.load('least-likely_trigrams.txt')

    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigrams_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)

def prep_words(name, word_list_ini):
    """アナグラムを見つけるために単語リストを準備する。"""
    print('Length initial word_list = {}'.format(len(word_list_ini)))
    len_name = len(name)
    word_list = [word.lower() for word in word_list_ini
                if len(word) == len_name]
    print('Length new word_list = {}'.format(len(word_list)))
    return word_list

def cv_map_words(word_list):
    """単語にある文字を子音と母音に対応づけ(=mappingす)る"""
    vowels = 'aeiouy'
    cv_mapped_words = []
    for word in word_list:
        temp = ''
        for letter in word:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        cv_mapped_words.append(temp)

    # ユニークなc-vパターンの数を決める
    total = len(set(cv_mapped_words))
    # 除外する目標の割合 5%
    target = 0.05
    # 目標の割合に含まれる要素数を取得する
    n = int(total * target)
    count_pruned = Counter(cv_mapped_words).most_common(total - n)

    filtered_cv_map = set()

    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print('Length filtered_cv_map = {}'.format(len(filtered_cv_map)))
    return filtered_cv_map

def cv_map_filter(name, filtered_cv_map):
    """ありえない子音母音の組み合わせに基づいて単語の並び替えを削除する"""
    perms = {''.join(i) for i in permutations(name)}
    print('Length initial permutations sets = {}'.format(len(perms)))
    vowels = 'aeiouy'
    filter_1 = set()

    for candidate in perms:
        temp = ''
        for letter in candidate:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'

        if temp in filtered_cv_map:
            filter_1.add(candidate)
    print("# choices after filter_1 = {}".format(len(filter_1)))
    return filter_1

def trigrams_filter(filter_1, trigrams_filtered):
    """ありえないトライグラムを並べ替えから削除する"""
    filtered = set()
    for candidate in filter_1:
        for trigram in trigrams_filtered:
            if trigram in candidate:
                filtered.add(candidate)
    # セット操作で、filter_1から新しいフィルタを差し引く
    filter_2 = filter_1 - filtered
    print("# choices after filter_2 = {}".format(len(filter_2)))
    return filter_2

def letter_pair_filter(filter_2):
    """ありえない文字のペアを並び替えから削除する"""
    filtered = set()
    rejects = ['dt', 'lr', 'md', 'ml', 'mt', 'mv',
               'td', 'tv', 'vd', 'vl', 'vr', 'vt']
    first_pair_rejects = ['ld', 'lm', 'lt', 'lv', 'rd',
                          'rl', 'rm', 'rt', 'rv', 'tl', 'tm']

    for candidate in filter_2:
        for r in rejects:
            if r in candidate:
                filtered.add(candidate)
        for fp in first_pair_rejects:
            if candidate.startswith(fp):
                filtered.add(candidate)

    filter_3 = filter_2 - filtered
    print("# choices after filter_3 = {}".format(len(filter_3)))
    if 'voldemort' in filter_3:
        print('Voldemort found!!', file=sys.stderr)
    return filter_3

def view_by_letter(name, filter_3):
    """入力された文字で始まるアナグラムにフィルタリングする"""
    print("Remaining letters = {}".format(name))
    first = input("select a starting letter or press Enter to see all: ")
    subset = []
    for candidate in filter_3:
        if candidate.startswith(first):
            subset.append(candidate)
    print(*sorted(subset), sep='\n')
    print('Number of choices starting with {} = {}'.format(first, len(subset)))
    try_again = input("Try again? (Press Enter else any other key to Exit)")
    if try_again == '':
        view_by_letter(name, filter_3)
    else:
        sys.exit()

if __name__ == '__main__':
    main()

"""
出力結果
-----------------------------------------
$ python voldemort_british.py
Length initial word_list = 60388
Length new word_list = 8687
Length filtered_cv_map = 234
Length initial permutations sets = 181440
# choices after filter_1 = 123120
# choices after filter_2 = 674
# choices after filter_3 = 248
Voldemort found!!
Remaining letters = tmvoorlde
select a starting letter or press Enter to see all: vol
voldemort
voldemotr
voldermot
voldertom
voldetorm
voldetrom
voldomert
voldometr
voldormet
voldortem
voldoterm
voldotrem
voldremot
voldretom
voldromet
voldrotem
voledmort
voledmotr
volortedm
volotredm
Number of choices starting with vol = 20
Try again? (Press Enter else any other key to Exit)
Remaining letters = tmvoorlde
select a starting letter or press Enter to see all:
deltormov
demortolv
demotrolv
dermotolv
dlemotrov
dlertomov
dletormov
dletromov
dlevotorm
dlevotrom
dlormotev
dlormovet
dlortemov
dlotermov
dlotomerv
dlotremov
dlotrovem
dlovemort
dlovemotr
dlovermot
dlovertom
dlovetorm
dlovetrom
dmelotrov
dmeltorov
dmeortolv
dmeotrolv
dmerotolv
dmertolov
dmertoolv
dmetorlov
dmetorolv
dmetrolov
dmetroolv
dmoretolv
dmorlevot
dmorlotev
dmorlovet
dmorolvet
dmorovelt
dmortelov
dmortevol
dmortolev
dmortolve
dmoterlov
dmoterolv
dmotolerv
dmotolver
dmotorlev
dmotrelov
dmotrevol
dmotrolev
dmotrolve
dmotrovel
dmovelort
dmovelotr
dmoveltor
dmoverlot
dmovertol
dmovetorl
dmovetrol
domertolv
dometrolv
dormetolv
dormovelt
dortolvem
dotolverm
dotrolvem
dreltomov
dremotolv
drolvemot
drolvetom
drometolv
dromovelt
drotolvem
droveltom
edmortolv
edmotrolv
ledmotrov
lortedmov
lotredmov
lotrovedm
lovedmort
lovedmotr
medlotrov
medortolv
medotrolv
medrotolv
meldotrov
merdotolv
metoldrov
modertolv
modetrolv
mordetolv
morldevot
morldotev
mortedlov
mortevold
mortoldev
mortolved
motedrolv
moteldrov
motevoldr
motolderv
motoldrev
motolvedr
motolverd
motorldev
motredlov
motrevold
motroldev
motrolved
motrovedl
motroveld
movedlort
movedlotr
moveldort
moveldotr
moveldrot
moveltord
moverldot
movertold
movetoldr
movetorld
movetrold
olvedmort
olvedmotr
ortolvedm
otrolvedm
redmotolv
rolvedmot
rotolvedm
tedlormov
tedmorlov
tedmorolv
teldormov
teldromov
terldomov
tevoldorm
tevoldrom
toldermov
toldomerv
toldremov
toldrovem
tolvedmor
tolvedorm
tolvedrom
tolvemord
tolverdom
tolvermod
tomedrolv
tomeldrov
tomorldev
tomoveldr
tomoverld
torldemov
torledmov
torlovedm
tormedlov
tormovedl
tormoveld
torolvedm
treldomov
trevoldom
troldemov
troledmov
trolovedm
trolvedmo
trolvedom
trolvemod
tromedlov
tromovedl
tromoveld
troolvedm
troveldom
vedlormot
vedlortom
vedlotorm
vedlotrom
vedmorlot
vedmortol
vedmotorl
vedmotrol
veldomort
veldomotr
veldormot
veldortom
veldotorm
veldotrom
veldromot
veldrotom
veltodorm
veltomord
veltordom
veltormod
vemorldot
vemortold
vemotoldr
vemotorld
vemotrold
verldomot
verldotom
vermotold
vertoldom
vetoldorm
vetoldrom
vetomorld
vetorldom
vetroldom
voldemort
voldemotr
voldermot
voldertom
voldetorm
voldetrom
voldomert
voldometr
voldormet
voldortem
voldoterm
voldotrem
voldremot
voldretom
voldromet
voldrotem
voledmort
voledmotr
volortedm
volotredm
votedlorm
votedmorl
voteldorm
voteldrom
votemorld
voterldom
votolderm
votoldrem
votomeldr
votomerld
votorldem
votorledm
votormedl
votormeld
votreldom
votroldem
votroledm
votromedl
votromeld
Number of choices starting with  = 248
Try again? (Press Enter else any other key to Exit)
Remaining letters = tmvoorlde
select a starting letter or press Enter to see all: voldemort
voldemort
Number of choices starting with voldemort = 1
Try again? (Press Enter else any other key to Exit)a
"""
