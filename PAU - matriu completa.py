def crear_matriz_completa(lista_matrices):
    matriz_completa = [[0 for _ in range(36)] for _ in range(36)]

    for matriz in lista_matrices:
        for i in range(36):
            for j in range(36):
                # Si el valor de la matriz actual en la posición (i, j) es mayor a cero
                # y en la matriz_completa aún no se ha colocado ningún valor, o el valor es cero,
                # entonces lo colocamos en la matriz_completa
                if matriz[i][j] > 0 and matriz_completa[i][j] == 0:
                    matriz_completa[i][j] = matriz[i][j]

        # Verificamos si la matriz_completa ya no contiene ceros
        if all(all(num > 0 for num in fila) for fila in matriz_completa):
            break

    return matriz_completa