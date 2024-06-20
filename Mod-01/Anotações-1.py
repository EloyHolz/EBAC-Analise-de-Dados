#Primeira aula

print("Olá, Mundo!")
print('oba, eu quebrei a maldição, dnv kkk')

#Segunda aula - estudo das Variáveis I

joao_idade = 35
print("Joao tem", joao_idade, "anos!")
tipo_idade = type(joao_idade)
print(tipo_idade)

ana_idade = 10.6
print("Já Ana tem", ana_idade, "anos")
tipo_idade = type(ana_idade)
print(tipo_idade)

primeiro_nome = "Ana"
print(primeiro_nome)
print(type(primeiro_nome))

questionamento = False
print(questionamento)
print(type(questionamento))

valor = None
print(None)
print(type(None))

#Aula 3 - Estudo Variáeis II - Numericos

compra = 0
compra += 1
print(compra)
compra += 3
print(compra)
compra -= 2
print(compra)

preco_kg = 35
peso = 0.5
total = preco_kg * peso
print(total)

a = 50
b = 3
c = a/b
d = a//b
e = a%b
print ("A divisão de", a, "por", b,"é:", c)
print ("O resto dessa divisão é:", e)
print ("E a divisão inteira é:", d)
print(float(a)) #conversão de tipos numericos

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