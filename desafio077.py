palavras = "aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar"
for item in palavras:
    print(f"\nNa palavra {item.upper()} temos as vogais ",end="")
    for letra in item:
        if letra.lower() in "aeiou":
            print(f"{letra} ",end="")






  #  for i in range(0, len(vogais)):
   #     if vogais[i] in palavras[c]:
    #        print(f"{vogais[i]}")