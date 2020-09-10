"""暗号文の文字列を引数にとって、転置式暗号であるか換字式暗号であるかを判断するPython
プログラムをかく。

ここで、アルファベットの頻度分布に、
Dvorakjpの文字頻度表(http://www7.plala.or.jp/dvorakjp/hinshutu.htm)のうちの
アルファベットの頻度表を用いる。これは「CNN・ABC・VOAの各ニュースの各分野からランダムに
4万1600文字を抜き出して各文字についてカウントしたもの」（抜粋）であり、以下の通りである

 	回数	ﾊﾟｰｾﾝﾃｰｼﾞ

e	4663	11.40962588	 f	 811    1.984389146
a	3452	8.446499792	 g	 744	1.820450708
t	3345	8.184687661	 y	 733	1.793535443
i	2914	7.130098608	 w	 694    1.698108591
o	2882	7.051799653	 b	 672    1.644278059
s	2850	6.973500697	 v	 408    0.998311679
n	2767	6.770412782	 k	 366    0.8955443
r	2543	6.222320096	 j	 84	    0.205534757
h	1739	4.255058847	 x	 72	    0.176172649
l	1583	3.87335144	 q	 34	    0.08319264
d	1582	3.870904598	 z	 32	    0.078298955
c	1306	3.195576109	 .	 661    1.617362793
u	1207	2.953338716	 ,	 440    1.076610634
m	1092	2.671951846	 ; : 32	    0.078298955
p	827	    2.023538623	 ' " 334    0.817245345

 	 	 	合計	40869	100%

頻度の高い文字はe, a, t, i, o, s, n, rであることがわかる
これらの文字の頻度が高い、すなわち、
上の頻度分布に近い頻度分布を持つ文字列を転置式暗号であると判断する。
"""
from collections import Counter

def identify_cipher_type(cipher):
    cipher = "".join(cipher.split())
    len_cipher = float(len(cipher))
    count = Counter(cipher)

    #文字列の頻度分布を取得
    alphabet_freq = {}
    for k, v in count.items():
        alphabet_freq[k] = v / len_cipher * 100

    return alphabet_freq


with open("cipher_a.txt", mode="r") as text_a:
    cipher_a = text_a.read()

with open("cipher_b.txt", mode="r") as text_b:
    cipher_b = text_b.read()


alphabet_freq_a = identify_cipher_type(cipher_a)
alphabet_freq_b = identify_cipher_type(cipher_b)
print(alphabet_freq_a)
print("\n\n", alphabet_freq_b)

"""
出力結果
ーーーーーーーーーーーーーーーー
$ python identify_cipher_type.py
{'F': 2.3498694516971277, 'C': 2.6979982593559617, 'N': 6.70147954743255,
'E': 14.360313315926893, 'R': 6.875543951261967, 'O': 8.093994778067886,
'T': 10.966057441253264, 'B': 1.2184508268059182, 'H': 6.962576153176675,
'W': 2.4369016536118364, 'D': 5.047867711053089, 'A': 8.87728459530026,
'P': 1.3054830287206265, 'I': 5.918189730200174, 'M': 1.1314186248912097,
'U': 1.8276762402088773, 'G': 2.4369016536118364, 'L': 3.6553524804177546,
'S': 3.829416884247171, 'V': 2.088772845953003, 'Y': 0.8703220191470844,
'K': 0.26109660574412535, 'Q': 0.08703220191470844}


 {'Q': 4.090513489991297, 'W': 3.6553524804177546, 'H': 3.5683202785030463,
 'T': 4.090513489991297, 'G': 7.049608355091384, 'N': 4.090513489991297,
 'B': 4.43864229765013, 'C': 6.614447345517842, 'M': 2.6979982593559617,
 'P': 6.70147954743255, 'R': 5.221932114882506, 'D': 1.4795474325500435,
 'A': 2.6979982593559617, 'S': 5.308964316797215, 'L': 3.1331592689295036,
 'E': 5.047867711053089, 'I': 2.610966057441253, 'F': 2.78503046127067,
 'J': 2.8720626631853787, 'Z': 4.003481288076589, 'U': 2.78503046127067,
 'V': 5.221932114882506, 'Y': 4.177545691906006, 'O': 3.1331592689295036,
 'K': 1.3054830287206265, 'X': 1.2184508268059182}
ーーーーーーーーーーーーーーーー

出力より、２つの文字列において、頻度の高い文字は以下の通りである。降順で示す。

cipher_a: e, t, a, o, i, r, n
cipher_b: g, p, c, s, r, v, e

上の結果と頻度表より、
cipher_aは転置式暗号、cipher_bは換字式暗号であると判断する。
"""
