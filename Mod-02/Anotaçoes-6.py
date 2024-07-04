#Estudando Estruturas de dados - Listas
saldo_inical = 1000
transacao_1 = 243
transacao_2 = -798.58
transacao_3 = 427.12
transacao_4 = -10.91
saldo_final = saldo_inical + transacao_1 + transacao_2 + transacao_3 + transacao_4 
print(saldo_final)

#Existe uma forma melhor de amarzenar essas variáveis? Com as listas dá -> usando [ ]


idade = 20
saldo_conta = saldo_final
login = True
usuario_web = ['André' , idade,  'Andrezinho' , 'andre 1223' , 'andre.perreira@gmail.com', saldo_conta, login]
print(usuario_web)
print(type(usuario_web))


#concatenação para listas
fab_mob_china = ['xiaomi', 'hauwei']
fab_mob_usa = ['apple', 'motorola']
fab_mob = fab_mob_china + fab_mob_usa

print(fab_mob_usa)
print(fab_mob_china)
print(fab_mob)



fab_mob_china = fab_mob[0:2]
fab_mob_usa = fab_mob[2:len(fab_mob)]

print('china: ' + str(fab_mob_china))
print('eua: ' + str(fab_mob_usa))

#atribuição de valores - subistitui o valor na posição selecionada -> são mutáveis
fab_mob [2] = "nokia"
print (fab_mob)



# Métodos com pyhton
juros = [0.05, 0.07, 0.02, 0.04, 0.08]
print(juros)

#inserir um elemento sem subistituir os existentes = list.insert(index (posição que quer add), val(valor em si))
juros.insert(0, 0.10)
print(juros)

# inserir no fim da lista -> list.append(val)
juros.append(0.09)
print(juros)

# Remover um valor especifico da lista list.remove(val)
juros.remove(0.07)
print(juros)

# Remover pela posição -> list.pop(val)
terceiro_juros = juros.pop(2)
print(juros)
print ( terceiro_juros)

# Conversão de Listas para strings

email = 'andre.prex@gmail.com'
caracteres_email = list(email)

print(email)
print(caracteres_email)

#Aplicando os conhecimentos na atividade inicial

dia_11_saldo_inicial = 2000
dia_11_transacoes = list()

dia_11_transacoes.append(243)
dia_11_transacoes.append(-798.58)
dia_11_transacoes.append(427.12)
dia_11_transacoes.append(-10.91)

print(dia_11_transacoes)
dia_11_saldo_final = dia_11_saldo_inicial + dia_11_transacoes[0] + dia_11_transacoes[1] + dia_11_transacoes[2] + dia_11_transacoes[3]

print (dia_11_saldo_final)