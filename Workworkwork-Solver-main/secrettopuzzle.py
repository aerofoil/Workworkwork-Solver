from copy import deepcopy
def secrettopuzzle(terminalcode:str):
    piecerow = 0
    piececolumn = 0
    piecedensity = 0
    pieceorbdensity = 0
    puzzle = {}
    puzzleoutput = {}
    currentgrid = {}
    for char in terminalcode:
        if char == "-":
            continue
        elif char == "_":
            piecedensity = None
        elif char == "1":
            piecedensity += 1
        elif char == "w" or char == "W":
            pieceorbdensity += 1
        elif char == "i" or char == "∞":
            piecedensity = float("inf")
        elif char == ".":
            if piecedensity is not None:
                currentgrid[(piecerow,piececolumn)] = (piecedensity,pieceorbdensity)
            piecedensity = 0
            pieceorbdensity = 0
            piececolumn += 1
        elif char == "/":
            if piecedensity is not None:
                currentgrid[(piecerow,piececolumn)] = (piecedensity,pieceorbdensity)
            piecedensity = 0
            pieceorbdensity = 0
            piecerow += 1
            piececolumn = 0
        elif char == ">":
            if piecedensity is not None:
                currentgrid[(piecerow,piececolumn)] = (piecedensity,pieceorbdensity)
            if puzzle == {}:
                puzzle = deepcopy(currentgrid)
            currentgrid = {}
            piecerow = 0
            piececolumn = 0
            piecedensity = 0
            pieceorbdensity = 0
    currentgrid[(piecerow,piececolumn)] = (piecedensity,pieceorbdensity)
    puzzleoutput = currentgrid
    return puzzle,puzzleoutput
