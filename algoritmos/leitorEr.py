__author__ = 'lucasmpalma and luizu'

class LeitorEr:

    def __init__(self, fileName):
        self.fileName = fileName
        pass

    def ler(self):
        file = open('../testes/'+self.fileName, 'r')
        expression = ''
        for line in file:
            for element in line:
                expression += element
        return expression


