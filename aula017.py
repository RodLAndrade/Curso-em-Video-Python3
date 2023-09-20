from time import sleep
lanche = ["burguer","suco", "pizza", "picolé"]
print(lanche)
lanche.append("cookie")    #comando .append adiciona um novo item no fim da lista
sleep(1)
print(lanche)
lanche.insert(0,"hot dog") #comando .inset adiciona um novo item na posição indicada .insert(posição,item)
sleep(1)
print(lanche)
# para remover um item da lista pode se usar os comandos del, pop ou remove
del lanche[3] #removeu o item pizza
sleep(1)
print(lanche)
lanche.insert(3,"pizza")
sleep(1)
print(lanche)
lanche.pop(3) #removeu o item pizza, o comando pop é mais usado para remover o ultimo item da lista
sleep(1)
print(lanche)
lanche.insert(3,"pizza")
lanche.remove("pizza") # o comando remove remove pelo nome do item. se o item nao estiver na linha, sobe um erro
                        # se tiver mais de um item igual na lista, o primeiro é removido
sleep(1)
print(lanche)

num = [2, 5, 9, 1]
print(num)
num.append(7)
sleep(1)
print(num)
num.sort()
sleep(1)
print(num)
num.sort(reverse=True)
num.insert(2,0)
sleep(1)
print(num)
num.pop()
sleep(1)
print(num)
if 4 in num:
    num.remove(4)
else:
    print("Não achei o numero 4 para remover")