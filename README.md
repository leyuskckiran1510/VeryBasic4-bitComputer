# VeryBasic4-bitComputer
This is just a raw implementation for just to feed out brain a dopamine
# instructions:-
  A       -> load data to A
  B       -> load data to B
  C       -> load data to C
  AB/BA   -> load data to AB
  AC/CA   -> Load data to AC
  BC/CB   -> load data to BC
  ABC/BCA -> load data to ABC and notaion
  JMP     -> jump to the nth line of code

## ===========================================
## Data values:-
## ===========================================
  A       -> 1000
  B       -> 1001
  C       -> 1010
  AB/BA   -> 1011
  AC/CA   -> 1100
  BC/CB   -> 1101
  ABC/BCA -> 1110
  JMP     -> 1111
  0       -> 0000
  1       -> 0111

## =========================================
### Explanation of opcode
## ==========================================
1001
^^-^------- these are data values according to the above table
|
------------First Bit Denotes I/comp(D) i:e 1=Instruciton/0=Data

## ==============================================
## Examples
## ===============================================
  A 1 //Sets A
  B 0 //Restes B
  JMP 2// goes to line 2
  AC 1 // Sets AC
  JMP 0 // goes to line 0
## ==================================================
## to implement later after basics
## =================================================
  A B //Both A and B will have same value as B has
  A AC //And Value of A and C goes to A
