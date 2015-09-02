
q0 = {0: ['q0','q1'], 1: ['q0']}
q1 = {0: ['q2'], 1: ['M']}
q2 = {0: ['M'], 1: ['q3']}
q3 = {0: ['M'], 1: ['M']}
M = {0: ['M'], 1: ['M']}
s = {'q0': q0, 'q1': q1, 'q2': q2, 'q3': q3, 'M': M}
d = s.copy()
st = []
alfabeto = q0.keys()
fim = False

for key, value in s.items():
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
     for key, value in s.items():
        

def determina (s):
    if '&' in alfabeto:
        print("Automato com & transições")
    else:   
        procuraEstados(s)
        while len(s) != len(d):
            atualizaEstados(d)
            procuraEstados(s)
        print(s)

determina(s)