#Aula 4 - Variaveis III - Strings

Residencia = "Casa"
outro_nome = ""
print (Residencia, outro_nome)
print(type(Residencia))
print(type(outro_nome))

nome = 'Eloy'
sobrenome = "Holzgrefe"
print (
"Olá, me chamo " + nome +' ' + sobrenome+ ". Qual o seu nome?"
)
#com a concatenação apenas junta, fica sem espaço entre as coisas
#outra forma de fazer
apresentacao = f"Olá, meu nome é {nome} {sobrenome}! Qual o seu nome?"
print (apresentacao)

email = "eloyneto61@gmail.com"
print(email[3])
print(email[0:10])

#conversao entre string e num
faturamento = 'R$ 35 mil'
print(faturamento)
print(type(faturamento))

faturamento = int(faturamento[3:5])
print(faturamento)
print(type(faturamento))

#atividade de latitude

# sua empresa
lat = '-22.005320'
lon = '-47.891040'

# startup adquirida
latlon = '-22.005320;-47.891040'

#Primeiro, encontrar o caractere que separa os valores, no caso o ; e atribuir o seu valor a uma variavel
posicao_char_divisao = latlon.find(';')
print(posicao_char_divisao)

#Depois, deve extrair a primeira parte, nesse caso vamos fazer com o Lat, suando como limitação a divisao delimitada acima
lat_startup = latlon[0:posicao_char_divisao]
print(lat_startup)

#agora com as duas informaçoes, resta extrair o resto
lon_startup = latlon[posicao_char_divisao+1: len(latlon)]
print(lon_startup)