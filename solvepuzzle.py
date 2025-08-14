
from addpiece import addpiece
from generatepieces import generatepieces
from rotatepiece import rotatepiece
from math import pi
from copy import deepcopy
from checkpiece import checkpiece
from math import cos,sin
def solvepuzzle(puzzle:dict, puzzleoutput:dict):
  output = {(0,0):(0,0)}
  outputposition = (0,0)
  outputrotation = (0,1)
  pieceenterrotation = 0
  path = []
  workers = []
  for cell in puzzle:
    if puzzle[cell] == (0,1):
      workers.append(cell)
  for worker in workers:
    path = [worker]
    output = {(0,0):(0,0)}
    #outputposition = worker
    solver(puzzle, puzzleoutput, output, outputposition, outputrotation, pieceenterrotation, path, inpiece=False)
def rotateVector(vector, degreesRadians):
  return round(vector[0] * cos(degreesRadians) - vector[1] * sin(degreesRadians)), round(vector[0] * sin(degreesRadians) + vector[1] * cos(degreesRadians))
def solver(puzzle:dict, puzzleoutput, output, outputposition, outputrotation, pieceenterrotation, path:list, inpiece = False):
    directions = ((0,1),(1,0),(0,-1),(-1,0))
    rotations = {(1,0):pi/2,(0,1):0,(-1,0):pi*3/2,(0,-1):pi}
    pieceenterrotation2 = pieceenterrotation
    outputposition2 = outputposition[:]
    outputrotation2 = outputrotation[:]
    for direction in directions:
        nextcellindex = (path[-1][0] + direction[0], path[-1][1] + direction[1])
        nextcellvalue = puzzle.get(nextcellindex, None)
        if nextcellindex in path or nextcellvalue is None:
            continue
        path.append(nextcellindex)

        if inpiece:
            direction = rotateVector(direction,pieceenterrotation)
            outputposition = (outputposition[0] + direction[0], outputposition[1] + direction[1])
            outputrotation = direction
    
        if nextcellvalue == (0,0):
            solver(puzzle, puzzleoutput, output, outputposition, outputrotation, pieceenterrotation, path, inpiece=False)
        else:
            if nextcellvalue == (0,1) and checkpiece(output,puzzleoutput) and checkpiece(puzzleoutput,output):
                print(f'\033[0;31m{path}\033[0m')
            if len(path) == 2:
                outputrotation = direction
                pieceenterrotation = rotations[direction]
            if not inpiece:
                pieceenterrotation = rotations[direction] - rotations[outputrotation]
            if not(puzzle[path[-2]][0] > 0 and nextcellvalue[0] > 0):
                #print(*path)
                pieces, cellvalues = generatepieces(puzzle)
                pieces:dict = pieces #{pieceindex:piece}
                cellvalues:dict = cellvalues #{cell:cellvalue}
                piece = pieces[nextcellindex]
                rotation = rotations[direction]-rotations[outputrotation]
                piece, cellvalues = rotatepiece(piece,cellvalues,rotation, nextcellindex)
                newoutput = addpiece(deepcopy(output), piece, cellvalues, nextcellindex, outputposition)
                if checkpiece(newoutput,puzzleoutput):
                    #print(f'\033[0;32m{newoutput}\033[0m')
                    solver(puzzle, puzzleoutput, newoutput, outputposition, outputrotation, pieceenterrotation, path, inpiece=True)
            else:
                solver(puzzle, puzzleoutput, output, outputposition, outputrotation, pieceenterrotation, path, inpiece=True)
        pieceenterrotation = pieceenterrotation2
        outputposition = outputposition2
        outputrotation = outputrotation2
        path.pop(-1)

        
if __name__ == "__main__":
  puzzle = {
    (0,0):(0,1),
    (0,1):(1,0),
    (0,2):(0,0),
    (1,0):(0,1),
    (1,1):(1,0),
    (1,2):(0,0),
    (2,1):(0,0),
    (2,2):(0,0)
  }
  puzzleoutput = {
    (0,0):(1,0),
    (0,1):(1,0),
    (0,2):(1,0),
    (1,0):(1,0)
  }
  solvepuzzle(puzzle, puzzleoutput)
  