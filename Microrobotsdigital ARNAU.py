import random
from typing import List, Tuple, Dict
import time

def organitzaquadrats(quadrat1,quadrat2,quadrat3,quadrat4):
    taulell = []
    taulell = [quadrat1[0], quadrat2[0],quadrat1[1],quadrat2[1],quadrat1[2],quadrat2[2],quadrat3[0],quadrat4[0],quadrat3[1],quadrat4[1],quadrat3[2],quadrat4[2]]
    return taulell

def rota_quadrat(quadrat: List[List[Tuple[int, str]]]) -> List[List[Tuple[int, str]]]:
     temp_matrix = []
     column = len(quadrat)-1
     for column in range(len(quadrat)):
         temp = []
         for row in range(len(quadrat)-1,-1,-1):
             temp.append(quadrat[row][column])
         temp_matrix.append(temp)
     for i in range(len(quadrat)):
         for j in range(len(quadrat)):
             quadrat[i][j] = temp_matrix[i][j]
     return temp_matrix
     quadrat_nou = []

def mourequadrats(quadrat1,quadrat2,quadrat3,quadrat4):
    quadrats = [quadrat1,quadrat2,quadrat3,quadrat4]
    novaorg = ['a','b','c','d']
    posicio = random.randint(0,3)
    posicions = []
    for quadrat in quadrats:
        while posicio in posicions:
            posicio = random.randint(0,3)
        posicions += [posicio]
        novaorg[posicio] = quadrat
#     print (posicions)
    return novaorg
def crea_taulell(quadrat1,quadrat2,quadrat3,quadrat4) -> List[List[Tuple[int, str]]]:
    quadrats = [quadrat1,quadrat2,quadrat3,quadrat4]
    quadratsrotats= []
    mouquadrats = mourequadrats(quadrats[0], quadrats[1], quadrats[2], quadrats[3])
#     print(mouquadrats)
    for quadrat in mouquadrats:
        vegadesrot = random.randint (0,3)
#         print(vegadesrot)
        if vegadesrot == 0:
            quadratsrotats += [quadrat]
        elif vegadesrot == 1:
            quadratsrotats +=[rota_quadrat(quadrat)]
        elif vegadesrot == 2:
            quadratsrotats += [rota_quadrat(rota_quadrat(quadrat))]
        elif vegadesrot == 3:
            quadratsrotats += [rota_quadrat(rota_quadrat(rota_quadrat(quadrat)))]
    return quadratsrotats

class Quadrat():
    def __init__(self, llista: List[List[Tuple[int, str]]]):
        self.llista = llista

    def __repr__(self):
        resultat = ''
        for fila in self.llista:
            for cella in fila:
                resultat += f'{cella[0]}{cella[1]}' + ' '
            resultat += '\n'
        return resultat

    def rotar(resultat):
        # aquí hi va el codi de rotar
        temp_matrix = []
        column = len(resultat)-1
        for column in range(len(resultat)):
            temp = []
            for row in range(len(resultat)-1,-1,-1):
                temp.append(resultat[row][column])
            temp_matrix.append(temp)
        for i in range(len(resutltat)):
            for j in range(len(resultat)):
               resultat[i][j] = temp_matrix[i][j]
        return Quadrat(temp_matrix)

class Taulell():
    def __init__(self, llista_quadrats: List[Quadrat]):
        self.llista_quadrats = llista_quadrats
        self.dades = []

        for i in range(6):
            fila_nova = []
            for j in range(6):
                if i < 3:
                    if j < 3:
                        fila_nova.append(llista_quadrats[0].llista[i][j])
                    else:
                        fila_nova.append(llista_quadrats[1].llista[i][j - 3])
                else:
                    if j < 3:
                        fila_nova.append(llista_quadrats[2].llista[i - 3][j])
                    else:
                        fila_nova.append(llista_quadrats[3].llista[i - 3][j - 3])
            self.dades.append(fila_nova)

    def __repr__(self):
        resultat = ''
        for i, fila in enumerate(self.dades):
            for j, cella in enumerate(fila):
                resultat += f'{cella[0]}{cella[1]}' + ' '
                if j == 2:
                    resultat += '| '
            if i == 2:
                resultat += '\n' + '-'*(3*6+2)
            resultat += '\n'
        return resultat

def genera_matriu_adjacencia(t: Taulell):
    m = []
    for i in range(len(t.dades)):
        for j in range(len(t.dades[0])):
            fila_actual = t.dades[i]
            columna_actual = [t.dades[k][j] for k in range(len(t.dades))]
            casella_actual = t.dades[i][j]
            for k in range(len(t.dades)):
                for l in range(len(t.dades[0])):
                    fila_mirar = t.dades[k]
                    columna_mirar = [t.dades[m][l] for m in range(len(t.dades))]
                    casella_a_mirar = t.dades[k][l]
                    if casella_actual == casella_a_mirar:
                        m.append(0)
                    elif (casella_actual[0] == casella_a_mirar[0] or casella_actual[1] == casella_a_mirar[1]) and (fila_actual == fila_mirar or columna_actual == columna_mirar):
                        m.append(1)
                    else:
                        m.append(0)
    return m

def dividir_matriu(matriu):
    return [matriu[i:i + 36] for i in range(0, len(matriu), 36)]

def generea_casella(taulell):
    fila_aleatoria = random.randint(0, len(taulell.dades) - 1)
    columna_aleatoria = random.randint(0, len(taulell.dades[0]) - 1)
    return (taulell.dades[fila_aleatoria][columna_aleatoria])

def temporitzador() -> str:
    print('Teniu 1 minut per pensar en un camí per arribar de la casella original a la final i escriure'+"""'l.""")
    time.sleep(45)
    print('S\'ha acabat el temps')
    
def demana_moviments(jugador) -> list:
    nombremov = int(input(jugador + ', digues el nombre de moviment que has necessitat per arribar a la casella destí: ') )
    moviments = input(jugador + ', escriu els moviments que has fet, esriu-los en format nombre de la casella(p.e. 4y,5r,6b,...), lletra de la casella, sense '' ni parèntesis ni claudators: ')
    elements = moviments.split(',')
    llistamov = []
    tupla = []
    movimentsretocats = []
    movimentsretocats2 = []
    llistaFAB=[]
    
    for e in elements:
        tupla.append(e)
        llistamov.append(tupla)
        tupla = []
    for a in llistamov:
        for b in a:
            movimentsretocats.append(tuple(b))
    for tup in movimentsretocats:
       tuplaFAB=int(tup[0]),tup[1]
       llistaFAB.append(tuplaFAB)
       tuplaFAB=()
    
    if len(llistamov) != nombremov:
        print('El nombre de moviments no coincideix amb els moviments que has escrit.'+'\n'+'HAS PERDUT, MÉS SORT EL PROPER COP')
    elif len(llistamov) == nombremov:
        print('Ara comprovarem la teva resposta, espera pacientment.')
    return llistaFAB

def comprova_moviments(moviments, taulell, casella_inicial, casella_final) -> bool:
    moviments2 = []
    t = Taulell([Quadrat(taulell[0]),Quadrat(taulell[1]),Quadrat(taulell[2]),Quadrat(taulell[3])])
    taulell2 = organitzaquadrats(taulell[0],taulell[1],taulell[2],taulell[3])
    matriu = dividir_matriu(genera_matriu_adjacencia(t))
    casella_actual = casella_inicial
    fila_casella_actual = -1
    posicio_moviments = -1
    estat = False
    estat2 = False
    respostes_correctes = 0
    while len(moviments) > 0:
        for fila in taulell2:
            for casella in fila:
                fila_casella_actual += 1
                if casella == casella_actual:
                    estat = True
                    break
            if estat == True:
                break

#         print(fila_casella_actual, casella_actual)
        for fila in taulell2:
            for casella in fila:
                posicio_moviments += 1
                if casella ==moviments[0]:
                    estat2 = True
                    break
            if estat2 == True:
                break
#         print(posicio_moviments, moviments[0])
        if matriu[fila_casella_actual][posicio_moviments] == 1:
            print('Moviment correcte.')
            respostes_correctes += 1
            casella_actual =moviments[0]
            fila_casella_actual = -1
            posicio_moviments = -1
            moviments2.append(moviments[0])
            moviments.remove(moviments[0])
            estat = False
            estat2 = False
        else:
            print('La solució donada és errónea.')
            return False
    if respostes_correctes == len(moviments2):
        print('Tots els moviments que has donat són correctes, ben jugat.')
        print('Has donat una solució correcte de ', len(moviments2), ' moviment/s')
        return True
            
        
        
        
# comprova_moviments([(4,'g'),(3,'y'),(5,'y'),(5,'r'),(3,'r')],([[(2,'y'),(1,'w'),(1,'b')],
#             [(2,'w'),(2,'g'),(2,'r')],
#             [(4,'p'),(6,'g'),(4,'w')]],[[(3,'p'),(3,'y'),(3,'g')],
#             [(2,'p'),(4,'r'),(5,'g')],
#             [(5,'p'),(6,'r'),(4,'b')]],[[(5,'w'),(4,'g'),(3,'b')],
#             [(3,'w'),(4,'y'),(3,'r')],
#             [(2,'b'),(6,'b'),(6,'w')]],[[(1,'g'),(1,'r'),(6,'p')],
#             [(5,'r'),(5,'b'),(5,'y')],
#             [(1,'y'),(6,'y'),(1,'p')]]),(6,'g'),(3,'r'))        
#     

 

def torn_microrobots(jugador) -> str:
    quadrats1 = [[(2,'y'),(1,'w'),(1,'b')],
            [(2,'w'),(2,'g'),(2,'r')],
            [(4,'p'),(6,'g'),(4,'w')]], [[(3,'p'),(3,'y'),(3,'g')],
            [(2,'p'),(4,'r'),(5,'g')],
            [(5,'p'),(6,'r'),(4,'b')]], [[(5,'w'),(4,'g'),(3,'b')],
            [(3,'w'),(4,'y'),(3,'r')],
            [(2,'b'),(6,'b'),(6,'w')]], [[(1,'g'),(1,'r'),(6,'p')],
            [(5,'r'),(5,'b'),(5,'y')],
            [(1,'y'),(6,'y'),(1,'p')]]
    quadrats2 = [[(2,'r'),(3,'r'),(4,'r')],
            [(6,'r'),(2,'y'),(5,'y')],
            [(3,'p'),(6,'b'),(5,'b')]], [[(4,'g'),(5,'g'),(1,'p')],
            [(1,'w'),(5,'w'),(4,'w')],
            [(4,'p'),(3,'g'),(2,'p')]], [[(1,'b'),(4,'y'),(3,'b')],
            [(6,'p'),(6,'w'),(4,'b')],
            [(5,'p'),(6,'y'),(2,'b')]], [[(3,'y'),(1,'g'),(3,'w')],
            [(1,'y'),(2,'w'),(2,'g')],
            [(1,'r'),(6,'g'),(5,'r')]]
    quadrats_a_jugar = random.randint(0,1)
    if quadrats_a_jugar == 0:
        quadrat1 = [[(2,'y'),(1,'w'),(1,'b')],
            [(2,'w'),(2,'g'),(2,'r')],
            [(4,'p'),(6,'g'),(4,'w')]]
        quadrat2 = [[(3,'p'),(3,'y'),(3,'g')],
            [(2,'p'),(4,'r'),(5,'g')],
            [(5,'p'),(6,'r'),(4,'b')]]
        quadrat3 = [[(5,'w'),(4,'g'),(3,'b')],
            [(3,'w'),(4,'y'),(3,'r')],
            [(2,'b'),(6,'b'),(6,'w')]]
        quadrat4 = [[(1,'g'),(1,'r'),(6,'p')],
            [(5,'r'),(5,'b'),(5,'y')],
            [(1,'y'),(6,'y'),(1,'p')]]
    elif quadrats_a_jugar == 1:
        quadrat1 = [[(2,'r'),(3,'r'),(4,'r')],
            [(6,'r'),(2,'y'),(5,'y')],
            [(3,'p'),(6,'b'),(5,'b')]]
        quadrat2 = [[(4,'g'),(5,'g'),(1,'p')],
            [(1,'w'),(5,'w'),(4,'w')],
            [(4,'p'),(3,'g'),(2,'p')]]
        quadrat3 = [[(1,'b'),(4,'y'),(3,'b')],
            [(6,'p'),(6,'w'),(4,'b')],
            [(5,'p'),(6,'y'),(2,'b')]]
        quadrat4 = [[(3,'y'),(1,'g'),(3,'w')],
            [(1,'y'),(2,'w'),(2,'g')],
            [(1,'r'),(6,'g'),(5,'r')]]
    t = crea_taulell(quadrat1,quadrat2,quadrat3,quadrat4)
    taulell = Taulell([Quadrat(t[0]),Quadrat(t[1]), Quadrat(t[2]), Quadrat(t[3])])
    print(taulell)
    casella_inicial = generea_casella(taulell)
    print('La casela inicial és : ' , casella_inicial)
    casella_final = generea_casella(taulell)
    print('La casela final és : ' , casella_final)
    temporitzador()
    moviments = demana_moviments(jugador)
    comprovacio = comprova_moviments(moviments, t, casella_inicial, casella_final)
    if comprovacio == True:
        jugar = input(jugador + ', vols tornar a jugar? Respon SÍ o NO: ')
        if jugar == 'Sí':
            torn_microrobots(jugador)
        elif jugar == 'NO':
            print('Fins aviat !!!')
            exit()
        else:
            print('No has respost res o has respost incorrectament a la última pregunta, fins aviat!')
            exit()
    
torn_microrobots('Arnau')

def codi_guanyador(taulell, casella_inicial, casella_final):
    matriu = dividir_matriu(genera_matriu_adjacencia(Taulell([Quadrat(taulell[0]),Quadrat(taulell[1]),Quadrat(taulell[2]),Quadrat(taulell[3])])))
    casella_actual = casella_inicial
    taulell2 = organitzaquadrats(taulell[0],taulell[1],taulell[2],taulell[3])
    fila_casella_actual = -1
    pos_casella_final = -1
    estat = False
    estat2 = False
    moviments_guanyadors = []
    for f in taulell2:
        for c in f:
            fila_casella_actual += 1
            if c == casella_actual:
                estat = True
                break
        if estat == True:
            break
    for f in taulell2:
        for c in f:
            pos_casella_final += 1
            if c == casella_final:
                estat2 = True
                break
        if estat2 == True:
            break
    if matriu[fila_casella_actual][pos_casella_final] == 1:
        moviments_guanyadors.append(casella_final)
        if comprova_moviments(moviments_guanyadrs, taulell, casella_inicial, casella_final) == True:
            print('Solució més curta possible aconseguida, moviments utilitzats:'+ len(moviments_guanyadors)+'. '+'\n'+'llistat dels moviments usats: '+ moviments_guanyadors)
    elif matriu[fila_casella_actual][pos_casella_final] != 1:
        while casella_actual != casella_final:
            for num in matriu[fila_casella_actual]:
                if num ==1:
                    moviments_guanyadors.append(taulell2[matriu[num]])
                    casella_actual = taulell2[matriu[num]]
                
            
    
    
    
    

