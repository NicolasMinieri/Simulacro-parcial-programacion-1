def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:int) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz



def mostrar_matriz(matriz:list) -> None:
    for fil in range(len(matriz)):
        #for col in range(len(matriz[0]))
        for col in range(len(matriz[fil])):
            print(matriz[fil][col],end=" ")
        print("")


def carga_secuencial(matriz, indice_inicial_fil, indice_inicial_col):

    print("--agregar nota de jurado--\n")

    for i in range(len(matriz)):

        if i >= indice_inicial_col:

            for t in range(len(matriz[0])):
                if t >= indice_inicial_fil:
                    matriz[i][t] = int(input(f"Ingresar nota jurado {t}: "))
                    mostrar_matriz(matriz)

    return matriz

def carga_secuencial_nombres(matriz:list)->list:

    print("--agregar bailarines--\n")

    for i in range(len(matriz)):

        matriz[i][0]= input(f"Ingresar nota nombre de bailarin/a {i+1}: ")
        
        mostrar_matriz(matriz)

    return matriz


def mostrar_participantes_notas(matriz:list) -> list:
    for fil in range(len(matriz)):
        promedio = (matriz[fil][1] + matriz[fil][2] + matriz[fil][3])/ 3
        
        print(f"\nNro de participante {fil+1}: nota de jurado 1 --nota: {matriz[fil][1]}, nota de jurado 2 --nota: {matriz[fil][2]}, nota de jurado 3 --nota: {matriz[fil][3]}, nota promedio --nota: {promedio}\n")    


def ordenar_por_nota(matriz):

    for i in range(len(matriz)-1):

            for j in range(i+1,len(matriz)):

                if matriz[i][2] < matriz[j][2]:
                    auxiliar = matriz[i][2]
                    matriz[i][2] = matriz[j][2]
                    matriz[j][2] = auxiliar
                    mostrar_matriz(matriz)
    
    return matriz

def mostrar_prticipante_7(matriz:list) ->str:

    print(f"\nParticipantes con 7 en todo los jruados\n")
    for i in range(len(matriz)):

        if matriz[i][1] == 7 and matriz[i][2] == 7 and matriz[i][3] == 7:
            print(f"\nEl participante: {matriz[i]}\n")

    return matriz