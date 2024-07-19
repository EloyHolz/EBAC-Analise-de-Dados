#Estudo Sobre conjuntos -> Armazenam sequencias imutaveis e desordenadas valores, sem repitição. 
# São do tipo set.
 
#não consegue acessar a um elemento especifico -> nao ha uma ordem
#em vez de [] usa {}
#Não permite elemetnos repetidos
frutas = {"banana", "maca", "uva", "uva"}
print(frutas)
print(type(frutas))

#operações com conjuntos -> Diferença (-) -> gera um novo conjunto
#a ordem dos elementos importa

norte_eu ={"reino unido", "suecia", "russia", "noruega", "dinamarca"}
escandinavia ={ "noruega", "dinamarca", "suecia"}

print(norte_eu)
print(escandinavia)

norte_eu_nao_escandinavo = norte_eu - escandinavia
escandinavo_nao_norte_eu = escandinavia - norte_eu
print(norte_eu_nao_escandinavo)
print(escandinavo_nao_norte_eu) #nao havia dif, por isso fica vazio

#Métodos de manipulação dos conjuntos   
cursos = {'Exatas','Humanas', 'Biológicas'}
print(cursos)

#adição -> inserir elemento no conjunto: set.add(val)
cursos.add('Saúde')
print(cursos)

#remoção -> retirar um elemento no conjunto: set.remove(val)
cursos.remove('Saúde')
print(cursos)

#Conversao -> Listas <-> Conjuntos
#remoção muito ultilziada para remover itens duplicados de listas, convertendo elas para conjunto, ou para acessar elemento especifico de um conjunto, convertendo para uma lista
times_paulistas = {'SP', 'Palmeiras', 'Corinthians', 'Santos'}
print(times_paulistas)
print(type(times_paulistas))

print(list(times_paulistas))
print(type(list(times_paulistas)))

#Motivação Semanal -> converteu e removeu a duplicidade das listas
hastag_seg = ["#tiago", "#joao" , "#bbb"]
hastag_ter = ["#sarah", "#bbb", "#fiuk"]
hastag_qua = ["#gil", "#thelma", "#lourdes"]
hastag_qui = ["#rafa", "#fora", "#danilo"]
hastag_sex = ["#juliete", "#arthur", "#bbb"]

hastag_semana = hastag_seg + hastag_ter + hastag_qua + hastag_qui + hastag_sex
print(hastag_semana)
print(len(hastag_semana))

hastag_semana = list(set(hastag_seg +hastag_ter + hastag_qua + hastag_qui + hastag_sex))
print(hastag_semana)
print(len(hastag_semana))