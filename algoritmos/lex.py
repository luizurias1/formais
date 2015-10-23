from automato import Automato
from er import Er

class Lex:

    def __init__(self):
        self.identifacadores = {'Fim112': 'PR'}

    def reserved(self):
        word = ''
        automatos = []
        states = 0
        file = open('algoritmos/reservado.txt', 'r')
        for line in file:
            for element in line:
                if element != '\n':
                    word += element
                if element == '\n':
                    e = Er(word)
                    e.inicialCase(states)
                    a = e.erToAutomato()
                    dictA = a.getDictAutomato()
                    a.determina()
                    a.min()
                    a.completaAutomato()
                    dictA = a.getDictAutomato()
                    states += len(dictA.keys()) +1
                    automatos.append(a)
                    word = ''

        return automatos

    def lexer(self):
        automatos = self.reserved()
        automatoInicial = automatos[0]
        automatoFinalzasso = automatoInicial.oU(automatos)
        automatoFinalzasso.determina()
        automatoFinalzasso.putAlfabetAndMorto()
        automatoFinalzasso.stateOfError()
        automatoFinalzasso.printAtomato()
        aceita, estado = automatoFinalzasso.aceita('NAO')
        print(len(automatoFinalzasso.getFinais()))
        self.token(estado,'NAO')
    def token(self,estado, palavra):
        file = open('algoritmos/tokens.txt', 'w')
        file.write('<'+palavra+','+self.identifacadores[estado]+'>')
        print('<'+palavra+','+self.identifacadores[estado])
