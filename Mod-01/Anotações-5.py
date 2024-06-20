saldo = 1000
saque = 500

pode_sacar = saque<=saldo
print(pode_sacar)

usuario_cadastrado = "eloyneto61@gmail.com"
senha_cadastrada = "batata-frita"
usuario = "eloyneto61@gmail.com"
senha = "batata-frita"

usuario_igual = usuario == usuario_cadastrado
senha_igual = senha == senha_cadastrada
conceder_acesso = usuario_igual & senha_igual

print(usuario_igual)
print(senha_igual)
print(conceder_acesso)