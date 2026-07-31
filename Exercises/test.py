n, k = map(int, input().split())
trees = list(map(int, input().split()))

current_total = sum(trees[:k])
total = current_total

for i in range(k, n):
    current_total += trees[i]
    current_total -= trees[i - k]
    total = max(total, current_total)

return total