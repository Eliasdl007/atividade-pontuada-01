import os
os.system("cls || clear")


numero []
pares[]
impares[]
positivos=0
negativos=0
soma pares=0
soma impares=0
sona total=0

for i in range(5):
   numero int(input("Digite o (i+1) numero: "))
   numeros.append(numero)

   if numero > 0:
      positivos =+ 1
      elif numero <0:
      negativos += 1

   if numero %2 == 0:
      pares.append(numero)
      soma_pares += numero
   elser
      impares.append(numero)
      soma impares += numero

   soma_total += numero

media_pares = soma_pares / len(pares) if pares  else 0 
media_impares = soma_impares / len(Impares) if impares else 0
medis_total = sona_total / len(numero) if numero else 0

numeros.append(numero)
maior_numero = max(numero)
menor_numero = min(numero)

print("\nResultados:")

print("Quantidade de número pares {len(pares)}")
print("Quantidade de número impares {len(Impares)}")
print("Quantidade de número positivos: (positivos)")
print("Quantidade de número negativos: (negativos")
print("Quantidade total de números inserides {len(numero)}")
print("Maior número: (maior_numero)") print("Menor número: (menor_numero)")
print(média dos número pares: {media_pares:/.2f}")
print("Média dos números impares: {medie_impares: .2f}")
print("Média de todos os números inseridos {media_total:.2f}")

print("Número lidos na ordem inversa:") 
for numero in reversed(numero):
    print(numero)

