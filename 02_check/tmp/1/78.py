# encoding:UTF-8

map_1 = {'wang': 20, 'li': 22, 'zhang': 33, 'teng': 40}
m = 'wang'
for x in map_1.keys():
    if map_1[m] < map_1[x]:
        m = x
print(m, map_1[m])
