matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somarPar = 0
somar = 0
bigger = 0


for l in range(0, 3):
  for c in range(0, 3):
    matrix[l][c] = int(input(f'Digite um valor para a posição {l},{c}: '))

print('-=' * 11)
for l in range(0, 3):
  for c in range(0, 3):
    if matrix[l][c] % 2 == 0:
      somarPar += matrix[l][c]
    
    if matrix[l][c] == matrix[l][2]:
      somar += matrix[l][2]

    if matrix[l][c] == matrix[1][c]:
      if matrix[1][c] == 0:
        bigger = matrix[1][c]
      else:
        if matrix[1][c] > bigger:
          bigger = matrix[1][c]

    print(f'[{matrix[l][c]:^5}]', end='')
  print()
print('-=' * 11)

print(f'A soma dos números pares é: {somarPar}');
print(f'A soma dos valores da terceira coluna é: {somar}')
print(f'O maior número da segunda linha é: {bigger}')

print('-=' * 11)