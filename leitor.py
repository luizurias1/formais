import json

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
				if world == 'S':
					self.completaAutomato(dict, line, transition)
		return dict 

	def completaAutomato(self, dict, line, transition):
		fileName = ''
		for element in line:
			if element == '\n':
				with open(fileName) as data_file:    
   	 				data = json.load(data_file)
   	 				for key, value in dict.items():
   	 					for k, v in value.items():
   	 						tamanho = len(data[key][k])
							for x in xrange(0,tamanho):
   	 							a = data[key][k][x]
   	 							v.append(a)
			if element not in self.rejected:
				fileName += element
	
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
automato = l.ler()