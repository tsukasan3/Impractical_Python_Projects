"""暗号の列数を整数で受け取って、ありうる鍵の組み合わせをタプルとして返す。"""
from itertools import permutations

# 列数
COLS = 4

possible_keys = [n for n in range(-(COLS),COLS+1) if n != 0]
keys = []
print(possible_keys)

for key in permutations(possible_keys, 4):
    abs_key = set()
    for n in key:
        abs_key.add(abs(n))

    if len(abs_key) == 4:
        keys.append(key)

print(*keys, sep="\n")
print("Number of cols conbinations = {}".format(len(keys)))
