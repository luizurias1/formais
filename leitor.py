class Leitor :

	def __init__(self):
		self.rejected = ['U', 'E', 'K', 'S', ' ', '=', '{', '}', ',', '(', ')', '[', ']', '>']
		pass

	def ler(self):
		file = open('entrada', 'r')
		dict = {}
		transition = []
		for line in file:
			for world in line:
				if world == 'K':
					dict = self.geraEstados(line)
				if world == 'E':
					dict, transition = self.geraAlfabeto(line, dict)
		return dict 

	def geraTransicoes(self, line, dict):
		state = ''
		for element in line:
			if element not in self.rejected:
				state += element

	def geraAlfabeto(self, line, dict):
		transition = ''
		t = []
		for element in line:
			if element == ',' or element == ')':
				for key, value in dict.items():
					value[transition] = []
				transition = ''
			if element not in self.rejected:
				transition += element
			t.append(transition)
		return dict, t 

	def geraEstados(self, line):
		state = ''
		dict = {}
		for element in line:
			if element == ',':
				dict[state] = {}
				state = ''
			if element not in self.rejected:
				state += element
		return dict
l = Leitor()
print (l.ler())