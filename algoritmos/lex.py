from automato import Automato
from er import Er

class lexer:

	def __init__(self):
		pass

	def reserved(self):
		word = ''
		automatos = []
		states = 0
		file = open('reserved', 'r')
		for line in file:
			for element in line:
				if element != '\n':
					word += element
				if element == '\n':
					e = Er(word)
					e.inicialCase(states)
					a = e.erToAutomato()
					dictA = a.getDictAutomato()
					states = len(dictA.keys())
					a.determina()
					automatos.append(a)
					word = ''

		return automatos

l = lexer()
automatos = l.reserved()
for item in automatos:
	item.printAtomato()
	print(" ")