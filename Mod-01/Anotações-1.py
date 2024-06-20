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