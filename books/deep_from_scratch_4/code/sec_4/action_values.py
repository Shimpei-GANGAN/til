V = {'L1': 0.0, 'L2': 0.0}
V_new = V.copy()

# 方策は更新しないんだっけ？ずっと 0.5
cnt = 0
while True:
    V_new['L1'] = 0.5 * (-1 + 0.9 * V['L1']) + 0.5 * (1 + 0.9 * V['L2'])
    V_new['L2'] = 0.5 * (0.9 * V['L1']) + 0.5 * (-1 + 0.9 * V['L2'])
    
    delta = abs(V_new['L1'] - V['L1'])
    delta = max(delta, abs(V_new['L2'] - V['L2']))
    V = V_new.copy()

    cnt += 1
    if delta < 0.0001:
        print(V)
        print(cnt)
        break
