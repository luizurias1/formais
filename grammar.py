__author__ = 'luizu'

class Grammar:

    def __init__(self,producoes,terminais,nonTerminais):
        self.producoes = producoes
        self.terminais = terminais
        self.nonTerminais = nonTerminais

    def initEstados(self):
        estadosAutomato = []
        for i in self.nonTerminais:
            estadosAutomato.append(i)

        estadosAutomato.append('F')
        estadosAutomato.append('M')

        s = {}
        aux = {}
        test = {}

        for a in estadosAutomato:
            s[a] = aux
        return s


    def convertGtoAF(self):
        s = {}
        s = self.initEstados()
        transicao = ''
        estado = ''

        for key, value in self.producoes.items():
            test = {}
            for item in value:
                if item in self.terminais:
                    test[item].append('F')
                else:
                  for caracter in item:
                      if caracter in self.nonTerminais:
                          estado = caracter
                      if caracter in self.terminais:
                          transicao = caracter
                  test[transicao] = [estado]
            s[key] = test
        test = {}
        for key, value in s.items():
            if key == 'M' or  key == 'F':
                for item in self.terminais:
                    test[item] = ['M']
                s[key] = test
        return s