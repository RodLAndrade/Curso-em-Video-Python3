times = "Botafogo", "Flamengo", "Plameiras", "Grêmio", "São Paulo", "Fluminense", "Bragantino", "AthleticoPR", "Fortaleza", "Cruzeiro", "Internacional", "AtleticoMG", "Cuiabá", "Santos", "Corinthians", "Bahia", "Goiás", "Coritiba", "AméricaMG", "Vasco"
print(f"Os Cinco primeiros colocados do Brasileirão são: {times[0:5]}")
print("-"*50)
print(f"Os quatro ultimos colocados do Brasileirão são: {times[-4:]}.")
print("-"*50)
print(sorted(times))
print("-"*50)
print(f"O Chapecoense não está Brasileirão em 2023, mas o Corinthians está na {times.index('Corinthians')+1}")
