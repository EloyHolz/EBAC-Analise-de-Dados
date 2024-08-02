filmes = [
    "Um Sonho de Liberdade,",
    "O Poderoso Chefão,",
    "Batman: O Cavaleiro das Trevas,",
    "12 Homens e uma Sentença,",
    "A Lista de Schindler,",
    "O Senhor dos Anéis: O Retorno do Rei,",
    "Pulp Fiction: Tempo de Violência,",
    "O Senhor dos Anéis: A Sociedade do Anel,",
    "Três Homens em Conflito."
]

print(filmes)

#Retirar os Valores 
primeiro_filme = filmes.pop(0)
print(primeiro_filme)

segundo_filme = filmes.pop(0)
print(segundo_filme)

#Adicionar e trocar de posição
filmes.insert(0, segundo_filme)
filmes.insert(1,primeiro_filme)
print(filmes)

#identificar e duplicar os 3 ultimos filmes ( poderia usar o add tb aqui)
    #O método extend adiciona todos os elementos de uma lista (ou qualquer iterável) ao final da lista original.
ultimos_filmes = filmes[-5:]
filmes.extend(ultimos_filmes)

print(filmes)
print(len(filmes))

#Convertendo para Conjuntos (set)
conjunto_filmes = list(set(filmes))
print(conjunto_filmes)
print(len(conjunto_filmes))


IMDB = [
    {'nome': "The Shawshank Redemption", 'ano': 1994, 'sinopse': "Dois homens condenados estabelecem uma ligação ao longo de vários anos, encontrando consolo e redenção através de atos de decência."},
    {'nome': "The Godfather", 'ano': 1972, 'sinopse': "O patriarca envelhecido de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante."},
    {'nome': "The Dark Knight", 'ano': 2008, 'sinopse': "Quando a ameaça conhecida como Coringa emerge de seu passado misterioso, ele causa estragos e caos nas pessoas de Gotham."},
    {'nome': "The Godfather Part II", 'ano': 1974, 'sinopse': "A vida precoce e carreira de Vito Corleone na década de 1920 em Nova York é retratada enquanto seu filho Michael expande e aperta o controle sobre a organização criminosa familiar."},
    {'nome': "12 Angry Men", 'ano': 1957, 'sinopse': "Um jurado tenta evitar um erro judiciário forçando seus colegas a reconsiderar a evidência."},
    {'nome': "Schindler's List", 'ano': 1993, 'sinopse': "Na Polônia ocupada pelos nazistas durante a Segunda Guerra Mundial, Oskar Schindler se torna um improvável humanitário ao gastar toda sua fortuna para salvar 1.100 judeus do Holocausto."},
    {'nome': "The Lord of the Rings: The Return of the King", 'ano': 2003, 'sinopse': "Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para distrair seu olhar de Frodo e Sam enquanto eles se aproximam do Monte da Perdição com o Um Anel."},
    {'nome': "Pulp Fiction", 'ano': 1994, 'sinopse': "As vidas de dois homens, um boxeador, um gangster e sua esposa e dois bandidos se entrelaçam em quatro contos de violência e redenção."},
    {'nome': "The Good, the Bad and the Ugly", 'ano': 1966, 'sinopse': "Um pistoleiro errante se junta com dois homens para encontrar uma fortuna em ouro enterrada em um cemitério remoto."},
    {'nome': "Fight Club", 'ano': 1999, 'sinopse': "Um insone descontente e um fabricante de sabonetes despreocupado formam um clube de luta subterrâneo que se transforma em algo muito maior."}
]
print(IMDB)
nota1 = IMDB.pop(0)
nota2 = IMDB.pop(0)

print(nota1)
print(nota2)

IMDB.insert(0,nota2)
IMDB.insert(1,nota1)

print(IMDB)
