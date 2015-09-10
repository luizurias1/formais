__author__ = 'lucasmpalma'

class Automato:

    def __init__(self, states):
        self.automato = states
        self.d = states.copy()

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