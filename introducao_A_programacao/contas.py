class Conta:
	'conta do cliente'
	
	def __init__(self,clientes=None, numero=0, saldo=0.0):
		self.saldo = saldo
		self.clientes = clientes
		self.numero = numero
		self.operacoes = [] 		# registro de operações realizadas :- logs
		
	def resumo(self):
		print("CC número: {0:10} Saldo: {1:.2f}".format(self.numero, self.saldo))
		#print('CC Nº%s Saldo: %10.2f' %(self.numero, self.saldo))
		
	def saque (self, valor):
		if (self.saldo >= valor):
			self.saldo-=valor
			self.operacoes.append(['SAQUE', valor])
			
		else:
			print('Saque inválido. Valor maior que o saldo disponível')
		
	def deposito(self, valor):
		self.saldo+=valor
		self.operacoes.append(['DEPÓSITO',valor])
		
	def __str__(self):
		if self.clientes == None:
			client = '<sem cliente>'
		else:
			client = self.clientes
		return 'informacoes da conta\n    clientes:{0}\n    numero:{1}\n    saldo: {2:.2f}'.format(client, self.numero, self.saldo)


	def extrato(self):
		
		print(f'\n\nExtrato CC Nº {self.numero}')
		for op in self.operacoes:
			print(f'          {op[0]:10} {op[1]:10.2f}')



