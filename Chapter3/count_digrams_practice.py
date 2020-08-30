"""
tmvoordle にあるバイグラムをすべて見つけて、
辞書ファイル'2of4brif.txt' に出てくる頻度を数える
"""
import re
from itertools import permutations
from collections import defaultdict
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

name = 'tmvoordle'

# 名前から一意な文字のペアを生成する
digrams = set()
perms = [''.join(i) for i in permutations(name)]
for perm in perms:
    for i in range(len(perm) - 1):
        digrams.add(perm[i : i + 2])
print(*digrams, sep='\n')
print('\nNumber of digrams = {}\n'.format(len(digrams)))

# 辞書に出てくるバイグラムの頻度を数える
mapped = defaultdict(int)
for word in word_list:
    word = word.lower()
    for digram in digrams:
        for m in re.finditer(digram, word):
            mapped[digram] += 1

print('digrams frequency count:')
for k in mapped:
    print('{} {}'.format(k, mapped[k]))

"""
出力結果
ーーーーーーーーーーーーーー
$ python count_digrams_practice.py
de
mo
vm
lr
dv
lt
el
dm
et
me
rm
rt
ed
mt
rd
vt
lv
te
re
le
tm
rv
oo
md
tr
dt
ld
om
tl
dr
er
ro
eo
mr
ml
ev
vr
em
lm
ot
ov
rl
vo
vd
vl
ve
ol
dl
tv
or
td
od
do
lo
to
mv
oe

Number of digrams = 57

digrams frequency count:
dv 78
rd 955
lo 2312
do 928
ed 7287
me 2460
em 1571
te 6856
to 2022
ot 1335
re 6650
ev 648
om 1773
or 3970
er 9875
et 2240
de 3861
tl 656
le 4935
rm 812
od 809
ol 2070
rt 1474
ve 2755
ov 796
el 2591
ro 3168
lv 138
tr 2586
dl 547
mo 1531
dr 601
tm 136
dm 100
lt 500
oo 1474
eo 365
vo 419
rl 394
lm 156
ml 58
ld 457
oe 267
lr 29
mr 16
dt 22
rv 287
vr 18
mv 7
td 27
mt 4
md 5
tv 4
vl 2

"""
