# Workworkwork-Solver
A tool to automatically solve workworkwork puzzles.
# Preface
This code might be slow at times and be hard to read

I might make it better at some point
# How to run it through terminal
## On Mac
First download and extract the .zip file, then run it through terminal.
Open terminal and type: 
```
cd (the folder)
```
You should replace "(the folder)" with the folder you just obtained.

Then type:
```
python3 main.py
```
And that should work.

If it doesn't, try downloading python3 from [python.org](https://www.python.org)
## On Anything else
If you are not on a Mac, I don't know so sorry.
# How it works

## **This is _EXTREMELY_ important**
A solution is represented as a list of cells which represents the order the cells were travelled through

The coordinates are represented like this:
```
(row,column)
```

When you try to solve a puzzle, it will give back multiple paths as answers.

This is because the program currently considers paths to be directional.

**So if it currently returns 2 paths, it has a unique solution.**

Sorry if this confused anyone.

When you first run the program it will ask you if you know some secrets about the game.

This is to prevent spoilers
### People who do not know about that secret
If you don't know, then for now, you are just going to have to edit the code.

Sorry.

A puzzle and its output are represented by dictionaries which contain info about the cells.

The info about a cell is represented like this:
```
{(row,column),(density,orbdensity)}
```
In solvepuzzle.py at the bottom, there is an example of a puzzle which is puzzle 8.
### People who **DO** know the secret
**Everything past this point contains spoilers**\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
The valid symbols for the terminal code are:\
Seperator: "."\
Blank Space: "-"\
Wall: "_"\
Block: "1"\
Worker: "w" or "W"\
End of Row: "/"\
Output: ">"\
Incinerator: "x" or "X"\
Infinity Block: "i" or "I" or "∞"
#### Notes:
Currently, Higher density blocks can only be accessed by a string of ones.\
Sorry.\
Just in case, you input the output after the puzzle, so it would look like:
```
puzzle>output
```


