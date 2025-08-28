
def findneighbors(puzzle, cell):
    neighbors = []
    directions = ((0,1),(1,0),(0,-1),(-1,0))
    for direction in directions:
        neighborcellindex = (cell[0] + direction[0], cell[1] + direction[1])
        neighborcellvalue = puzzle.get(neighborcellindex, None)
        if neighborcellvalue is None:
            continue
        elif neighborcellvalue[0] <= 0:
            continue
        else:
            neighbors.append(neighborcellindex)
    return neighbors
def findpiece(puzzle, cell, piece = None):
    if piece is None:
        piece = [cell]
    neighbors = findneighbors(puzzle, cell)
    for neighbor in neighbors:
        if neighbor not in piece:
            piece.append(neighbor)
            findpiece(puzzle, neighbor, piece)
    return piece
def generatepieces(puzzle:dict):
    pieces = {}
    piecevalues = {}
    for cellindex in puzzle:
        cellvalue = puzzle.get(cellindex, None)
        if cellvalue is None or cellvalue == (0,0) or cellindex in pieces:
            continue
        elif cellvalue == (0,1):
            piecevalues[cellindex] = puzzle[cellindex]
            pieces[cellindex] = [cellindex]
        else:
            piece = findpiece(puzzle, cellindex)
            for cellindex in piece:
                piecevalues[cellindex] = puzzle[cellindex]
                pieces[cellindex] = piece
    return pieces,piecevalues
