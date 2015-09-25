__author__ = 'lucasmpalma and luizu'
import copy
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
        ns = ''
        c = 0
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
                        for item in v:
                            if item in self.finais:
                                c += 1
                        for item in v:
                            ns += item
                        if c >= 1:
                            self.finais.append(ns)
                        ns = ''
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

    def genericAutomata(self):
        genericAutomata = copy.deepcopy(self.automato)
        #adiciona qi e aponta os finais para qf
        for key, value in self.automato.items():
            aux = {}
            aux['&'] = []
            if key == 'M':
                del(genericAutomata[key])
            if key in self.inicial:
                aux['&'].append(key)
                genericAutomata['qi'] = aux
            if key in self.finais:
               for k, v in value.items():
                   aux = copy.deepcopy(value)
                   aux['&'] = ['qf']
                   genericAutomata[key] = aux
        alfabeto = self.getAlfabeto()
        aux = {}
        #adiciona qf
        for a in alfabeto:
            aux[a] = ['M']
            genericAutomata['qf'] = aux
        return genericAutomata

    def automataToER(self):
        genericAutomata = self.genericAutomata()
        genericAux = copy.deepcopy(genericAutomata)
        x = len(genericAutomata)
        while(x>2):
            for k, v in genericAutomata.items():
                if(k != 'qi' and k!= 'qf'):
                    del(genericAutomata[k])
                    break
            #percorrendo dicionario para adequar
            for key, value in genericAux.items():
                aux = {}
                g = {}
                extra = True
                if key != k:
                    for alf, est in value.items():
                        R1, R2, R3, uniao = "", "", "", ""
                        if k in est:
                            R1 = "("+str(alf)+"."
                            for alfabetoAlcancadoPeloRem, estadosAlcancadosPeloRem in v.items():
                                uniao = ""
                                if estadosAlcancadosPeloRem in value.values() and k.split() != estadosAlcancadosPeloRem:
                                    extra = False
                                    for uniaoK, uniaoV in value.items():
                                        if uniaoV == estadosAlcancadosPeloRem:
                                            uniao = "U("+str(uniaoK)+")"
                                if k.split() in v.values() and R2 == "":
                                    for fechoK, fechoV in v.items():
                                        if fechoV == k.split():
                                            R2 = "("+str(fechoK)+")*."
                                if estadosAlcancadosPeloRem != k.split():
                                    estadofinal = estadosAlcancadosPeloRem
                                    R3 = ""+str(alfabetoAlcancadoPeloRem)
                                    expressaoFinal = R1+R2+R3+uniao+")"
                                    aux[expressaoFinal] = estadofinal
                                    genericAutomata[key] = aux

                        else:
                            g[alf] = est
                if(extra==True):
                    for chave, valor in g.items():
                        aux[chave] = valor
                genericAutomata[key] = aux
                if key == k:
                    del(genericAutomata[k])
            genericAux = copy.deepcopy(genericAutomata)
            x -= 1
        self.printER(genericAutomata)
    def printAtomato(self):
        print('{:<8} {:<15} '.format('S', 'Transition'))
        for key, value in self.automato.items():
            if key == self.inicial:
                print('{!s:<8} {!s:<15} '.format('->'+''.join(key), value))
            elif key in self.finais:
                print('{!s:<8} {!s:<15} '.format('*'+''.join(key), value))
            else:    
                print('{!s:<8} {!s:<15} '.format(key, value))

    def printER(self,ex):
        er = ''
        print('Expressao Regular do automato: ')
        for k, v in ex.items():
            for key, value in v.items():
                if value == 'qf'.split():
                    er = key.replace('&' , '')

        er = er.replace('.','')
        print(er)