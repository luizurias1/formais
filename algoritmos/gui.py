__author__ = 'lucasmpalma and luizu'
import tkinter as Tk
from tkinter import ttk
from leitor import Leitor
from automato import Automato
from automato import Automato
from leitor import Leitor
from grammar import Grammar
from leitorG import LeitorG
from er import Er
from leitorEr import LeitorEr


def entradaDeterminizar():
    ttk.Label(root, text="<- arquivo .in").grid(column=10, row=1, sticky=Tk.W)
    Tk.Entry(root, width=7, textvariable=entrytext).grid(column=8, row=1, sticky=(Tk.W, Tk.E))
    input = entrytext.get()
    print(str(input))
    ttk.Button(root, text="OK", command=clicked1).grid(column=15, row=1, sticky=Tk.W)

def entradaAutomatoGramatica():
    ttk.Label(root, text="<- arquivo .in").grid(column=10, row=1, sticky=Tk.W)
    Tk.Entry(root, width=7, textvariable=entrytext).grid(column=8, row=1, sticky=(Tk.W, Tk.E))
    input = entrytext.get()
    print(str(input))
    ttk.Button(root, text="OK", command=clicked2).grid(column=15, row=1, sticky=Tk.W)

def entradaGramaticaAutomato():
    ttk.Label(root, text="<- arquivo .in").grid(column=10, row=1, sticky=Tk.W)
    Tk.Entry(root, width=7, textvariable=entrytext).grid(column=8, row=1, sticky=(Tk.W, Tk.E))
    input = entrytext.get()
    print(str(input))
    ttk.Button(root, text="OK", command=clicked3).grid(column=15, row=1, sticky=Tk.W)

def entradaERAutomato():
    ttk.Label(root, text="<- arquivo .in").grid(column=10, row=1, sticky=Tk.W)
    Tk.Entry(root, width=7, textvariable=entrytext).grid(column=8, row=1, sticky=(Tk.W, Tk.E))
    input = entrytext.get()
    print(str(input))
    ttk.Button(root, text="OK", command=clicked4).grid(column=15, row=1, sticky=Tk.W)

def entradaAutomatoER():
    ttk.Label(root, text="<- arquivo .in").grid(column=10, row=1, sticky=Tk.W)
    Tk.Entry(root, width=7, textvariable=entrytext).grid(column=8, row=1, sticky=(Tk.W, Tk.E))
    input = entrytext.get()
    print(str(input))
    ttk.Button(root, text="OK", command=clicked5).grid(column=15, row=1, sticky=Tk.W)

def clicked1():
    input = entrytext.get()
    determiniza(input)

def clicked2():
    input = entrytext.get()
    automatoGramatica(input)

def clicked3():
    input = entrytext.get()
    gramaticaAutomato(input)

def clicked4():
    input = entrytext.get()
    ERAutomato(input)

def clicked5():
    input = entrytext.get()
    automatoER(input)

def automatoGramatica(input):
    l = Leitor(input)
    dict, ini, final = l.ler()
    a = Automato(dict,ini,final)

    prod,terminais,nonTerminais,inicial = a.automataToGrammar()
    g = Grammar(prod,terminais,nonTerminais,inicial)
    g.printGrammar()
    g.writeGrammarToFile(input)

    input = input.replace('.in', '')
    data_file = open('../testes/'+input+'.out')
    data = data_file.read()
    data_file.close()
    test = Tk.Tk()
    Results = Tk.Label(test, text = data)
    Results.grid(row = 20, column = 3, sticky= Tk.W)

def gramaticaAutomato(input):
    input = entrytext.get()
    l = LeitorG(input)
    dict, termi,nonter,ini = l.ler()
    g = Grammar(dict,termi,nonter,ini)
    s, inicial, final = g.convertGtoAF()
    a = Automato(s,inicial,final)
    a.printAtomato()
    a.writeAutomataToFile(input)

    input = input.replace('.in', '')
    data_file = open('../testes/'+input+'.out')
    data = data_file.read()
    data_file.close()
    test = Tk.Tk()
    Results = Tk.Label(test, text = data)
    Results.grid(row = 20, column = 3, sticky= Tk.W)

def ERAutomato(input):
    input = entrytext.get()
    l = LeitorEr(input)
    ex = l.ler()
    er = Er(ex)

    a = er.erToAutomato()
    a.printAtomato()
    a.writeAutomataToFile(input)

    input = input.replace('.in', '')
    data_file = open('../testes/'+input+'.out')
    data = data_file.read()
    data_file.close()
    test = Tk.Tk()
    Results = Tk.Label(test, text = data, justify = 'left')
    Results.grid(row = 20, column = 3, sticky= Tk.W)
    Results.pack(fill="x")

def automatoER(input):
    input = entrytext.get()
    l = Leitor(input)
    dict, ini, final = l.ler()
    a = Automato(dict,ini,final)
    er = a.automataToER()
    expressao = Er(er)
    expressao.printER()
    expressao.writeERToFile(input)

    input = input.replace('.in', '')
    data_file = open('../testes/'+input+'.out')
    data = data_file.read()
    data_file.close()
    test = Tk.Tk()
    Results = Tk.Label(test, text = data)
    Results.grid(row = 20, column = 3, sticky= Tk.W)

def determiniza(args):
    input = entrytext.get()
    l = Leitor(input)
    dict, ini, final = l.ler()
    a = Automato(dict,ini,final)
    a.determina()
    a.printAtomato()
    a.writeAutomataToFile(input)

    input = input.replace('.in', '')
    data_file = open('../testes/'+input+'.out')
    data = data_file.read()
    data_file.close()
    test = Tk.Tk()
    Results = Tk.Label(test, text = data, )
    Results.grid(row = 20, column = 3, sticky=(Tk.W, Tk.E))


root = Tk.Tk()
entrytext = Tk.StringVar()
root.title("Palma&Urias Formais")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(Tk.N, Tk.W, Tk.E, Tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = Tk.StringVar()
meters = Tk.StringVar()

# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, /row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(Tk.W, Tk.E))
ttk.Button(mainframe, text="Determinizar", command=entradaDeterminizar).grid(column=3, row=1, sticky=Tk.W)
ttk.Button(mainframe, text="Automato para gramatica", command=entradaAutomatoGramatica).grid(column=3, row=2, sticky=Tk.W)
ttk.Button(mainframe, text="Gramatica para automato", command=entradaGramaticaAutomato).grid(column=3, row=3, sticky=Tk.W)
ttk.Button(mainframe, text="Automato para ER", command=entradaAutomatoER).grid(column=3, row=4, sticky=Tk.W)
ttk.Button(mainframe, text="ER para automato", command=entradaERAutomato).grid(column=3, row=5, sticky=Tk.W)

# ttk.Label(mainframe, text="<- arquivo .in").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind('<Return>', determinizar)

root.mainloop()