__author__ = 'lucasmpalma and luizu'
from automato import Automato
from leitor import Leitor
from grammar import Grammar
from leitorG import LeitorG
from lex import Lex
from er import Er

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
#
# A = {'a': ['B'], 'b': ['F']}
# B = {'a': ['G'], 'b': ['C']}
# C = {'a': ['A'], 'b': ['C']}
# D = {'a': ['C'], 'b': ['G']}
# E = {'a': ['H'], 'b': ['F']}
# F = {'a': ['C'], 'b': ['G']}
# G = {'a': ['G'], 'b': ['E']}
# H = {'a': ['G'], 'b': ['C']}
# s = {'A' : A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H}
# inicial = 'A'
# finais = ['C']

# automato = Automato(s, inicial, finais)
# automato.min()
# automato.printAtomato()

# A = {'a': ['M'], 'b': ['A', 'B']}
# B = {'a': ['A'], 'b': ['B']}
# C = {'a': ['C', 'D'], 'b': ['M']}
# D = {'a': ['D'], 'b': ['C']}
# S = {'a': ['A', 'C', 'D'], 'b': ['A', 'B', 'C']}
# M = {'a': ['M'], 'b': ['M']}
# s = {'A' : A, 'B': B, 'C': C, 'D': D, 'S': S, 'M': M}

# inicial = 'S'
# finais = ['C', 'A', 'B', 'D']

# automato = Automato(s, inicial, finais)
# automato.determina()
# automato.min()
# automato.printAtomato()

# P.R.O.G.R.A.M.A
# V.A.R.I.A.V.E.L
# I.N.T.E.I.R.O
# T.E.X.T.O
# A.R.R.A.N.J.O
# I.N.I.C.I.O.:
# E.N.Q.U.A.N.T.O
# C.O.N.C.L.U.I.D.O
# S.E.:
# S.E.N.A.O.:
# L.E.I.A
# M.O.S.T.R.A
# E
# O.U
# N.A.O
# F.I.N.A.L

lex = Lex()
reservadas = lex.lexer()
print(reservadas.aceita('MLEIA '))
# reservadas.printAtomato()
# reservadas.organizaAutomato()
# reservadas.determina()
# reservadas.montaAutomato()
# reservadas.min()
# reservadas.printAtomato()
# print(reservadas.getFinais())
# print(reservadas.aceita('LEIA'))
# reservadas.printAtomato()

# er = Er('((((((a|b)|c)|d)|e)|g)*)')
# automato = er.erToAutomato()
# automato.determina()
# # automato.printAtomato()
# print (automato.aceita('eaaaaaaabbbbababababagbebeaebeaebeaecacccccdaaa'))