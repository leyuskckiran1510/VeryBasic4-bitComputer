# VeryBasic4-bitComputer


It's a 4-bit programable micro-controller,That has only LOAD,MOV,SUB,ADD,JNZ,JMP and RESET features due<br>it's limit of 4-bit instruciton set. It uses 8-bit address bus for addressing upto 255-addresses<br>
meaning upto 255 instructions can be loaded.<br>
It uses 4-bit in a clever way to make room for more instrucitons. Like first 10sets are used up by number<br>from 0-9 `but we use number explictly only during load process so, we can check if we are currenlty`<br>`in load mode or not if not then treat those as instructions which allowed me to add more Instruction`<br>`set.`
After the addition of `JNZ` now we can do conditional programming , and the `ADD & SUB` feature allows<br> to have more controll over the A,B & C registers.
It is  a raw circuit and you can visualize it on [Logisim-Evlution](https://github.com/logisim-evolution/logisim-evolution). Open up the last modified .circ file as I am adding new feature in new circuit every<br>day.

# instructions:-                                      
  A       -> load data to A                           <br>
  B       -> load data to B                           <br>
  C       -> load data to C                           <br>
  JNZ     -> jump when C is not zero(conditional jump)<br>
  JMP     -> jump to the nth line of code             <br>
  SUB     -> subtract from choosen register           <br>
  ADD     -> add to choosen register                  <br>

## Opcode values:- 

    IR       Value
    0     -> 0b0        <br>
    1     -> 0b1        <br>
    2     -> 0b10       <br>
    3     -> 0b11       <br>
    4     -> 0b100      <br>
    5     -> 0b101      <br>
    6     -> 0b110      <br>
    7     -> 0b111      <br>
    8     -> 0b1000     <br>
    9     -> 0b1001     <br>
    A     -> 0b1010     <br>
    B     -> 0b1011     <br>
    C     -> 0b1100     <br>
    SUM   -> 0b1000     <br>
    SUB   -> 0b1001     <br>
    JNZ   -> 0b1110     <br>
    JMP   -> 0b1111     <br>
    RESET -> 0b1101     <br>



### Explanation of opcode
    Every instructions has their own binary value. And due to lack of enough bits<br>
    the numericals bits are reused for other instrucitons as the numericals are only<br>
    used while on LOAD and JUMP process so on everyother situation the numbers bits will<br>
    be used for other instructions set to make it more functional.


## Examples <br>

    A 1                         || Set value of A to 1               <br>
    label1:B 0                  || Set value of B to 0               <br>
        JMP label1              || Go  to line with label1           <br>
    A 7                         || Set A with value 7                <br>
    A B                         || Move content of B to A || `A <- B`<br>
    A C                         || Move content of C to A            <br>
    C A                         || move content of A to C || `C <- A`<br>
    SUB C 1                     || subrtact one from C
    ADD C 5                     || add 5 to C
    ADD A 9                     || add 9 to A 

    #### Conditional Looping example
    A 9
    C 9
    loop SUB C 1
         SUB A 1
         JNZ loop

    This loop will continue until C is zero

Use '#' to comment out the line comment         <br>


### Look at files Code Example for any refrence


 1)[It's displays 123456000456000456....](./assembler/light_blinker.lkc) in 7-segment<br>
 2)[It moves three stips of light/led from left to right and loops back infintely](./assembler/left_to_right_window.lkc) in main output led                                        <br>

### To implement    
    Insted of realing on `C` to be zero add a FLAG register with these values:-
    Z -> if last operation yeild zero or not
    C -> if last operation yeild carry or not
    And new Instructions like
    JNC/JC one of it
