#Estudo Sobre conjuntos -> Armazenam sequencias imutaveis e desordenadas valores, sem repitição. 
# São do tipo set.
   

hastag_seg = ["#tiago", "#joao" , "#bbb"]
hastag_ter = ["#sarah", "#bbb", "#fiuk"]
hastag_qua = ["#gil", "#thelma", "#lourdes"]
hastag_qui = ["#rafa", "#fora", "#danilo"]
hastag_sex = ["#juliete", "#arthur", "#bbb"]

hastag_semana = hastag_seg + hastag_ter + hastag_qua + hastag_qui + hastag_sex
print(hastag_semana)

#não consegue acessar a um elemento especifico -> nao ha uma ordem
#em vez de [] usa {}
#Não permite elemetnos repetidos
frutas = {"banana", "maca", "uva", "uva"}
print(frutas)
print(type(frutas))

#operações com conjuntos -> Diferença (-) -> gera um novo conjunto
norte_eu ={"reino unido", "suecia", "russia", "noruega", "dinamarca"}
escandinavia ={ "noruega", "dinamarca", "suecia"}

norte_eu_nao_escandinavo = norte_eu - escandinavia
escandinavo_nao_norte_eu = norte_eu - escandinavia
print(norte_eu_nao_escandinavo)
print(escandinavo_nao_norte_eu)

