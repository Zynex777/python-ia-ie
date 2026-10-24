# Laços aninhados percorrem linha e coluna; % calcula o resto da divisão.
# and e or combinam as regras de desenho; end=" " evita a quebra após o símbolo.
# O print() vazio está dentro do laço das colunas, quebrando a linha após cada posição.

for row in range(6):
    for col in range(7):
        if ((row == 0 and col % 3 != 0) or
            (row == 1 and col % 3 == 0) or
            (row - col == 2) or
            (row +  col == 8)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
        print()