import pyautogui

def getCoord(lista):
    print("lista:", lista)
    lengthx = lista[1][0] - lista[0][0]
    lengthy = lista[1][1] - lista[0][1]
    coords_x = []
    coords_y = []
    squarex = lengthx / 8
    squarey = lengthy / 8
    for x in range(8):
        coords_x.append(lista[0][0] + (squarex * x) + (squarex / 2))
    for y in range(8):
        coords_y.append(lista[0][1] + (squarey * y) + (squarey / 2))
    return coords_x, coords_y

def coordDictionary(lista):
    coords_x, coords_y = getCoord(lista)
    coordtabuleiro = {}
    for x in range(8):
        for y in range(8):
            coordtabuleiro[chr(97+x)+str(8-y)] = (coords_x[x], coords_y[y])

    return coordtabuleiro


def movePiece (board_coord, pieces):
    for piece in pieces:
        print("coord:", board_coord[piece])
        pyautogui.click(board_coord[piece], button='left', duration=0.5)
    return 0