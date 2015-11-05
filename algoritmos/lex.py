from automato import Automato
from er import Er
import copy

class Lex:

    def __init__(self):
        self.identifacadores = {'Fim112': 'PR'}

    def reserved(self):
        word = ''
        automatos = []
        states = 0
        file = open('../algoritmos/reservado.txt', 'r')
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
                    states += len(dictA.keys()) + 1
                    automatos.append(a)
                    word = ''

        return automatos

    def lexer(self):
        automatos = self.reserved()
        first = automatos[0]
        result = first.oU(automatos, ' ')
        result.determina()
        result.organizaAutomato()
        result.montaAutomato()
        # result.printAtomato()
        result.min()
        result.printAtomato()
        return result