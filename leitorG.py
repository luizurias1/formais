import json

class LeitorG:

	def  __init__(self):
		self.rejected = ['', 'P', 'N', 'T', ' ', '=', '{', '}', ',', '(', ')', '[', ']', '>']
		pass

	def ler(self):
		file = open('entradaG.txt', 'r')
		dict = {}
		terminais = []
		for line in file:
			for world in line:
				if world == 'T':
					terminais = self.getaT(line)
				if world == 'N':
					naoTerminais, gramatica = self.geraNT(line)
				if world == 'P':
					self.completaGramatica(line, gramatica)
		return gramatica, terminais, naoTerminais

	def completaGramatica(self, line, gramatica):
		fileName = ''
		for element in line:
			if element == '\n':
				with open(fileName) as data_file:    
   	 				data = json.load(data_file)
   	 				for key, value in gramatica.items():
   	 					aux = data[key]
   	 					tamanho = len(aux)
   	 					for x in range(0,tamanho):
   	 						gramatica[key].append(data[key][x])
			if element not in self.rejected:
				fileName += element	
	
	def geraNT(self, line):
		nt = ''
		nts = []
		gramatica = {}
		for element in line:
			if element == ',' or element == '}':
				nts.append(nt)
				gramatica[nt] = []
				nt = ''
			if element not in self.rejected:
				nt += element
		return nts, gramatica

	def getaT(self, line):
		t = ''
		ts = []
		for element in line:
			if element == ',' or element == '}':
				ts.append(t)
				t = ''
			if element not in self.rejected:
				t += element
		return ts