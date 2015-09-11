__author__ = 'lucasmpalma and luizu'

class Automato:

    def __init__(self, states, inicial, finais):
        self.automato = states
        self.d = states.copy()
        self.inicial = inicial
        self.finais = finais

    def getAlfabeto(self):
        aState = next (iter (self.automato.values()))
        alfabeto = aState.keys()
        return alfabeto

    def atualizaEstados(self, dict):
        for key, value in dict.items():
            naturalStates = self.automato.keys()
            if key not in naturalStates:
                self.automato[key] = value
        return self.automato

    def criaEstado(self, v):
        dict = {}
        novo = ''
        alfabeto = self.getAlfabeto()
        for alf in alfabeto:
            dict[alf] = []
        for valor in v:
            novo+=valor
        for item in v:
            state = self.automato.get(item)
            for key , value in state.items():
                texto = ''
                for it in value:
                    if it != 'M':
                        texto = it
                        dict[key].append(texto)
        self.d[novo] = dict

    def procuraEstados(self):
        st = []
        for key, value in self.automato.items():
            if key not in st:
                st.append(key)
        for key, value in self.automato.items():
            for k, v in value.items():
                newState =''
                for it in v:
                    if it != 'M':
                        estado = it
                        newState = newState + estado
                    if newState not in st and newState != '':
                        newState = ''
                        self.criaEstado(v)

    def calculaFecho(self):
        sFecho = {}
        for key, value in self.automato.items():
            if key !='M':
                sFecho[key] = []
        for key, value in self.automato.items():
            for k, v in value.items():
                for item in v:
                    if k == '&' and key != 'M' and item != 'M':
                        sFecho[key].append(item)
        for key, value in sFecho.items():
            for item in value:
                aux = sFecho[item]
                for it in aux:
                    value.append(it)
        for key, value in sFecho.items():
            sFecho[key].append(key)
        fe = {}
        for key, value in sFecho.items():
            fecho=''
            for item in value:
                fecho+=item
            fe[key]=fecho
        return sFecho, fe

    def atualizaAFND(self, fecho, states):
        alfabeto = self.getAlfabeto()
        chaves = states.keys()
        if self.inicial in chaves:
            aux = states[self.inicial]
            self.inicial = aux
        dt = {}
        a = []        
        for key, value in states.items():
            if len(fecho[key]) > 1:
                aux = self.automato[value] = {}
                for item in alfabeto:
                    if item != '&':
                        aux[item] = []
                        for k, v in fecho.items():
                            if k == key:
                                for it in v:
                                    s = self.automato[it]
                                    for chave, valor in s.items():
                                        for i in valor:
                                            if i not in aux[item]:
                                                if i in chaves:
                                                    a = states[i]
                                                    if item == chave:
                                                        aux[item].append(a)
                                                elif len(a) == 0:
                                                    aux[item].append('M')
        for key, value in states.items():
            if len(fecho[key]) > 1:
                del(self.automato[key])
        retorno = {}
        novo = {}
        for key, value in self.automato.items():
            for k, v in value.items():
                if k != '&':
                    novo[k] = v
            retorno[key] = novo
            novo = {}
        self.automato = retorno
        self.d = self.automato.copy()

    def determina(self):
        alfabeto = self.getAlfabeto()
        if '&' in alfabeto:
            fecho, states = self.calculaFecho()
            self.atualizaAFND(fecho, states)
            self.procuraEstados()
            while len(self.automato) != len(self.d):
                self.atualizaEstados(self.d)
                self.procuraEstados()
            return self.automato
        else:   
            self.procuraEstados()
            while len(self.automato) != len(self.d):
                self.atualizaEstados(self.d)
                self.procuraEstados()
            return self.automato

    def automataToGrammar(self):
        nonTerminais = []
        terminais = []
        prod = {}
        for k, v in self.d.items():
            if k != 'M':
                nonTerminais.append(k)
            for key, value in v.items():
                if key not in terminais:
                    terminais.append(key)
        for a in nonTerminais:
            prod[a] = []
        for k, v in self.d.items():
            if k!= 'M':
                for key, value in v.items():
                    finale = ''.join(value)
                    if finale in self.finais:
                        aux = ''.join(key)
                        prod[k].append(aux)
                        aux = ''.join(key)+(''.join(value)).upper()
                        prod[k].append(aux)
                    else:
                        aux = ''.join(key)+(''.join(value)).upper()
                        prod[k].append(aux)
        nonTerminais = [x.upper() for x in nonTerminais]
        inicial = self.inicial
        return prod, terminais, nonTerminais, inicial

    def printAtomato(self):
        print "{:<8} {:<15} ".format('S','Transition')
        for key, value in self.automato.items():
            if key == self.inicial:
                print "{:<8} {:<15} ".format('->'+''.join(key), value)
            else:    
                print "{:<8} {:<15} ".format(key, value)
