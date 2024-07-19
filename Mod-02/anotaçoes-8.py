#Estudo da estrutura Dicionários

#estrutura mais completa para armazenar informaçoes que tenham relação entre si
#São estruturas de dados que armazendam dados na estrutura Chave-valor -> sao do tipo dict

# Não podem haver chaves duplicadas -> o python exclui a primiera chave duplicada
# a chave de dicionário tem q ser sempre uma string

brasil = {
    "capital" : 'Brasília',
    'idioma' : 'Portugês',
    'População' : 210
    }

print(brasil)
print(type(brasil))

#pode criar dicionários compostos -> dicionários dentro de dicionários
# as aberturas de dicionários são chamadas de keys

cadastro = {
    'andre' : {
        'nome' : 'Andre Perez',
        'ano-nasc' : 1992,
        'pais' : {
            'pai' :{
                'nome_pai': 'Gabriel Perez',
                'ano_nasc': 1971,
            }, 
            'mae' :{
                "nome_mae" : 'Gabriela Perez',
                'ano_nasc' : 1973
            }, 
        },
    },
}


# para acessar uma info dentro de um dicionário: vai chegando nas chaves principais ate achar o que vc quer -> duas formas, usando get() ou usando colchetes + cria uma variavel para armazernar esse dado especifico

    # com .get(), se nao achar, mostra none
    # as chaves no get() server para quando abre um dicionário dentro de um dicionário

niver_mae = cadastro['andre']['pais']['mae']['ano_nasc']
print(niver_mae)

niver_pai = cadastro.get('andre',{}).get('pais', {}).get('pai', {}).get('ano_nasc')
print(niver_pai)

# Operações com Dicionários
credito = {
    '123' : 750,
    '789' : 980
}

score_123 = credito.get('123')
score_789 = credito.get('789')

print(score_123)
print(score_789)

#para alterar algum elemento dentro -> outra forma de fazer sem o .update
credito['123'] = 560
score_123 = credito.get('123')
print(score_123)


#mesma coisa para criar novas chaves
credito['456'] = 1000
print(credito)

# Métodos com Dicionários
    #outra forma de criar dicionparios, suando o dict

art = dict (
    titulo = 'Mod 02 - Python e Estrutura de Dados',
    corpo = 'Topicos, aulas, Listas, Conjuntos, Dicionários',
    total_caracteres = 1530
) 

# Método de .Update -> permite adiconar/atualizar um elemento pelo chave-valor dict.update(dict)
print(art)
art.update({'total_caracteres' : 7850})
print(art) 

# Método .pop -> excluir um elemento do dicionário: dict.pop(key)
total_caracteres = art.pop('total_caracteres')
print(art)

# Conversão dict -> list (nao faz a volta)
chaves = list(art.keys())
print(chaves)
print(type(chaves))

valores = list(art.values())
print(valores)
print(type(valores))


# Desafio da Semana
wifi_disponiveis = dict(
    rede_1 = {
        'nome': 'rede 1',
        'senha' : 'cnx-cnx'
    },
    rede_2 = {
        'nome': 'rede 2',
        'senha': 'r3d3' },
)
print(wifi_disponiveis)
print(type(wifi_disponiveis))
