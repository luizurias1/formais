__author__ = 'lucasmpalma and luizu'
from automato import Automato

class Er:

    '''
    Construtor da classe Er
    self.expression, expressao regular em formato de estring
    '''
    def __init__(self, elementos):
        self.expression = elementos
        self.operacoes = ['|', '.', '*']
        self.alfabeto = []
        self.number = 0
    '''
    Aumenta em uma unidade o numero de casos na expressao regular
    '''
    def oneMoreCase(self):
        self.number += 1
    '''
    Em um loop em expression a quantidade de operacoes necessarias
    e os automatos que devem ser criados
    '''
    def erToAutomato(self):
        contador = 0
        pilhaOp = []
        auts = []
        done = ''

        for element in self.expression:
            if element not in self.operacoes:
                if element != ')' and element != '(' and element not in self.alfabeto and element != '\n':
                    self.alfabeto.append(element)

        for element in self.expression:
            if element == '(':
                contador += 1
            if element == ')':
                contador -= 1
                if pilhaOp != []:
                    op = pilhaOp.pop()
                    if op == '|':
                        a = auts.pop()
                        b = auts.pop()
                        result = self.toOu(a,b)
                        auts.append(result)
                    if op == '*':
                        a = auts.pop()
                        result = self.toFecho(a)
                        auts.append(result)
                    if op == '.':
                        a = auts.pop()
                        b = auts.pop()
                        result = self.toConcatenation(b,a)
                        auts.append(result)
            if element in self.operacoes:
                done += element
                pilhaOp.append(element)
            if element in self.alfabeto:
                done += element
                automato, inicial, finais  = self.toBasic(element)
                result = Automato(automato, inicial, finais)
                auts.append(result)

        while pilhaOp != []:
            op = pilhaOp.pop()
            if op == '|':
                a = auts.pop()
                b = auts.pop()
                result = self.toOu(a,b)
                auts.append(result)
            if op == '*':
                a = auts.pop()
                result = self.toFecho(a)
                auts.append(result)
            if op == '.':
                a = auts.pop()
                b = auts.pop()
                result = self.toConcatenation(b,a)
                auts.append(result)
        finar = auts.pop()
        return self.organizeErToAutomato(finar)

    '''
    Cria um automato para um caso basico, um automato que aceita um element do alfabeto
    @return automato, Inicial e final para o automato
    @return inicial
    @return finais
    '''
    def toBasic(self, element):
        self.oneMoreCase()
        automato = {}
        Morto = {}
        Morto = {element : Morto}
        automato['Fim' + str(self.number)] = {element : ['M']}
        automato['Ini' + str(self.number)] = {element : ['Fim' + str(self.number)]}
        automato['M'] = {element : ['M']}
        inicial = 'Ini' + str(self.number)
        finais = ['Fim' + str(self.number)]
        return automato, inicial, finais

    '''
    Gera um novo automato que e a operacao de | entre 2 automatos
    @param a, automato 1
    @param b, automato 2
    @return aut, resultado de a|b
    '''
    def toOu(self, a, b):
        self.oneMoreCase()
        dictA = a.getDictAutomato()
        dictB = b.getDictAutomato()
        inicialA = a.getInicial()
        inicialB = b.getInicial()
        finaisA = a.getFinais()
        finaisB = b.getFinais()
        automato = {}
        automato['Ou' + str(self.number)] = {'&': [inicialA, inicialB]}
        ini = 'Ou' + str(self.number)
        fins = []
        for state in finaisA:
            fins.append(state)
        for state in finaisB:
            fins.append(state)
        for key, value in dictA.items():
            automato[key] = value
        for key, value in dictB.items():
            automato[key] = value
        aut = Automato(automato, ini, fins)
        return aut

    '''
    Gera um novo automato que e a operacao de * com um automato
    @param a, automato
    @return aut, automato resultado a*
    '''
    def toFecho(self, a):
        self.oneMoreCase()
        inicialA = a.getInicial()
        finaisA = a.getFinais()
        dictA = a.getDictAutomato()
        automato = {}
        automato['Fecho' + str(self.number)] = {'&': [inicialA]}
        fins = []
        fins.append(inicialA)
        ini = 'Fecho' + str(self.number)
        for state in finaisA:
            fins.append(state)
            aux = dictA[state]
            if '&' not in aux.keys():
                aux['&'] = [ini]
            else:
                aux['&'].append(ini)
        for key, value in dictA.items():
            automato[key] = value
        aut = Automato(automato, ini, fins)
        return aut

    '''
    Gera um automato que e a operacao . entre dois automatos passados
    @param a, automato a
    @param b, automato b
    @return aut, automato resultado de a.b
    '''
    def toConcatenation(self, a, b):
        self.oneMoreCase()
        automato = {}
        dictA = a.getDictAutomato()
        dictB = b.getDictAutomato()
        finaisA = a.getFinais()
        inicialB = b.getInicial()
        for key, value in dictA.items():
            aux = automato[key] = value
            if key in finaisA:
                if '&' not in aux.keys():
                    aux['&'] = [inicialB]
                else:
                    aux['&'].append(inicialB)
        for key, value in dictB.items():
            automato[key] = value
        ini = a.getInicial()
        fins = []
        for state in b.getFinais():
            fins.append(state)
        aut = Automato(automato, ini, fins)
        return aut

    def printER(self):
        print(self.expression)

    def writeERToFile(self,file):
        file = file.replace('.in', '')
        f = open('../testes/'+file+'.out', 'w')
        f.write('Expressao Regular: \n'+self.expression)
        f.close()

    def organizeErToAutomato(self, automato):
        dictA = automato.getDictAutomato()
        for key, value in dictA.items():
            for item in self.alfabeto:
                if item not in value.keys():
                    value[item] = ['M']
            if '&' not in value.keys():
                value['&'] = ['M']
        return automato