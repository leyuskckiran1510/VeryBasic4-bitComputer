# VeryBasic4-bitComputer


This is just a raw implementation for just to feed out brain a dopamine <br>
It uses 3bit for data and 1 bit for data/instruction mode; So in total it's a 4bit programmable computer<br>
Which can be used to build light system or other system. Their is no physical computer as per to say as<br>
it's just a raw circuit and you can visualize it on [Logisim-Evlution](https://github.com/logisim-evolution/logisim-evolution). Open [Single_BIT](./single_bit_comp.circ) or [ThreeBit](./three_bit_comp.circ) in logisim.                      <br>
# instructions:-                                      
  A       -> load data to A                           <br>
  B       -> load data to B                           <br>
  C       -> load data to C                           <br>
  JNZ     -> jump when C is not zero(conditional jump)<br>
  JMP     -> jump to the nth line of code             <br>


## Data values:- 

  A       -> 1000 <br>
  B       -> 1001 <br>
  C       -> 1010 <br>
  SUM     -> 1011 <br>
  SUB     -> 1100 <br>
          -> 1101 <br>
  JNZ     -> 1110 <br>
  JMP     -> 1111 <br>
  0       -> 0000 <br>
  1       -> 0111 <br>


### Explanation of opcode

1001 <br>
^^-^------- these are data values according to the above table   <br>
| <br>
------------First Bit Denotes I/comp(D) i:e 1=Instruciton/0=Data <br>


## Examples <br>

> A 1      || Set value of A to 1               <br>
> B 0      || Set value of B to 0               <br>
> JMP 2    || Go  to line 2                     <br>
> JMP 0    || Go  to line 0                     <br>
> A 7      || Set A with value 7                <br>
> A B      || Move content of B to A || `A <- B`<br>
> A C      || Move content of C to A            <br>
> C A      || move content of A to C || `C <- A`<br>
Use '#' to comment out the line comment         <br>
And any words after first two words will be rejected/ignored<br>
example:-<br>
 A 5 this loads 5 to A<br>
 ^ ^---second word    <br>
 |-----first word     <br>
 the ` this loads 5 to A` will be ignored                                           <br>


### Look at files Code Example for any refrence


 1)[It's displays 123456000456000456....](./assembler/light_blinker.lkc) in 7-segment<br>
 2)[It moves three stips of light/led from left to right and loops back infintely](./assembler/left_to_right_window.lkc) in main output led                                        <br>

