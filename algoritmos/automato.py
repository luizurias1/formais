__author__ = 'lucasmpalma and luizu'
import copy

class Automato:
    
    '''
    Construtor da classe automato
    self.automato, dicionario com as transicoes e alfabeto
    self.d, copia do dicionario par uso na comparacao na adicao de novos estados
    self.inicial, estado inicial do AFD ou AFND
    self.finais, conjunto dos estados aceitadores
    self.fecho e self.states, em caso de AFND guardam a estrutura do calculo do fecho &
    '''
    def __init__(self, states, inicial, finais):
        self.automato = states
        self.d = copy.deepcopy(states)
        self.inicial = inicial
        self.finais = finais
        self.fecho = {}
        self.states = {}
        self.equivalents = []

    '''
    Identifica o alfabeto do automato
    @return, array com os elementos do alfabeto
    '''
    def getAlfabeto(self):
        alfabeto = []
        for k,v in self.automato.items():
            for key, value in v.items():
                if key not in alfabeto:
                    alfabeto.append(key)
        
        return alfabeto

    '''
    Adiciona o novo estado encontrado na determinizacao ao dicionario de estados
    @return o dicionario self.automato atualizado
    '''
    def atualizaEstados(self):
        for key, value in self.d.items():
            naturalStates = self.automato.keys()
            if key not in naturalStates:
                self.automato[key] = value
        
        return self.automato

    def removeInalc(self):
        estados = []
        notAlcan = []
        
        for key, value in self.automato.items():
            if key != self.inicial:
                estados.append(str(key))

        notAlcan = copy.deepcopy(estados)
        
        for k, v in self.automato.items():
            for key, value in v.items():
                for est in value:
                    if est in notAlcan and est != k:
                            notAlcan.remove(est)


        for limpa in notAlcan :
                estados.remove(limpa)

        estadosFim = []
        estadosAux = []
        for a in estados:
            if a in self.finais:
                estadosFim.append(a)
            else:
                estadosAux.append(a)
        for a in notAlcan:
            del(self.automato[a])
        if self.inicial in self.finais and self.inicial not in estadosFim:
            estadosFim.append(self.inicial)
        elif self.inicial not in estadosAux and self.inicial not in estadosFim:
            estadosAux.append(self.inicial)

        estados = []
        estados.append(estadosAux)
        estados.append(estadosFim)
        self.equivalents = estados


    def classEquivalents(self):
        self.removeInalc()
        mudou = copy.deepcopy(self.equivalents)
        classes = self.equivalents
        nwArray = []
        newArray = nwArray
        alocados = []
        arrayFinal = ['']
        unicos = []

        while(arrayFinal != classes):
            for alf in self.getAlfabeto():
                for item in classes:
                    if len(item) > 1:
                        for element in item:
                            if element == 'M':
                                newArray.append([element])
                                unicos.append(element)
                            else:
                                aux = self.automato[element]
                                next = aux[alf][0]
                                if not newArray:
                                    newArray.append([element])
                                else:
                                    for array in newArray:
                                        for x in array:
                                            if (x in self.finais and element in self.finais) or (x not in self.finais and element not in self.finais):
                                                aux2 = self.automato[x]
                                                next2 = aux2[alf][0]
                                                if x not in unicos:
                                                    if self.isEquivalent(next,next2):
                                                        if element not in array and element not in alocados:
                                                            array.append(element)
                                                            alocados.append(element)
                                    if element not in alocados:
                                        newArray.append([element])
                                        alocados.append(element)
                    else:
                        newArray.append(item)
                        unicos.append(item[0])

                arrayFinal = classes
                classes = newArray
                self.equivalents = newArray
                newArray = []
                alocados = []
                unicos = []

        return arrayFinal,mudou

    def equivalents2(self):
        boolean = []
        self.removeInalc()
        mudou = copy.deepcopy(self.equivalents)
        classes = self.equivalents
        newArray = []
        arrayFinal = ['']
        novo = []
        unicos = []
        morto = False
        for m in classes:
            if 'M' in m:
                m.remove('M')
                morto = True

        if morto == True:
            classes.append(['M'])

        while(arrayFinal != classes):
            for item in classes:
                for element in item:
                    if len(item) > 1:
                        if not newArray:
                            newArray.append([element])
                        else:
                            conta = 0
                            for array in newArray:
                                if ''.join(array) not in unicos:
                                    primeiro = array[0]
                                    if element != primeiro:
                                        for alf in self.getAlfabeto():
                                            aux = self.automato[primeiro]
                                            next = aux[alf][0]
                                            aux2 = self.automato[element]
                                            next2 = aux2[alf][0]
                                            if self.isEquivalent(next2,next):
                                                boolean.append(True)
                                            else:
                                                boolean.append(False)
                                        if False not in boolean and element not in array:
                                            array.append(element)
                                        boolean = []
                            for array in newArray:
                                if element in array:
                                    novo.append(True)
                                else:
                                    novo.append(False)
                            if True not in novo:
                                newArray.append([element])
                            novo = []
                    else:
                        newArray.append(item)
                        unicos.append(item[0])
            print(newArray)
            arrayFinal = classes
            classes = newArray
            self.equivalents = newArray
            newArray = []
        return arrayFinal, mudou

    def min(self):
        classes, mudou = self.equivalents2()
        chave = ''
        dic = {}
        if classes != mudou:
            for i in classes:
                for j in i:
                    chave+=j
                aux = dic[chave] = {}

                for j in i:
                    estado = self.automato[j]
                    for k, v in estado.items():
                      for a in v:
                          for next in self.equivalents:
                              if a in next:
                                aux[k] = next
                              if self.inicial in next:
                                  self.inicial = ''.join(next)
                chave = ''

            self.automato = dic
            # self.organizaAutomato()
            self.montaAutomato()

    def isEquivalent(self,a,b):
        verdade = False
        for item in self.equivalents:
            if a in item and b in item:
                verdade = True
                return verdade
            else:
                verdade = False
        return verdade

    def montaAutomato(self):

        help = copy.deepcopy(self.automato)
        for k, v in help.items():
            aux= self.automato[k]
            for key, value in v.items():
                string = ''
                if len(value) > 1:
                    for array in value:
                        string+=array
                        aux[key] = string.split()

    def organizaAutomato(self):

        for key, value in self.automato.items():
            if value != {}:
                for k, v in value.items():
                    for item in self.getAlfabeto():
                        if item not in value.keys():
                            value[item] = ['M']
                        if v == []:
                            v.append('M')
            else:
                for item in self.getAlfabeto():
                    value[item] = ['M']

        m = {}
        for a in self.getAlfabeto():
            m[a] = ['M']
        self.automato['M'] = m
        self.completaAutomato()

    '''
    Recebe um array com a configuracao de estados novos, cria um dicionario para ele
    '''
    def criaEstado(self, v):
        if v == []:
            self.atualizaEstados(self.d)
        else:
            dict = {}
            novo = ''
            jaTa = []
            alfabeto = self.getAlfabeto()
            for alf in alfabeto:
                dict[alf] = []
            for valor in v:
                for key, value in self.states.items():
                    if valor == value:
                        for item in self.fecho[key]:
                            if item not in jaTa:
                                jaTa.append(item)
                                novo += item
            jaTa = []

            for item in v:
                state = self.automato.get(item)
                for key , value in state.items():
                    texto = ''
                    for it in value:
                        if it != 'M':
                            texto = it
                            if texto not in dict[key]:
                                dict[key].append(texto)
            fim = {}

            for key, value in dict.items():
                guard = fim[key] = []
                jaTa = []
                alone = []
                for item in value:
                    for chave, valor in self.states.items():
                        if item == valor:
                            if len(self.fecho[chave]) > 1:
                                guard.append(item)
                                for i in self.fecho[chave]:
                                    jaTa.append(i)
                            else:
                                alone.append(item)

                for s in alone:
                        if s not in jaTa:
                            guard.append(s)

            self.d[novo] = fim.copy()

    '''
    Realiza uma busca no dicionario de estados, procurando possivei novos estados
    Se encontrado, chama criaEstado, para que se possa criar um novo dicionario
    '''
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

    def completaAutomato(self):
        for k, v in self.automato.items():
            for key, value in v.items():
                for alf in self.getAlfabeto():
                    if alf not in v.keys():
                        v[alf] = ['M']

    def aceita(self, palavra):
        c = 0
        alfabeto = self.getAlfabeto()
        for key, value in self.automato.items():
            for k, v in value.items():
                if len(v) > 1:
                    c +=1

        aux = self.automato[self.inicial]
        estadoAtual = ''
        for letra in palavra:
            if letra in aux.keys():
                for item in aux[letra]:
                    estadoAtual = item
                    aux = self.automato[estadoAtual]
            else:
                return False
        if estadoAtual in self.finais:
            return True,estadoAtual
        else:
            return False

    def oU(self, automatos, separador):
        result = {}
        newInicial = {}
        fimUnico = {}
        newInicial['&'] = []
        iniciais = []
        iniciais.append(self.inicial)
        finais = []
        alfabetoNew = []

        for aut in automatos:
            alf = aut.getAlfabeto()
            for alfabeto in alf:
                if alfabeto not in alfabetoNew:
                    alfabetoNew.append(alfabeto)

        for aut in automatos:
            aux = aut.getFinais()
            for state in aux:
                if state not in finais:
                    finais.append(state)

        for a in self.getAlfabeto():
            newInicial[a] = []
            fimUnico[a] = ['M']


        for aut in automatos:
            x = {}
            ini = aut.getInicial()
            if ini not in iniciais:
                iniciais.append(ini)
                x = aut.getDictAutomato()
            for key, value in x.items():
                for k, v in value.items():
                    fimUnico[k] = ['M']
                    if k not in newInicial.keys():
                        newInicial[k] = []

        result['ini'] = newInicial
        result['fU'] = fimUnico

        for aut in automatos:
            x = aut.getDictAutomato()
            for key, value in x.items():
                if key not in result.keys():
                    result[key] = value
        
        for key, value in self.automato.items():
            if key not in result.keys():
                result[key] = value
            if key in self.finais and key not in finais:
                finais.append(key)

        for state in iniciais:
            aux = result['ini']
            aux['&'].append(state)

        for key, value in newInicial.items():
            if len(value) == 0:
                newInicial[key].append('M')

        for f in finais:
            aux = result[f]
            aux[separador] = ['fU']

        for k,v in result.items():
            for alf in alfabetoNew:
                if alf not in v.keys():
                    v[alf] = ['M']
        finais = ['fU']
        r = Automato(result, 'ini', finais)

        return r
    '''
    Uma vez Identificado a necessidade do calculo do fecho, o metodo
    procura o conjunto de estados referentes ao fecho de cada um dos
    estados do AFND.
    @return sFecho, dicionario do fecho, CHAVE -> [E, S, T, A, D, O, S]
    @return fe, dicionario do fecho, CHAVE -> [ESTADOS]
    '''
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
                    if it not in value:
                        value.append(it)
        
        for key, value in sFecho.items():
            if key not in sFecho[key]:
                sFecho[key].append(key)
        
        fe = {}
        
        for key, value in sFecho.items():
            fecho=''
            for item in value:
                fecho+=item
            fe[key]=fecho
        return sFecho, fe

    '''
    Atualiza o dicionario de estados com os novos estados, descubertos apos
    o calculo do fecho em uma AFND com & transicoes
    '''
    def atualizaAFND(self, fecho, states):
        dicAux = {}
        
        for key, value in states.items():
            if len(fecho[key]) > 1:
                dicAux[value] = {}
        
        for alf in self.getAlfabeto():
            if alf !='&':
                for key, value in dicAux.items():
                    value[alf] = []

        for key, value in dicAux.items():
            for k, v in value.items():
                for chave, valor in states.items():
                    if valor == key:
                        aux = fecho[chave]
                        for item in aux:
                            if len(fecho[item]) == 1:
                                take = self.automato[item]
                                for ch, vl in take.items():
                                    for i in vl:
                                        if i not in v and i != 'M' and k == ch:
                                            if i in states.keys():
                                                v.append(states[i])
                                            else:
                                                v.append(i)
                            else:
                                take = self.automato[item]
                                for ch, vl in take.items():
                                    for i in vl:
                                        if i not in v and i != 'M' and k == ch:
                                            t = states[i]
                                            v.append(t)
            for k, v in value.items():
                if len(v) == 0:
                    v.append('M')
            
        for key, value in self.automato.items():
            alf = value.keys()
            aux = []
            for its in alf:
                if its != '&':
                    aux.append(its)
            if key != 'M':
                if key not in dicAux.keys() and len(fecho[key]) == 1:
                    a = dicAux[key] = {c:value[c] for c in aux}
                    for k, v in value.items():
                        array = []
                        for item in v:
                            if item != 'M' and len(fecho[item]) > 1:
                                array.append(states[item])
                            else:
                                array.append(item)
                        for chave, valor in a.items():
                            if k != '&' and chave == k:
                                a[k] = array
        
        current_dict = {}
        
        for key, value in dicAux.items():
            aux = []
            st = self.automato.keys()
            current_sub = current_dict[key] = {}
            for k, v in value.items():
                going = current_sub[k] = []
                aux = []
                for item in v:
                    text = ''
                    for m in st:
                        if m in item:
                            if m not in aux:
                                aux.append(m)
                    for it in item:
                        text += it
                        if text in st:
                            if text not in aux:
                                aux.append(text)
                                text = ''
                for i in aux:
                    if i not in going:
                        going.append(i)

        finalDict = current_dict.copy()
        sta = []
        sa = ''
       
        for key, value in current_dict.items():
            aux = finalDict[key]
            for k, v in value.items():
                moment = aux[k] = []
                for item in v:
                    if item != 'M':
                        sta.append(item)
                for chave, valor in fecho.items():
                    if set(sta) == set(valor):
                        guardar = states[chave]
                        sta = []
                        if guardar not in moment:
                            moment.append(guardar)
                sta = []
                if moment == []:
                    for item in v:
                        if item != 'M':
                            sa += item
                            if sa in states.values():
                                moment.append(sa)
                                sa = ''
                if moment == []:
                    moment.append('M')

        self.automato = finalDict.copy()
        self.d = finalDict.copy()
        self.inicial = self.states[self.inicial]
        finalAtual = []
        
        for key, value in self.states.items():
            for state in self.finais:
                if key == state:
                    finalAtual.append(value)
        self.finais = finalAtual

    '''
    Ordena a sequencia de metodos necessarios para a determinizacao, 
    que varia de AFND para AFD, em um loop ate que nao hajam novos
    estados para adicionar
    @return, self.automato atualizado
    '''
    def determina(self):
        alfabeto = self.getAlfabeto()
        if '&' in alfabeto:
            self.fecho, self.states = self.calculaFecho()
            self.atualizaAFND(self.fecho, self.states)
            self.procuraEstados()
            while len(self.automato) != len(self.d):
                self.atualizaEstados()
                self.procuraEstados()
            self.organizaAutomato()
            return self.automato
        else:
            self.fecho, self.states = self.calculaFecho()   
            self.procuraEstados()
            while len(self.automato) != len(self.d):
                self.atualizaEstados()
                self.procuraEstados()
            self.organizaAutomato()
            return self.automato

    '''
    Metodo que gera a gramatica do automato criado pelo construtor.
    @return prod
    @return terminais
    @return nonTerminais
    @return inicial
    '''
    def automataToGrammar(self):
        nonTerminais = []
        terminais = []
        prod = {}
        morto = []
        for k, v in self.automato.items():
            if k != 'M':
                for key, value in v.items():
                    if 'M'.split() not in value:
                        if k not in nonTerminais:
                            nonTerminais.append(k)
                    if key not in terminais:
                        terminais.append(key)
                    if all(x == 'M'.split() for x in v.values()):
                        morto.append(k)

        for abc in nonTerminais:
            if abc in morto:
                nonTerminais.remove(abc)
        for a in nonTerminais:
            if a not in morto:
                prod[a] = []
        for k, v in self.automato.items():
            if k!= 'M':
                for key, value in v.items():
                    if value != 'M'.split():
                        finale = ''.join(value)
                        if finale in self.finais:
                            aux = ''.join(key)
                            prod[k].append(aux)
                            if finale not in morto:
                                aux = ''.join(key)+(''.join(value)).upper()
                                prod[k].append(aux)
                        elif finale not in morto:
                            aux = ''.join(key)+(''.join(value)).upper()
                            prod[k].append(aux)
        nonTerminais = [x.upper() for x in nonTerminais]
        inicial = self.inicial

        return prod,terminais,nonTerminais,inicial

    '''
    Metodo que transforma o objeto automato em um automato generico.
    @ return genericAutomata
    '''
    def genericAutomata(self):
        generic = copy.deepcopy(self.automato)
        c = 0
        for k, v in self.automato.items():
            for key, value in v.items():
                if len(value) > 1:
                    c += 1
        if c >= 1:
            generic = self.determina()

        genericAutomata = copy.deepcopy(generic)

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

    '''
    Metodo que converte o automato da classe em uma expressao regular
    @return a expressao regular do automato
    '''
    def automataToER(self):
        genericAutomata = self.genericAutomata()
        print(genericAutomata)
        genericAux = copy.deepcopy(genericAutomata)
        x = len(genericAutomata)
        while(x>2):
            for k, v in genericAutomata.items():
                if(k != 'qi' and k!= 'qf'):
                    del(genericAutomata[k])
                    break
            print('Estado a ser removido: '+str(k))
            #percorrendo dicionario para adequar
            for key, value in genericAux.items():
                aux = {}
                g = {}
                if key != k:
                    for alf, est in value.items():
                        R1, R2, R3, uniao, R21, p1, p2 = "", "", "", "", "",'',''
                        for array in est:
                            if array == k:
                                R1 = "("+str(alf)+"."
                                for alfabetoAlcancadoPeloRem, estadosAlcancadosPeloRem in v.items():
                                    uniao, p1,p2 = "",'',''
                                    if estadosAlcancadosPeloRem in aux.values():
                                        for keyAux, valueAux in aux.items():
                                            if valueAux == estadosAlcancadosPeloRem:
                                                chavedeletar = keyAux
                                        del(aux[chavedeletar])
                                    if estadosAlcancadosPeloRem in value.values() and k.split() != estadosAlcancadosPeloRem:
                                        for uniaoK, uniaoV in value.items():
                                            if uniaoV == estadosAlcancadosPeloRem:
                                                uniao = "|("+str(uniaoK)+')'
                                        p1 = '('
                                        p2 = ')'
                                    if k.split() in v.values() and R2 == "":
                                        for fechoK, fechoV in v.items():
                                            if fechoV == k.split():
                                                    R21 += str(fechoK)+'|'
                                        R2 = "("+R21+")*."
                                        R2 = R2.replace('|)', ')')
                                    if estadosAlcancadosPeloRem != k.split():
                                        estadofinal = estadosAlcancadosPeloRem
                                        R3 = ""+str(alfabetoAlcancadoPeloRem)+")"
                                        expressaoFinal = p1+R1+R2+R3+uniao+p2
                                        aux[expressaoFinal] = estadofinal

                            else:
                                if array.split() not in aux.values():
                                    aux[alf] = array.split()

                genericAutomata[key] = aux
                if k == key:
                    del (genericAutomata[key])
            print(genericAutomata)
            genericAux = copy.deepcopy(genericAutomata)
            x -= 1
        print(genericAutomata)
        er = self.printER(genericAutomata)
        return er

    '''
    Metodo efetua um loop no dicionario de estados self.automato
    printando os cada um dos estados e suas transicoes
    '''
    def printAtomato(self):
        print('{:<8} {:<15} '.format('S', 'Transition'))
        for key, value in self.automato.items():
            if key == self.inicial:
                print('{!s:<8} {!s:<15} '.format('->'+''.join(key), value))
            elif key in self.finais:
                print('{!s:<8} {!s:<15} '.format('*'+''.join(key), value))
            else:    
                print('{!s:<8} {!s:<15} '.format(key, value))
    
    '''
    Metodo que recebe como parametro o automato reduzido e imprime sua expressao regular
    @:return a expressao regular
    '''
    def printER(self,ex):
        er = ''
        for k, v in ex.items():
            for key, value in v.items():
                if value == 'qf'.split():
                    er = key

        er = er.replace('&','')
        er = er.replace('.', '')
        return er

    def writeAutomataToFile(self, fileName):
        fileName = fileName.replace('.in', '')
        f = open('../testes/'+fileName+'.out', 'w')
        f.write('{:<8} {:<15} '.format('S', 'Transition'))
        for key, value in self.automato.items():
            if key\
                    == self.inicial:
                f.write('\n'+'{!s:<8} {!s:<15} '.format('->'+''.join(key), value))
            elif key in self.finais:
                f.write('\n'+'{!s:<8} {!s:<15} '.format('*'+''.join(key), value))
            else:
                f.write('\n'+'{!s:<8} {!s:<15} '.format(key, value))

        f.close()

    def getDictAutomato(self):
        return self.automato

    def getInicial(self):
        return self.inicial

    def getFinais(self):
        return self.finais
