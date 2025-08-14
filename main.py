#this solver works for puzzles using mechanics from chapters 1 to 4
#it might be a bit slow

from solvepuzzle import solvepuzzle
from secrettopuzzle import secrettopuzzle
def main() -> None:
    puzzle = {}
    puzzleOutput = {}
    knowssecret = input("do you know what the blocks of text before each chapter are? yes or no? ").casefold()

    #do not scroll right if you don't know because it is a spoiler
    #do not scroll right if you don't know because it is a spoiler
    #do not scroll right if you don't know because it is a spoiler
    #do not scroll right if you don't know because it is a spoiler
    #do not scroll right if you don't know because it is a spoiler
    #do not scroll right if you don't know because it is a spoiler
    #do not scroll right if you don't know because it is a spoiler
    #do not scroll right if you don't know because it is a spoiler

    #if you do know, scroll right for info on how to use this probably slightly broken tool                                                                                                                                                                                                                         #the valid symbols that you can use in the terminal codes for now are
    #                                                                                                                                                                                                                                                                                                              # "1" "w" "W" "-" "_" "." "/" ">" "i" "∞". spaces are allowed
    if knowssecret == "yes" or knowssecret == "y":                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                        puzzle,puzzleOutput = secrettopuzzle(input("\nterminal code for puzzle"))
    else:
       print("\nchange the code to input it manually, i will probably make an input system for you guys later but not now. sorry.")
       print("an example of a puzzle is at the bootom of 'solvepuzzle.py'. the puzzle is puzzle #8")




    
    #print(puzzle,puzzleOutput)
    #print(generatepieces(puzzle)[0])
    solvepuzzle(puzzle, puzzleOutput)
if __name__ == "__main__":
  main()
  
  