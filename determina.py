
# q0 = {0: ['q0','q1'], 1: ['q0']}
# q1 = {0: ['q2'], 1: ['M']}
# q2 = {0: ['M'], 1: ['q3']}
# q3 = {0: ['M'], 1: ['M']}
# M = {0: ['M'], 1: ['M']}
# s = {'q0': q0, 'q1': q1, 'q2': q2, 'q3': q3, 'M': M}
# --------------------------------------------------
q4 = {1: ['q4'], 2: ['M2'], 3: ['M2'], '&': ['q5']}
q5 = {1: ['M2'], 2: ['q5'], 3: ['M2'], '&': ['q6']}
q6 = {1: ['M2'], 2: ['M2'], 3: ['q6'], '&': ['M2']}
M2 = {1: ['M2'], 2: ['M2'], 3: ['M2'], '&': ['M2']}
se = {'q4': q4, 'q5': q5, 'q6': q6, 'M2': M2}
#---------------------------------------------------

d = se.copy()
st = []
alfabeto = q4.keys()

for key, value in se.items():
    if key not in st:
        st.append(key)

def atualizaEstados(dict):
    for key, value in dict.items():
        naturalStates = s.keys()
        if key not in naturalStates:
            s[key] = value
    return s

def criaEstado(v):
    dict = {}
    texto =''
    novo = ''
    for alf in alfabeto:
        dict[alf] = []
    for valor    in v:
        novo+=valor
    for item in v:
        state = s.get(item)
        for key , value in state.items():
            texto = ''
            for it in value:
                if it != 'M':
                    texto = it
                    dict[key].append(texto)
    d[novo] = dict

def procuraEstados(s):
    for key, value in s.items():
        for k, v in value.items():
            newState =''
            for it in v:
                if it != 'M':
                    estado = it
                    newState = newState + estado
                if newState not in st and newState != '':
                    newState = ''
                    criaEstado(v)

def calculaFecho():
    sFecho = {}
    Ytransition = []
    for key, value in se.items():
        if key !='M2':
            sFecho[key] = []
    for key, value in se.items():
        for k, v in value.items():
            for item in v:
                if k == '&' and key != 'M2' and item != 'M2':
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
    sFecho = fe
    atualizaFecho(sFecho)


def determina(s):
    if '&' in alfabeto:
        print("Automato com & transicoes")
    else:   
        procuraEstados(s)
        while len(s) != len(d):
            atualizaEstados(d)
            procuraEstados(s)
        print(s)

def atualizaFecho(fecho):
    print (fecho)
    af = fecho.keys
    dit = {}
    final = {}
    d = {}
    y = '&'
    for key, value in se.items():
        for k, v in fecho.items():
            if key == k:
                dit[v] = value
    for key, value in dit.items():
        for k, v in value.items():
            aux = v
            for item in aux:
                g = []                
                if item !='M2':
                    a = fecho[item]
                    g.append(a)
                    d[k] = g
                    dit[a] = d
    help = {}
    for key, value in dit.items():
        for k, v in value.items():
            if k != y:
                help[k] = v
        final[key] = help
    print(final)

calculaFecho()