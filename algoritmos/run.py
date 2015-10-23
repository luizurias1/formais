__author__ = 'lucasmpalma and luizu'
from automato import Automato
from leitor import Leitor
from grammar import Grammar
from leitorG import LeitorG

# Comeca e termina com a mesma letra
# q0 = {'a': ['q1'], 'b': ['q2']}
# q1 = {'a': ['q1'], 'b': ['q3']}
# q2 = {'a': ['q4'], 'b': ['q2']}
# q3 = {'a': ['q1'], 'b': ['q3']}
# q4 = {'a': ['q4'], 'b': ['q2']}
# se = {'q0' : q0, 'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4}
# inicial = 'q0'
# finais = ['q1', 'q2']
#
# # comeca e termina com a
# q5 = {'a': ['q6'], 'b': ['M']}
# q6 = {'a': ['q6', 'q7'], 'b': ['q6']}
# q7 = {'a': ['M'], 'b': ['M']}
# M = {'a': ['M'], 'b': ['M']}
# s = {'q5' : q5, 'q6': q6, 'q7': q7, 'M': M}
# ini = 'q5'
# fins = ['q7']

# para minimizar
A = {'a': ['B'], 'b': ['F']}
B = {'a': ['G'], 'b': ['C']}
C = {'a': ['A'], 'b': ['C']}
D = {'a': ['C'], 'b': ['G']}
E = {'a': ['H'], 'b': ['F']}
F = {'a': ['C'], 'b': ['G']}
G = {'a': ['G'], 'b': ['E']}
H = {'a': ['G'], 'b': ['C']}
ses = {'A' : A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H}
inicial1 = 'A'
finais1 = ['C']
# a = Automato(se, inicial, finais)
# b = Automato(s, ini, fins)
c = Automato(ses,inicial1,finais1)
c.min()
c.printAtomato()
# automatos = [b]
# resultado = a.oU(automatos)
# resultado.printAtomato()
# print a.aceita('abbbabababbbababbba')

