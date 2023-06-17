import os

SYSTEM_BIT = 3


def generator(dirty: str = "") -> dict[str, str]:
    """
    it takes a `->` directed instruction and it's respective binary code and generates a
    instruciton dictonary
    """
    if not dirty:
        dirty = """A       -> 1000
        B       -> 1001
        C       -> 1010
        AB   -> 1011
        AC   -> 1100
        BC   -> 1101
        ABC -> 1110
        JMP     -> 1111
        0       -> 0000
        1       -> 0111"""
    instructions = {i.split("->")[0].strip(): f'0b{i.split("->")[1].strip()}' for i in dirty.split("\n")}
    return instructions


instructions = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "SUM": 8,
    "SUB": 9,
    "JNZ": 14,
    "JMP": 15,
    "RESET": 13,
}
## both are same
instructions = {
    "0": 0b0,
    "1": 0b1,
    "2": 0b10,
    "3": 0b11,
    "4": 0b100,
    "5": 0b101,
    "6": 0b110,
    "7": 0b111,
    "8": 0b1000,
    "9": 0b1001,
    "A": 0b1010,
    "B": 0b1011,
    "C": 0b1100,
    "SUM": 0b1000,
    "SUB": 0b1001,
    "JNZ": 0b1110,
    "JMP": 0b1111,
    "RESET": 0b1101,
}


def parse_file(file_name: str, is_relative: bool = True) -> bytes:
    object_data = b""
    temp = 0
    if is_relative:
        absolute_path = os.path.join(os.curdir, file_name)
    else:
        absolute_path = file_name
    if os.path.exists(absolute_path):
        with open(absolute_path, "r") as file:
            source = file.read()
    else:
        raise SystemError("File Cannot Be found please provide a valid path")
    for line in source.split("\n"):
        jumppy = 0
        line = line.strip()
        _loop_var = line.split(":")
        if len(_loop_var) == 2:
            instructions[_loop_var[0].strip().upper()] = len(object_data)
            line = _loop_var[-1]
        if line.startswith("#") or line.startswith("\\") or len(line.strip()) < 1:
            continue
        for word in line.split(" "):
            temp <<= 4
            word = word.strip().upper()
            if instructions.get(word, None) == None:
                break
            if not word:
                temp |= 0
                continue
            if jumppy:
                if temp != 0:
                    temp <<= 4
                temp |= instructions.get(word, 0) * 2
                object_data += temp.to_bytes(length=1, byteorder="big")
                temp = 0
                break
            else:
                temp |= instructions.get(word, 0)
            if word == "JMP" or word == "JNZ":
                jumppy = 1
            if len(bin(temp)) > 6:
                object_data += temp.to_bytes(length=1, byteorder="big")
                temp = 0
    object_data += temp.to_bytes(length=1, byteorder="big")
    return object_data if object_data else b"\x00"


def binary_object(input_file: str = "light_blinker.lkc", output_file: str = "output.bin"):
    bin_data = parse_file(input_file)
    print(bin_data)
    with open(output_file, "wb") as file:
        file.write(bin_data)


binary_object("temp.lkc")
