# VeryBasic4-bitComputer <br>
This is just a raw implementation for just to feed out brain a dopamine <br>
It uses 3bit for data and 1 bit for data/instruction mode; So in total it's a 4bit programmable computer
Which can be used to build light system or other system
# instructions:- <br>
  A       -> load data to A <br>
  B       -> load data to B  <br>
  C       -> load data to C <br>
  AB/BA   -> load data to AB <br>
  AC/CA   -> Load data to AC <br>
  BC/CB   -> load data to BC <br>
  ABC/BCA -> load data to ABC and notaion <br>
  JMP     -> jump to the nth line of code <br>

## =========================================== <br>
## Data values:- <br>
## =========================================== <br>
  A       -> 1000 <br>
  B       -> 1001 <br>
  C       -> 1010 <br>
  AB/BA   -> 1011 <br>
  AC/CA   -> 1100 <br>
  BC/CB   -> 1101 <br>
  ABC/BCA -> 1110 <br>
  JMP     -> 1111 <br>
  0       -> 0000 <br>
  1       -> 0111 <br>

## =========================================
### Explanation of opcode
## ==========================================
1001 <br>
^^-^------- these are data values according to the above table <br>
| <br>
------------First Bit Denotes I/comp(D) i:e 1=Instruciton/0=Data <br>

## ==============================================
## Examples <br>
## ===============================================
  A 1 //Sets A <br>
  B 0 //Restes B <br>
  JMP 2// goes to line 2 <br>
  AC 1 // Sets AC <br>
  JMP 0 // goes to line 0 <br>
  A 7 // sets A with value 7
 Use '#' to comment out the line comment
 And any words after first two words will be rejected/ignored
 example:-
 A 5 this loads 5 to A
 ^ ^---second word
 |-----first word 
 the ` this loads 5 to A` will be ignored
 look at file './light_blinker.lkc' for any refrence
## ==================================================
## to implement later after basics <br>
## =================================================
  A B //Both A and B will have same value as B has OR `move content of B to A` <br>
  A AC //And Value of A and C goes to A OR `move content of AC to A` <br>
