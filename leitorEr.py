__author__ = 'lucasmpalma'

class LeitorEr:

	def __init__(self, fileName):
		self.fileName = fileName
		pass

	def ler(self):
		file = open(self.fileName, 'r')
		expression = ''
		for line in file:
			for element in line:
				expression += element
		return expression

l = LeitorEr('entradaEr.txt')
print(l.ler())

