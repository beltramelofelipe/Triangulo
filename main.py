a = int(input('Digite 1° medida: '))
b = int(input('Digite 2° medida: '))
c = int(input('Digite 3° medida: '))


if ((a + b) > c) and a == b and a == c:
   print("Triangulo equilatero")
elif ((a + b) > c) and a == b or b == c or a == c:
  print('Triangulo Isósceles')
elif ((a + b) > c) and a != b and b != c and a != c:
  print("Todos os lados diferentes")
else:
  print("Não é possivel formar um triangulo")