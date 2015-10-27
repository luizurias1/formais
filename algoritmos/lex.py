from automato import Automato
from er import Er

class Lex:

    def __init__(self):
        self.identifacadores = {'Fim112': 'PR'}

    def reserved(self):
        word = ''
        automatos = []
        states = 0
        file = open('reservado.txt', 'r')
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
                    dictA = a.getDictAutomato()
                    states += len(dictA.keys()) + 1
                    automatos.append(a)
                    word = ''

        return automatos

    def lexer(self):
        automatos = self.reserved()
        for machine in automatos:
            machine.printAtomato()
            print(" ")

    # def redefineEstados(self, automatos):
    #     numeracao = 0
    #     for automato in automatos:
    #         dicionario = {}
    #         aut = {}
    #         dict = automatos.getDictAutomato()
    #         for key, value in dict.items():
    #             numeracao +=1
    #             dicionario[key] = numeracao
    #         for k, v in dict.items():
    #             aux = dicionario[k]
    #             meio = aut[aux] = {}
    #             for chave, valor in v.items():
    #                 auxx = dicionario[chave]
    #                 array = []
    #                 for item in valor:
    #                     moment = dicionario[item]
    #                     array.append(moment)
    #                 aux[auxx] = array