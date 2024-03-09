def min_abs_coordinate(X, K, D):
    X = abs(X)  # 初期座標の絶対値を取る
    
    # K回の移動で座標0に到達する場合
    if X // D >= K:
        return X - K * D
    
    # まずは座標0に到達する
    X -= (X // D) * D
    K -= X // D
    
    # K回の移動での絶対値の最小化を考える
    if K % 2 == 0:
        return X
    else:
        return D - X

# 入力例1
X,K,D = map(int,input().split())
print(min_abs_coordinate(X,K,D))  # 出力例1: 1
