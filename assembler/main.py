import os


def generator() -> dict[str, str]:
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
    "A": 8,
    "B": 9,
    "C": 10,
    "AB": 11,
    "AC": 12,
    "BC": 13,
    "ABC": 14,
    "JMP": 15,
}
## both are same
instructions = {
    "0": 0b0000,
    "1": 0b0001,
    "2": 0b0010,
    "3": 0b0011,
    "4": 0b0100,
    "5": 0b0101,
    "6": 0b0110,
    "7": 0b0111,
    "A": 0b1000,
    "B": 0b1001,
    "C": 0b1010,
    "AB": 0b1011,
    "AC": 0b1100,
    "BC": 0b1101,
    "ABC": 0b1110,
    "JMP": 0b1111,
}


def parse_file(file_name: str, is_relative: bool = True) -> bytes:
    object_data = b""
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
        temp = 0
        for word in line.split(" "):
            temp <<= 4
            word = "".join(sorted(word.strip().upper()))
            temp |= instructions[word]
        object_data += temp.to_bytes(length=1, byteorder="big")
    return object_data


def binary_object(input_file: str = "light_blinker.lkc", output_file: str = "output.bin"):
    bin_data = parse_file(input_file)
    print(bin_data)
    with open(output_file, "wb") as file:
        file.write(bin_data)


binary_object()
