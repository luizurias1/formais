from leitor import Leitor
from determina import Automato
from grammar import Grammar

# q0 = {0: ['q0','q1'], 1: ['q0']}
# q1 = {0: ['q2'], 1: ['M']}
# q2 = {0: ['M'], 1: ['q3']}
# q3 = {0: ['M'], 1: ['M']}
# M = {0: ['M'], 1: ['M']}
# s = {'q0': q0, 'q1': q1, 'q2': q2, 'q3': q3, 'M': M}
# --------------------------------------------------
# q4 = {1: ['q4'], 2: ['M'], 3: ['M'], '&': ['q5']}
# q5 = {1: ['M'], 2: ['q5'], 3: ['M'], '&': ['q6']}
# q6 = {1: ['M'], 2: ['M'], 3: ['q6'], '&': ['M']}
# M = {1: ['M'], 2: ['M'], 3: ['M'], '&': ['M']}
# se = {'q4': q4, 'q5': q5, 'q6': q6, 'M': M}

terminal = ['a', 'b']
nTerminal = ['A', 'B', 'S']
producoes = {
    'S': ['aA', 'bB', 'a', 'b'],
    'A': ['aA', 'bA', 'a'],
    'B': ['bB', 'aB', 'b']
    }

# g = Grammar(producoes,terminal,nTerminal)
# automato = g.convertGtoAF()
# a = Automato(automato)
# print(automato)
# print(a.determina())

leitor = Leitor()
se = leitor.ler()
a = Automato(se)
automato = a.determina()
print(automato)