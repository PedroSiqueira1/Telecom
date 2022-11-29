import pyautogui

def getCoord (lista):
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

def coordDictionary (lista):
    coords_x, coords_y = getCoord(lista)
    coordtabuleiro = {}
    """for x in range(8):
        for y in range(8):
            coordtabuleiro[(x,y)] = (coords_x[x], coords_y[y])"""
    coordtabuleiro['a1'] = (coords_x[0], coords_y[0])
    coordtabuleiro['b1'] = (coords_x[1], coords_y[0])
    coordtabuleiro['c1'] = (coords_x[2], coords_y[0])
    coordtabuleiro['d1'] = (coords_x[3], coords_y[0])
    coordtabuleiro['e1'] = (coords_x[4], coords_y[0])
    coordtabuleiro['f1'] = (coords_x[5], coords_y[0])
    coordtabuleiro['g1'] = (coords_x[6], coords_y[0])
    coordtabuleiro['h1'] = (coords_x[7], coords_y[0])
    coordtabuleiro['a2'] = (coords_x[0], coords_y[1])
    coordtabuleiro['b2'] = (coords_x[1], coords_y[1])
    coordtabuleiro['c2'] = (coords_x[2], coords_y[1])
    coordtabuleiro['d2'] = (coords_x[3], coords_y[1])
    coordtabuleiro['e2'] = (coords_x[4], coords_y[1])
    coordtabuleiro['f2'] = (coords_x[5], coords_y[1])
    coordtabuleiro['g2'] = (coords_x[6], coords_y[1])
    coordtabuleiro['h2'] = (coords_x[7], coords_y[1])
    coordtabuleiro['a3'] = (coords_x[0], coords_y[2])
    coordtabuleiro['b3'] = (coords_x[1], coords_y[2])
    coordtabuleiro['c3'] = (coords_x[2], coords_y[2])
    coordtabuleiro['d3'] = (coords_x[3], coords_y[2])
    coordtabuleiro['e3'] = (coords_x[4], coords_y[2])
    coordtabuleiro['f3'] = (coords_x[5], coords_y[2])
    coordtabuleiro['g3'] = (coords_x[6], coords_y[2])
    coordtabuleiro['h3'] = (coords_x[7], coords_y[2])
    coordtabuleiro['a4'] = (coords_x[0], coords_y[3])
    coordtabuleiro['b4'] = (coords_x[1], coords_y[3])
    coordtabuleiro['c4'] = (coords_x[2], coords_y[3])
    coordtabuleiro['d4'] = (coords_x[3], coords_y[3])
    coordtabuleiro['e4'] = (coords_x[4], coords_y[3])
    coordtabuleiro['f4'] = (coords_x[5], coords_y[3])
    coordtabuleiro['g4'] = (coords_x[6], coords_y[3])
    coordtabuleiro['h4'] = (coords_x[7], coords_y[3])
    coordtabuleiro['a5'] = (coords_x[0], coords_y[4])
    coordtabuleiro['b5'] = (coords_x[1], coords_y[4])
    coordtabuleiro['c5'] = (coords_x[2], coords_y[4])
    coordtabuleiro['d5'] = (coords_x[3], coords_y[4])
    coordtabuleiro['e5'] = (coords_x[4], coords_y[4])
    coordtabuleiro['f5'] = (coords_x[5], coords_y[4])
    coordtabuleiro['g5'] = (coords_x[6], coords_y[4])
    coordtabuleiro['h5'] = (coords_x[7], coords_y[4])
    coordtabuleiro['a6'] = (coords_x[0], coords_y[5])
    coordtabuleiro['b6'] = (coords_x[1], coords_y[5])
    coordtabuleiro['c6'] = (coords_x[2], coords_y[5])
    coordtabuleiro['d6'] = (coords_x[3], coords_y[5])
    coordtabuleiro['e6'] = (coords_x[4], coords_y[5])
    coordtabuleiro['f6'] = (coords_x[5], coords_y[5])
    coordtabuleiro['g6'] = (coords_x[6], coords_y[5])
    coordtabuleiro['h6'] = (coords_x[7], coords_y[5])
    coordtabuleiro['a7'] = (coords_x[0], coords_y[6])
    coordtabuleiro['b7'] = (coords_x[1], coords_y[6])
    coordtabuleiro['c7'] = (coords_x[2], coords_y[6])
    coordtabuleiro['d7'] = (coords_x[3], coords_y[6])
    coordtabuleiro['e7'] = (coords_x[4], coords_y[6])
    coordtabuleiro['f7'] = (coords_x[5], coords_y[6])
    coordtabuleiro['g7'] = (coords_x[6], coords_y[6])
    coordtabuleiro['h7'] = (coords_x[7], coords_y[6])
    coordtabuleiro['a8'] = (coords_x[0], coords_y[7])
    coordtabuleiro['b8'] = (coords_x[1], coords_y[7])
    coordtabuleiro['c8'] = (coords_x[2], coords_y[7])
    coordtabuleiro['d8'] = (coords_x[3], coords_y[7])
    coordtabuleiro['e8'] = (coords_x[4], coords_y[7])
    coordtabuleiro['f8'] = (coords_x[5], coords_y[7])
    coordtabuleiro['g8'] = (coords_x[6], coords_y[7])
    coordtabuleiro['h8'] = (coords_x[7], coords_y[7])
    print(coordtabuleiro)
    return coordtabuleiro

#coordDictionary([[100,100],[700,700]])

def movePiece (board_coord, pieces):
    # coordtabuleiro = coordDictionary(lista)
    for piece in pieces:
        pyautogui.click(board_coord[piece], button='left', duration=0.5)
    return 0
    
# movePiece([[100,100],[700,700]], ['a1','h8','f4'])