"""
How it works
 each line denots a single time,
 1 means to turnon the LED
 0 means to turnoff the LED
 loop means to go back to first line
 loop N means goto Nth line
 This generator will ignore any code after loop;
 If you want to use loop properly please do try actuall coding 

In below as you can see each time three lights gets on and they are moved towards left
"""
from re import template
from typing import List


light_pattren = """
111000000
011100000
001110000
000111000
000011100
000001110
000000111
100000011
110000001
loop
"""
# this also another nice looking pattren
light_pattren = """
101010101
010101010
101010101
010101010
101010101
010101010
000000000
100000000
110000000
111000000
111100000
111110000
111111000
111111100
111111110
111111111
111111111
011111111
001111111
000111111
000011111
000001111
000000111
000000011
000000001
000000000
loop 6
"""
A = 0
B = 0
C = 0


def all_same(x: List[int]) -> bool:
    return max(x) == min(x)


def gen_line(abc_value: List[int]) -> str:
    global A, B, C
    line = ""

    if all_same(abc_value):
        if A == abc_value[0]:
            line = ""
        else:
            line = f"ABC {abc_value[0]}"
    elif abc_value[0] == abc_value[1]:
        if A == abc_value[0] and A == B:
            line = f"C {abc_value[2]}"
        elif C == abc_value[2]:
            line = f"AB {abc_value[0]}"
        else:
            line = f"AB {abc_value[0]}\nC {abc_value[2]}"
    elif abc_value[0] == abc_value[2]:
        if A == abc_value[0] and A == C:
            line = f"B {abc_value[1]}"
        elif B == abc_value[2]:
            line = f"AC {abc_value[0]}"
        else:
            line = f"AC {abc_value[0]}\nB {abc_value[1]}"
    elif abc_value[1] == abc_value[2]:
        if B == abc_value[1] and B == C:
            line = f"A {abc_value[0]}"
        elif A == abc_value[2]:
            line = f"BC {abc_value[1]}"
        else:
            line = f"A {abc_value[0]}\nBC {abc_value[1]}"
    else:
        line = f"A {abc_value[0]}\nB {abc_value[1]}\nC {abc_value[2]}"
    A, B, C = abc_value
    return line


def generate(light_pattren: str) -> str:
    source = ""
    line_label = {}
    gen_index = 0
    for n, i in enumerate(light_pattren.split("\n")):
        if not i:
            continue
        if i.startswith("loop"):
            source += f"JMP"
            if len(i.split(" ")) >= 2:
                to = int(i.split(" ")[1])
                source += f" {line_label[to]}\n"
            break
        temp_line = gen_line([int(i[:3], base=2), int(i[3:6], base=2), int(i[6:], base=2)])
        source += f"{temp_line}\n"
        gen_index += len(temp_line.split("\n"))
        line_label[n] = gen_index
    print(line_label)
    return source


def main():
    with open("temp.lkc", "w") as fl:
        fl.write(generate(light_pattren=light_pattren))


if __name__ == "__main__":
    main()
