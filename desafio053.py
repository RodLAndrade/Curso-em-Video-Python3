palavra = str(input("digite uma frase ou palavra: ")).strip().upper()
separado = palavra.split()
junto = ''.join(separado)
inverso = ''
print(f"{junto}")
for letra in range(len(junto) -1, -1, -1):
 inverso += junto[letra]
print(inverso)
if inverso == junto:
    print("É um palindromo.")
else:
    print("Não é um palindromo.")