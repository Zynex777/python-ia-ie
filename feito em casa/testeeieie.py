# Tentativa de busca binária: compara o alvo ao elemento central do intervalo.
# // é divisão inteira; lo e hi delimitam a região pesquisada.
# A atribuição inicial tem três variáveis e quatro valores e causa ValueError.
# len(v) também ultrapassa o último índice válido. O trecho permanece como está.

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