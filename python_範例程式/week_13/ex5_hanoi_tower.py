## ex5_hanoi_tower.py ##

def hanoi(n, _from, _mid, _to):
    if n == 1: # 河內塔的終止條件
        print(f"盤子{n}從{_from}到{_to}")
    else:
        hanoi(n-1, _from, _to, _mid)      # 將n-1個圓盤，先移到中間
        hanoi(1, _from, _mid, _to)        # 若只剩下1個圓盤，直接移到to
        hanoi(n-1, _mid, _from, _to)      # 把在中間位置的n-1個圓盤，移到to

hanoi(3, 'A', 'B', 'C') # 呼叫hanoi函式，定義盤子為3個，並包含A,B,C三個柱子

