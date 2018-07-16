class Banco:
	def __init__(self, nome):
		self.nome = nome
		self.clientes = []
		self.contas = []
		
	def abre_conta(self,conta):
		self.contas.append(conta)
		
	
	def lista_contas(self):
		for x in self.contas:
			x.resumo 
