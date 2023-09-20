nomeentrada = str(input("Qual é seu nome? "))
nome = nomeentrada.upper()
if nome == "Rod":
    print("Que belo nome!")
elif nome == "PEDRO" or nome == "PAULO" or nome == "MARIA":
    print("Seu nome é bem popular no Brasil.")
elif nome in "PETER PARKER MILES MORALES GWEN PETER PORKER PENI PARKER":
    print("Talvez você seja um MIRANHA")
else:
    print("Seu nome é bem normal.")
print(f"Tenha um bom dia, {nomeentrada}.")