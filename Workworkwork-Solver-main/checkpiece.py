from math import pi
from rotatepiece import rotatepiece
from copy import deepcopy
def checkpiece(output,puzzleoutput) -> bool:
    puzzleoutputdimensions = (max(puzzleoutput)[0]-min(puzzleoutput)[0],max([cell[1] for cell in puzzleoutput])-min([cell[1] for cell in puzzleoutput]))
    outputdimensionsoffset = (0-min(output)[0],0-min([cell[1] for cell in output]))
    puzzleoutputdimensionsoffset = (0-min(puzzleoutput)[0],0-min([cell[1] for cell in puzzleoutput]))
    puzzleoutput = {(cell[0]+puzzleoutputdimensionsoffset[0],cell[1]+puzzleoutputdimensionsoffset[1]):puzzleoutput[cell] for cell in puzzleoutput}
    rotations = [pi*angle/2 for angle in range(4)]
    for rotation in rotations:
        output = rotatepiece(output.keys(),deepcopy(output),rotation,(0,0))[1]
        outputdimensionsoffset = (0-min(output)[0],0-min([cell[1] for cell in output]))
        output = {(cell[0]+outputdimensionsoffset[0],cell[1]+outputdimensionsoffset[1]):output[cell] for cell in output}
        outputdimensions = (max(output)[0]-min(output)[0],max([cell[1] for cell in output])-min([cell[1] for cell in output]))
        if outputdimensions[0] > puzzleoutputdimensions[0] or outputdimensions[1] > puzzleoutputdimensions[1]:
            continue
        for rowoffset in range(puzzleoutputdimensions[0]-outputdimensions[0]+1):
            for columnoffset in range(puzzleoutputdimensions[1]-outputdimensions[1]+1):
                newoutput = {(cell[0]+rowoffset,cell[1]+columnoffset):output[cell] for cell in output}
                for cell in newoutput:
                    if newoutput[cell][0] > puzzleoutput.get(cell,(-float("inf"),0))[0] or newoutput[cell][1] > puzzleoutput.get(cell,(0,-float("inf")))[1]:
                        break
                else:
                    return True
    return False