__author__ = 'luizu'
class Grammar:

    def __init__(self,producoes,terminais,nonTerminais,ini):
        self.producoes = producoes
        self.terminais = terminais
        self.nonTerminais = nonTerminais
        self.ini = ini

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

        # a = Automato(s,self.ini,['F'])
        # a.writeAutomataToFile()
        return s, self.ini,['F']

    def printGrammar(self):
        string = ''
        for key, value in self.producoes.items():
            right = ''
            for array in value:
                right += str(array) + '|'
            string+=str(key.upper()) + ' -> '+ right +'\n'

        print('Gramatica do automato: \n')
        print('Estado inicial: '+ self.ini.upper()+'\n')
        print('Terminais: '+str(self.terminais)+'\n')
        print('Nao terminais: '+str(self.nonTerminais)+'\n')
        print('Producoes: '+'\n'+string+'\n')

    def writeGrammarToFile(self,file):
        string = ''
        for key, value in self.producoes.items():
            right = ''
            for array in value:
                right += str(array) + '|'
            string+=str(key.upper()) + ' -> '+ right +'\n'

        file = file.replace('.in', '')
        f = open('testes/'+file+'.out', 'w')
        f.write('Gramatica do automato: \n')
        f.write('Estado inicial: '+ self.ini.upper()+'\n')
        f.write('Terminais: '+str(self.terminais)+'\n')
        f.write('Nao terminais: '+str(self.nonTerminais)+'\n')
        f.write('Producoes: '+'\n'+string+'\n')
        f.close()

