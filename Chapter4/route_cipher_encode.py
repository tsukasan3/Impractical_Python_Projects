"""メッセージをルート転置式暗号にエンコードする
"""

# 平文
plaintext = """We will run the batteries at Vicksburg the night of April 16 and
proceed to Grand Gulf Where we will reduce the forts. Be prepared to cross the
river on April 25 or 29. Admiral Porter."""

# 符号語の辞書
code_dict = {
"Batteries": "HOUND",
"Vicksburg": "ODOR",
"April": "CLAYTON",
"16": "SWEET",
"Grand": "TREE",
"Gulf": "OWL",
"Forts": "BAILEY",
"River": "HICKORY",
"25": "ADD",
"29": "HERMES",
"Porter": "LANGFORD"
}

dummy_list = ["IS", "VILLAGE", "TRANSPORT", "JUST", "SOUTH", "REST"]

# 行数
COLS = 6

# 列数
ROWS = 7

# 鍵
key = [-1, 3, -2, 6, 5, -4]

# 平文の "." を消去
# 文字列を単語に分割
plaintext = plaintext.replace(".", "")
plainlist = list(plaintext.lower().split())

def replace_to_codeword(plainlist, code_dict):
    plainlist_replaced = []
    for word in plainlist:
        if word.capitalize() in code_dict:
            plainlist_replaced.append(code_dict[word.capitalize()])
        else:
            plainlist_replaced.append(word.upper())

    return plainlist_replaced

plainlist_replaced = replace_to_codeword(plainlist, code_dict)
# 末尾にダミー単語のリストを追加
fixed_plainlist = plainlist_replaced + dummy_list
print("\nplainlist = {}".format(fixed_plainlist))

translation_matrix = [list() for j in range(COLS)]

# 6 × 7 の暗号表を作る
for i in range(ROWS):
    for j in range(COLS):
        word = fixed_plainlist[j + i*COLS]
        translation_matrix[j].append(word)

print("\ntranslation_matrix = {}".format(translation_matrix))
print("key = {}".format(key))

# 暗号表と鍵を使って、暗号文を作る
ciphertext = ""

for k in key:
    if k > 0:
        words = " ".join(translation_matrix[abs(k)-1])
        ciphertext += words + " "
    elif k < 0:
        words = " ".join(list(reversed(translation_matrix[abs(k)-1])))
        ciphertext += words + " "

print("\nciphertext = {}".format(ciphertext))

"""
出力
ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
$ python route_cipher_encode.py

plainlist = ['WE', 'WILL', 'RUN', 'THE', 'HOUND', 'AT', 'ODOR', 'THE', 'NIGHT',
 'OF', 'CLAYTON', 'SWEET', 'AND', 'PROCEED', 'TO', 'TREE', 'OWL', 'WHERE',
 'WE', 'WILL', 'REDUCE', 'THE', 'BAILEY', 'BE', 'PREPARED', 'TO', 'CROSS',
 'THE', 'HICKORY', 'ON', 'CLAYTON', 'ADD', 'OR', 'HERMES', 'ADMIRAL',
 'LANGFORD', 'IS', 'VILLAGE', 'TRANSPORT', 'JUST', 'SOUTH', 'REST']

translation_matrix = [
['WE', 'ODOR', 'AND', 'WE', 'PREPARED', 'CLAYTON', 'IS'],
['WILL', 'THE', 'PROCEED', 'WILL', 'TO', 'ADD', 'VILLAGE'],
['RUN', 'NIGHT', 'TO', 'REDUCE', 'CROSS', 'OR', 'TRANSPORT'],
['THE', 'OF', 'TREE', 'THE', 'THE', 'HERMES', 'JUST'],
['HOUND', 'CLAYTON', 'OWL', 'BAILEY', 'HICKORY', 'ADMIRAL', 'SOUTH'],
['AT', 'SWEET', 'WHERE', 'BE', 'ON', 'LANGFORD', 'REST']
]
key = [-1, 3, -2, 6, 5, -4]

ciphertext = IS CLAYTON PREPARED WE AND ODOR WE RUN NIGHT TO REDUCE CROSS OR
TRANSPORT VILLAGE ADD TO WILL PROCEED THE WILL AT SWEET WHERE BE ON LANGFORD
REST HOUND CLAYTON OWL BAILEY HICKORY ADMIRAL SOUTH JUST HERMES THE THE TREE
OF THE
"""
