v = range(1,2**20)
x = 699051
lo, hi, n = 0, len(v), -1, 0
while lo <= hi:
    mid = (lo + hi) // 2
    n += 1
    if v[mid] == x: break
    if v[mid] < x: lo = mid + 1
    else: hi = mid - 1
print(v[mid], n)