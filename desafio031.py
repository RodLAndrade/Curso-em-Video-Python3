kmrodado = float(input("Digite à quantos kilometros de distancia fica seu destino: "))
if kmrodado <= 200:
    passagem = kmrodado*0.5
else:
    passagem = kmrodado*0.45
print(f"sua passagem vai custar R${passagem:.2f}.")
