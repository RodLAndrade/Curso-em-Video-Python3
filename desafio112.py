from exercicio112.UtilidadesCursoEmVideo.dado import dado
from exercicio112.UtilidadesCursoEmVideo.moeda import moeda

p = dado.loop_input_preços("Digite o valor: R$")
moeda.resumo(p, 20, 30)