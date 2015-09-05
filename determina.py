
q0 = {0: ['q0','q1'], 1: ['q0']}
q1 = {0: ['q2'], 1: ['M']}
q2 = {0: ['M'], 1: ['q3']}
q3 = {0: ['M'], 1: ['M']}
M = {0: ['M'], 1: ['M']}
s = {'q0': q0, 'q1': q1, 'q2': q2, 'q3': q3, 'M': M}
d = s.copy()
# --------------------------------------------------
# q4 = {1: ['q4'], 2: ['M'], 3: ['M'], '&': ['q5']}
# q5 = {1: ['M'], 2: ['q5'], 3: ['M'], '&': ['q6']}
# q6 = {1: ['M'], 2: ['M'], 3: ['q6'], '&': ['M']}
# M = {1: ['M'], 2: ['M'], 3: ['M'], '&': ['M']}
# se = {'q4': q4, 'q5': q5, 'q6': q6, 'M': M}
# d = se.copy()
#---------------------------------------------------

def getAlfabeto(automato):
    aState = next (iter (automato.values()))
    alfabeto = aState.keys()
    return alfabeto

def atualizaEstados(dict, automato):
    for key, value in dict.items():
        naturalStates = automato.keys()
        if key not in naturalStates:
            automato[key] = value
    return automato

def criaEstado(v, automato):
    dict = {}
    texto =''
    novo = ''
    alfabeto = getAlfabeto(automato)
    for alf in alfabeto:
        dict[alf] = []
    for valor in v:
        novo+=valor
    for item in v:
        state = automato.get(item)
        for key , value in state.items():
            texto = ''
            for it in value:
                if it != 'M':
                    texto = it
                    dict[key].append(texto)
    d[novo] = dict

def procuraEstados(automato):
    st = []
    for key, value in automato.items():
        if key not in st:
            st.append(key)
    for key, value in automato.items():
        for k, v in value.items():
            newState =''
            for it in v:
                if it != 'M':
                    estado = it
                    newState = newState + estado
                if newState not in st and newState != '':
                    newState = ''
                    criaEstado(v, automato)

def calculaFecho(automato):
    sFecho = {}
    for key, value in automato.items():
        if key !='M':
            sFecho[key] = []
    for key, value in automato.items():
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

def determina(automato):
    alfabeto = getAlfabeto(automato)
    if '&' in alfabeto:
        fecho, states = calculaFecho(automato)
        print(fecho)
    else:   
        procuraEstados(automato)
        while len(automato) != len(d):
            atualizaEstados(d, automato)
            procuraEstados(automato)
        print(automato)
# ----------------------------------------------------
determina(s)