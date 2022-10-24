import random

class ficha:
    def __init__(self):
        self.visible = False
        self.bomba = False
        self.n_bombas = 0

tablero_oculto = []
tablero_class = []

tamano_tablero = input("Elije el tamaño del tablero superior a 3: ")
if tamano_tablero.isdigit() and int(tamano_tablero) > 2:
    tamano_tablero = int(tamano_tablero)
    for i in range(tamano_tablero):
        tablero_oculto.append([])
        tablero_class.append([])
        for j in range(tamano_tablero):
            tablero_oculto[i].append('*')
            tablero_class[i].append(ficha())
    n_minas = ((tamano_tablero*tamano_tablero)*35)//100
    n_minas_puestas = 0
    while n_minas > n_minas_puestas:
        posicion01 = random.randint(0, tamano_tablero-1)
        posicion02 = random.randint(0, tamano_tablero-1)
        if not tablero_class[posicion01][posicion02].bomba:
            tablero_class[posicion01][posicion02].bomba = True
            n_minas_puestas += 1
for i in range(len(tablero_class)):
    for j in range(len(tablero_class)):
        if j < tamano_tablero - 1:
            if tablero_class[j + 1][i].bomba:
                tablero_class[j][i].n_bombas += 1
            if i < tamano_tablero - 1:
                if tablero_class[j + 1][i + 1].bomba:
                    tablero_class[j][i].n_bombas += 1
        if i < tamano_tablero-1:
            if tablero_class[j][i + 1].bomba:
                tablero_class[j][i].n_bombas += 1
            if j > 0:
                if tablero_class[j - 1][i + 1].bomba:
                    tablero_class[j][i].n_bombas += 1
        if j > 0:
            if tablero_class[j - 1][i].bomba:
                tablero_class[j][i].n_bombas += 1
            if i > 0:
                if tablero_class[j - 1][i - 1].bomba:
                    tablero_class[j][i].n_bombas += 1
        if i > 0:
            if tablero_class[j][i - 1].bomba:
                tablero_class[j][i].n_bombas += 1
            if j < tamano_tablero - 1:
                if tablero_class[j + 1][i - 1].bomba:
                    tablero_class[j][i].n_bombas += 1

while True:
    fichas_ocultas = 0
    for i in tablero_oculto:
        fichas_ocultas += i.count("*")
        for j in i:
            print(j, end=" ")
        print()
    if fichas_ocultas == n_minas_puestas:
        print("Ganaste cacho de mierda...")
        break
    jugada = input(f"Indica donde quieres jugar desde 0 a {tamano_tablero-1}, ejemplo (columna: 2, fila: 4): ")
    if tablero_class[int(jugada.split(",")[1])][int(jugada.split(",")[0])].bomba:
        print("Cagaste perdiste, tocaste bomba")
        break
    else:
        tablero_oculto[int(jugada.split(",")[1])][int(jugada.split(",")[0])] = tablero_class[int(jugada.split(",")[1])][int(jugada.split(",")[0])].n_bombas