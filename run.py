from automato import Automato
from leitor import Leitor
from grammar import Grammar
from leitorG import LeitorG

# ---------------------------------------------------
q0 = {0: ['q0','q1'], 1: ['q0']}
q1 = {0: ['q2'], 1: ['M']}
q2 = {0: ['M'], 1: ['q3']}
q3 = {0: ['M'], 1: ['M']}
M = {0: ['M'], 1: ['M']}
se = {'q0': q0, 'q1': q1, 'q2': q2, 'q3': q3, 'M': M}
inicial = 'q0'
finais = ['q3']
# -------------------------------------------------
# q0 = {'a': ['M'], 'b': ['M'], '&': ['q1', 'q3']}
# q1 = {'a': ['q2'], 'b': ['q1'], '&': ['M']}
# q2 = {'a': ['q1'], 'b': ['q2'], '&': ['M']}
# q3 = {'a': ['q3'], 'b': ['q4'], '&': ['M']}
# q4 = {'a': ['q4'], 'b': ['q5'], '&': ['M']}
# q5 = {'a': ['q5'], 'b': ['M'], '&': ['M']}
# M = {'a': ['M'], 'b': ['M'], '&': ['M']}
# se = {'q0': q0, 'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5, 'M': M}
# inicial = 'q0'
# finais = ['q1', 'q4', 'q5']
#---------------------------------------------------
# q4 = {1: ['q4'], 2: ['M'], 3: ['M'], '&': ['q5']}
# q5 = {1: ['M'], 2: ['q5'], 3: ['M'], '&': ['q6']}
# q6 = {1: ['M'], 2: ['M'], 3: ['q6'], '&': ['M']}
# M = {1: ['M'], 2: ['M'], 3: ['M'], '&': ['M']}
# se = {'q4': q4, 'q5': q5, 'q6': q6, 'M': M}
# inicial = 'q4'
# finais = ['q6']
#----------------------------------------------------

#Automata to grammar
#
# q0 = {'a': ['q1'], 'b': ['q2']}
# q1 = {'a': ['q0'], 'b': ['q3']}
# q2 = {'a': ['q3'], 'b': ['q0']}
# q3 = {'a': ['q2'], 'b': ['q1']}
# M = {'a': ['M'], 'b': ['M']}
# se = {'q0': q0, 'q1': q1, 'q2': q2, 'q3': q3, 'M': M}
# inicial = 'q0'
# finais = ['q1']

# terminal = ['a', 'b']
# nTerminal = ['A', 'B', 'S']
# producoes = {
#     'S': ['aA', 'bB', 'a', 'b'],
#     'A': ['aA', 'bA', 'a'],
#     'B': ['bB', 'aB', 'b']
#     }
# inicial = 'S'
#Automata to ER
# q1 = {'a': ['q2'], 'b': ['M']}
# q2 = {'a': ['q2'], 'b': ['q3']}
# q3 = {'a': ['q2'], 'b': ['q3']}
# se = {'q1': q1, 'q2': q2, 'q3': q3}
# inicial = 'q1'
# finais = ['q2']

#Comeca e termina com a mesma letra
# q0 = {'a': ['q1'], 'b': ['q2']}
# q1 = {'a': ['q1'], 'b': ['q3']}
# q2 = {'a': ['q4'], 'b': ['q2']}
# q3 = {'a': ['q1'], 'b': ['q3']}
# q4 = {'a': ['q4'], 'b': ['q2']}
# se = {'q0' : q0, 'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4}
# inicial = 'q0'
# finais = ['q1', 'q2']

# leitorg = LeitorG()
# producoes, terminais, nTerminais = leitorg.ler()
# g = Grammar(producoes,terminal,nTerminal, inicial)
# g.convertGtoAF()
# automato = g.convertGtoAF()
# a = Automato(automato)
# print(automato)
# print(a.determina())

# leitor = Leitor()
# se, inicial, finais = leitor.ler()
# a = Automato(se, inicial, finais)
# a.automataToER()
# a.printAtomato()

a = Automato(se, inicial, finais)
a.determina()
a.writeAutomataToFile()

# a.printAtomato()
# a.automataToER()
# a.printAtomato()
# prod, termi, non, inici = a.automataToGrammar()
# print(prod)
# print(termi)
# print(non)
# print(inici)