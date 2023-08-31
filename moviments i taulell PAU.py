import random
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple


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

# taulell = Taulell([Quadrat([[(2,'y'),(1,'w'),(1,'b')],
#             [(2,'w'),(2,'g'),(2,'r')],
#             [(4,'p'),(6,'g'),(4,'w')]]),Quadrat([[(3,'p'),(3,'y'),(3,'g')],
#             [(2,'p'),(4,'r'),(5,'g')],
#             [(5,'p'),(6,'r'),(4,'b')]]),Quadrat([[(5,'w'),(4,'g'),(3,'b')],
#             [(3,'w'),(4,'y'),(3,'r')],
#             [(2,'b'),(6,'b'),(6,'w')]]), Quadrat([[(1,'g'),(1,'r'),(6,'p')],
#             [(5,'r'),(5,'b'),(5,'y')],
#             [(1,'y'),(6,'y'),(1,'p')]])])



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

def crear_taulells_possibles(quadrat1,quadrat2,quadrat3,quadrat4):
    copsq1 = 0
    copsq2 = 0
    copsq3 = 0
    copsq4 = 0
    taulells = []
    q1 = [quadrat1, rota_quadrat(quadrat1),rota_quadrat(rota_quadrat(quadrat1)),rota_quadrat(rota_quadrat(rota_quadrat(quadrat1)))]
    q2 = [quadrat2, rota_quadrat(quadrat2),rota_quadrat(rota_quadrat(quadrat2)),rota_quadrat(rota_quadrat(rota_quadrat(quadrat2)))]
    q3 = [quadrat3, rota_quadrat(quadrat3),rota_quadrat(rota_quadrat(quadrat3)),rota_quadrat(rota_quadrat(rota_quadrat(quadrat3)))]
    q4 = [quadrat4, rota_quadrat(quadrat4),rota_quadrat(rota_quadrat(quadrat4)),rota_quadrat(rota_quadrat(rota_quadrat(quadrat4)))]
    quadrats = [q1,q2,q3,q4]
    tots = [[x1,x2,x3,x4] for x1 in q1 + q2 + q3 + q4 for x2 in q1 + q2 + q3 + q4 for x3 in q1 + q2 + q3 + q4 for x4 in q1 + q2 + q3 + q4 if x1 != x2 and x1 != x3 and x1 != x4 and x2 != x3 and x2 != x4 and x3 != x4]
    for taulell in tots:
        copsq1 = 0
        copsq2 = 0
        copsq3 = 0
        copsq4 = 0
        for quadrat in taulell:
            if quadrat in q1:
                copsq1 += 1
            elif quadrat in q2:
                copsq2 += 1
            elif quadrat in q3:
                copsq3 += 1
            elif quadrat in q4:
                copsq4 += 1
        if copsq1 == 1 and copsq2 == 1 and copsq3 == 1 and copsq4 == 1:
            taulells.append(taulell)
    print (len(taulells))
    return taulells

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

    def mou_primera_fila_a_ultima(self):
        primera_fila = self.dades.pop(0)
        self.dades.append(primera_fila)



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

class Matriu():
    def __init__(self, llista_de_llistes):
        self.dades = [fila[:] for fila in llista_de_llistes]
     
    def __repr__(self):
        return '\n'.join(' '.join(f'{num:3}'for num in fila) for fila in self.dades)
    
    def __add__(self, other):
        dades = []
        for fila1, fila2 in zip(self.dades, other.dades):
            fila_nova = []
            for a, b in zip(fila1, fila2):
                fila_nova.append(a + b)
            dades.append(fila_nova)
        return Matriu(dades)
    
    def __matmul__(self, other):
        if len(self.dades[0]) != len(other.dades):
            raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación.")
        
        dades = []
        for fila1 in self.dades:
            fila_nova = []
            for columna in zip(*other.dades):
                suma = sum(a * b for a, b in zip(fila1, columna))
                fila_nova.append(suma)
            dades.append(fila_nova)
        return Matriu(dades)
    

def dividir_matriu(matriu):
    return [matriu[i:i + 36] for i in range(0, len(matriu), 36)]


def estudi_taulell_moviments(quadrat1,quadrat2,quadrat3,quadrat4):
    taulell_nou = []
    taulells = crear_taulells_possibles(quadrat1,quadrat2,quadrat3,quadrat4)
    nombretaulells = 0
    taulellsfallats = []
    matrius = []
    cincmoviments = []
    suma = 0
    mitjanes = []
    matriusno = 0
    matriusmult= []
    matriucreada = []
    suma_elements = 0
    rankfacilitat = {}
    taulellsjugablesamb5mov = []
#     while len(taulellsfallats) < 1:
#         taulell_nou = crea_taulell(quadrat1,quadrat2,quadrat3,quadrat4)
#         if taulell_nou not in taulells:
#             taulells.append(taulell_nou)
#             nombretaulells += 1
#             print (nombretaulells)
#         elif taulell_nou in taulells:
#             print('ja s\'ha creat aquest taulell')
#             taulellsfallats.append(taulell_nou)
#             print (nombretaulells)
#             
    for taulell in taulells:
        matriucreada = (genera_matriu_adjacencia(Taulell([Quadrat(taulell[0]),Quadrat(taulell[1]),Quadrat(taulell[2]),Quadrat(taulell[3])])))
        matriucreada = dividir_matriu(matriucreada)
        matriusno += 1
        caselles_per_contador = {}
        print (matriusno)
        print (matriucreada, taulell)
        matriucreada = np.array(matriucreada)
        contador = 1
        caselles_arribades = 0
        matriu_completa = np.zeros_like(matriucreada)
        while 0 in matriu_completa:
            for i in range(matriucreada.shape[0]):
                for j in range(matriucreada.shape[1]):
                    if matriucreada[i, j] > 0 and matriu_completa[i, j] == 0:
                        matriu_completa[i, j] = matriu_completa[i, j] + contador
                        caselles_arribades += 1
            matriucreada = matriucreada @ matriucreada
            caselles_per_contador[contador] = caselles_arribades
            x = caselles_per_contador.keys()
            y = caselles_per_contador.values()

            plt.clf() 
            plt.bar(x, y)
            plt.xlabel("CONTADOR")
            plt.ylabel("CASELLES")

            ruta_carpeta = "C:\\Users\\rserrano\\OneDrive\\Documentos\\GitHub\\Treball-recerca\\Gràfics Generats"
            plt.savefig(ruta_carpeta + '\\grafico'+str(matriusno)+'.png')
            caselles_arribades = 0
            contador += 1
        matriu_completa = dividir_matriu(matriu_completa.tolist())
        contador -= 1
        print("Contador: ",contador)
        print("\nMatriu Completa:")
        print(matriu_completa)
        print(caselles_per_contador)
        print("El gráfico se ha guardado en:", ruta_carpeta + '\\grafico'+str(matriusno)+'.png')
        
#         cincmoviments.append(matriusmult)
#         print(matriusmult)
#         taulellcomlpet = all(all(valor >= 1 for valor in fila) for fila in matriusmult.dades)
#         if taulellcomlpet:
#             taulellsjugablesamb5mov.append(taulell)
#         for fila in matriusmult.dades:
#             for casella in fila:
#                 suma_elements += casella
#         rankfacilitat[suma_elements]= Taulell([Quadrat(taulell[0]),Quadrat(taulell[1]),Quadrat(taulell[2]),Quadrat(taulell[3])])
#     rankfacilitatordenat = sorted(rankfacilitat.keys(), reverse = False)
#     for clau in rankfacilitatordenat:
#         valor = rankfacilitat[clau]
#         print(clau, '\n',valor)
#     print ('Aquests taulells són jugables completament amb 5 moviments',taulellsjugablesamb5mov)

    
#         
# estudi_taulell_moviments([[(2,'y'),(1,'w'),(1,'b')],
#             [(2,'w'),(2,'g'),(2,'r')],
#             [(4,'p'),(6,'g'),(4,'w')]],[[(3,'p'),(3,'y'),(3,'g')],
#             [(2,'p'),(4,'r'),(5,'g')],
#             [(5,'p'),(6,'r'),(4,'b')]],[[(5,'w'),(4,'g'),(3,'b')],
#             [(3,'w'),(4,'y'),(3,'r')],
#             [(2,'b'),(6,'b'),(6,'w')]],[[(1,'g'),(1,'r'),(6,'p')],
#             [(5,'r'),(5,'b'),(5,'y')],
#             [(1,'y'),(6,'y'),(1,'p')]])