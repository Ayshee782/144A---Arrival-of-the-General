n = int(input())
a = list(map(int, input().split()))

max_height = max(a)
min_height = min(a)

max_index = a.index(max_height)  # first max
min_index = len(a) - 1 - a[::-1].index(min_height)  # last min

moves = max_index + (n - 1 - min_index)
if max_index > min_index:
    moves -= 1  # one less move due to overlap

print(moves)
