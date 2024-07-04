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
