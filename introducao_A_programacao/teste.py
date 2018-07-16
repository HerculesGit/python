'''
from cliente import Cliente # nome do arquivo e nome da Classe
from contas import Conta

hercules = Cliente('Hercules silva', '83991718217')
maria = Cliente('Maria antonia', '99999999999')

print(" ==== ++ ====")
print(' {0}'.format(hercules))
print(' {0}'.format(maria))

conta = Conta([hercules,maria],1111122222,1500.90) #cliente, numero, saldo
#print(f'conta => {conta} criada')

#conta.clientes = hercules
#print(f'a conta {conta} foi a atribuida a {hercules}')

#print(f'\n\n {conta}')



#conta.resumo()


conta.deposito(100)
conta.extrato()

conta.resumo()
print(conta)
'''
from cliente import Cliente
from bancos import Banco
from contas import Conta

joao = Cliente('joao gabriel','99999')
maria = Cliente('Maria da silva', '9919191')
jose = Cliente('jose da emanoel', '8388181')

contaJM = Conta([joao],[maria],100)
contaJ = Conta


