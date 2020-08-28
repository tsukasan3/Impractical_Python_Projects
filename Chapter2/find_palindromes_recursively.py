"""辞書ファイルにある回文を再帰的に見つける"""
import load_dictionary
word_list = load_dictionary.load('2of4brif.txt')
pali_list = []

"""再帰的に回文を見つける"""
for word in word_list:
    original_word = word
    while True:
        # 文字列の長さが0か1の場合、回文と判定
        if len(word) == 0 or len(word) == 1:
            pali_list.append(original_word)
            break
        # 文字列が２文字以上で、かつ最初の単語と最後の単語が同じ場合、両端の文字を削除する
        elif len(word) > 1 and word[0] == word[-1]:
            word = word[1:-1]
        else:
            break

print('\nNumber of palindromes found = {}\n'.format(len(pali_list)))
print(*pali_list, sep='\n')

"""
出力結果
ーーーーーーーーーーーーーーーーーーーーーーーーー

Number of palindromes found = 56

aha
bib
bob
boob
bub
civic
dad
deed
deified
did
dud
eke
ere
eve
ewe
eye
gag
gig
hah
huh
kayak
kook
level
madam
mam
minim
mom
mum
naan
nan
noon
nun
pap
peep
pep
pip
poop
pop
pup
radar
redder
refer
rotor
sagas
sees
sexes
sis
solos
stats
tat
tenet
tit
toot
tot
tut
wow

"""
