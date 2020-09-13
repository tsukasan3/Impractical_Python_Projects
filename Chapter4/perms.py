"""列の総数に対して、一意な列の配列をすべて見つける。

個々の列番号の一意な配置をすべて保持するリストのリストを作る。
列番号はルート転置式記号の方向(上向きに読むか下向きに読むか)によって負の値にもなる

Input:
- 列の総数

Returns:
- 一意な列の順序を保持するリストのリスト
ルート暗号の暗号化の方向によって負の値になることもある

"""
from itertools import permutations, product

# 列番号の組みあわせを保持するリストのリストを作る
# itertools の product　は入力された反復可能オブジェクトのデカルト積を計算する
def perms(num_cols):
    """列番号の整数を受け取って、正負の値の順列を作成する"""
    results = []
    columns = [x for x in range(1, num_cols+1)]
    for perms in permutations(columns):
        for signs in product([1, -1], repeat=len(columns)):
            results.append([i*sign for i, sign in zip(perms, signs)])
    return results
