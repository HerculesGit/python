class Cliente:
	'classe cliente de um banco'	
	
	def __init__(self, nome='',telefone=''):
		self.nome = nome
		self.telefone = telefone
	
	def __str__(self):
		return 'cliente: {0}, telefone: {1}'.format(self.nome, self.telefone)
	
	
