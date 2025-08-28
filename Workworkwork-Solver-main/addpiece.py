def addpiece(output:dict, piece:list, piecevalues:dict, enteredcell:tuple, outputposition:tuple) -> dict:
  offset = (enteredcell[0]-outputposition[0],enteredcell[1]-outputposition[1])
  piece = [(cell[0]-offset[0],cell[1]-offset[1]) for cell in piece]
  piecevalues = {(cell[0]-offset[0],cell[1]-offset[1]):piecevalues[cell] for cell in piecevalues}
  for cell in piece:
    if output.get(cell) is None:
        output[cell] = (0,0)
    newvalue = (piecevalues[cell][0]+output[cell][0],piecevalues[cell][1]+output[cell][1])
    output[cell] = newvalue[:]
  return output