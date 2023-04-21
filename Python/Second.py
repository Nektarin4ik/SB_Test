#Входные параметры для примера
n = 7
k = 12
L = [120, 180, 50, 700, 150, 200, 30]

if len(L) != n:
    raise ValueError('Ошибка расстояний между банкоматами')

# С рекурсией и сложностью O((n+k)^2)
def max_min_path(n: int, k: int, L):
    if len(L)==n+k:
        return L
    maximum, i=max(L), L.index(max(L))
    maximum = L.pop(i)
    L.insert(i, int(maximum/2))
    L.insert(i, int(maximum/2))
    return max_min_path(n, k, L)

# С сортировкой и сложностью O(nlogn)
def min_path(path_wi_s):
    max, index = path_wi_s.pop(0)
    path_wi_s.append((int(max/2), index))
    path_wi_s.append((int(max/2), index))
    return path_wi_s

def max_min_path2(n, k, L):
    path_wi = list(zip(L, range(n)))
    path_wi_s = sorted(path_wi, reverse=True)
    for _ in range(k):
        path_wi_s = sorted(min_path(path_wi_s), reverse=True)
    return list(map(lambda x: x[0], sorted(path_wi_s, key=lambda x: x[1])))