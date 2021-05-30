# SOLVING THE KLOTSKI PUZZLE USING RECURSION

In this python project, I solve the Klotski puzzle using recursion. No optimisations have been done here, however, it can further be worked upon to improve its **effiecieny** . Below I have tried to explain my methodology as simply as I could.

The klotski_puzzle.py file takes around 4,000 steps to solve. This is the minimum number of steps I could achieve, using recursion. Other permutations, either resulted in no soultion or were in the 25000-35000 range.

### HOW DOES IT WORK

The starting board, like the real life Klotski Puzzle looks like this - 

[['B1' 'R1' 'R1' 'B2']

 ['B1' 'R1' 'R1' 'B2']
 
 ['B3' 'P1' 'P1' 'B4']
 
 ['B3' 'G1' 'G2' 'B4']
 
 ['G3' 'XX' 'XX' 'G4']] 

It selects the blocks in this particular order: 

    redOne,
    greenTwo,
    greenOne,
    greenThree,
    greenFour,
    pinkBlock,
    blueOne,
    blueTwo,
    blueThree,
    blueFour,
    
Once it find a block that has an empty neighbour, and if the box can move their (due to the varying sizes of the box), the algorithm moves the box to the empty space and calls the function again. 

#### THE PROBLEM

The problem is that recursion can cause same patterns to repeat endlessly. For example ---- 

[['B1' 'R1' 'R1' 'B2']

 ['B1' 'R1' 'R1' 'B2']
 
 ['B3' 'P1' 'P1' 'B4']
 
 ['B3' 'G1' 'G2' 'B4']
 
 ['G3' 'XX' 'XX' 'G4']] 


|
|
|
|
|
|
|


[['B1' 'R1' 'R1' 'B2']

 ['B1' 'R1' 'R1' 'B2']
 
 ['B3' 'P1' 'P1' 'B4']
 
 ['B3' 'XX' 'G2' 'B4']
 
 ['G3' 'G1' 'XX' 'G4']] 
 
 
 If I move G1 first, this pattern will go on repeating endlessly. To counter it, I made a 3D array called patterns, that records all the patterns that the puzle board has been in. If a repeating pattern occurs, the block won't move and will instead go to a new block.
 
 All of the methods have comments over them in the file to help understand them better.
 
 #### I NEED YOUR HELP
 
 Since the Klotski puzzle can be solved in less than a 100 steps easily, please help me develop Klotski puzzle to solve it heuristically.
 
 Thank you for taking interest. My email id : harjaishivam@gmail.com
 
 
 
 
 

