filme = {"titulo":"Star Wars", "ano":1977, "diretor":"George Lucas"}
print(filme.values())
print(filme.keys())
print(filme.items())
print("*" * 30)
for k, v in filme.items():
    print(f"O {k} é {v}.")
    
    #é possivel fazer estrutura de lista com varias chves dentro EX:
    #locadora = [{"titulo": "Star Wars", "ano": 1977, "diretor": "George Lucas"},
    #            {"titulo": "Avengers", "ano": 2012, "diretor": "Joss Whedon"},
    #            {"titulo": "Matrix", "ano": 1999, "diretor": "Wachowski"}]