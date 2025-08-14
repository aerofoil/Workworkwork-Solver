from math import cos, sin
# !make this work
def rotatepiece(piece:list,piecevalues:dict,degreesradians:float,pointOfrotation:tuple):
  newpiecevalues = {}
  newpiece = []
  # print(pointOfrotation)
  for cellindex in piece:
    # print(f'\033[0;32m{cellindex}\033[0m')
    cellvalue = piecevalues.get(cellindex)
    cellindex = list(cellindex)
    cellindex[0] -= pointOfrotation[0]
    cellindex[1] -= pointOfrotation[1]
    newCell = list(cellindex)
    newCell[0] = round(cellindex[0] * cos(degreesradians) - cellindex[1] * sin(degreesradians))
    newCell[1] = round(cellindex[0] * sin(degreesradians) + cellindex[1] * cos(degreesradians))
    newCell[0] += pointOfrotation[0]
    newCell[1] += pointOfrotation[1]
    newpiece.append(tuple(newCell))
    # print(f'\033[0;32m{newCell}\033[0m')
    newpiecevalues[tuple(newCell)] = cellvalue
    # print(newpiece,newpiecevalues)
  return newpiece, newpiecevalues
