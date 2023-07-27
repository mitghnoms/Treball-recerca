def crear_matriu_completa(matriu_inicial):
    matriu_completa = matriu_inicial

    while any(0 in fila for fila in matriu_completa):
        matriu_temporal = [[0 for _ in range(36)] for _ in range(36)]

        for i in range(36):
            for j in range(36):
                # Si el valor de la matriu actual en la posición (i, j) es mayor a cero
                # y en la matriz_completa aún no se ha colocado ningún valor, o el valor es cero,
                # entonces lo colocamos en la matriz_temporal
                if matriu_completa[i][j] > 0 and matriu_temporal[i][j] == 0:
                    matriu_temporal[i][j] = matriu_completa[i][j]

        # Multiplicamos la matriz_temporal por la matriz_inicial
        matriu_completa = Matriu(matriu_temporal) @ Matriu(matriu_inicial)

    return matriu_completa