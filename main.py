def decimal_to_binary(N: int) -> str:

    res = ""
    while(N):
        res += str(N % 2)
        N //= 2

    while len(res) < 4:
        res += "0"

    return res[::-1]


def list_to_str(arr):
    _str = ""
    for x in arr:
        _str += str(x)
    
    return _str


def translator(instruction) -> str:
    binary_code = ["0"] * 12

    op_code = instruction[0]

    if(op_code == "MOV"):
        binary_code[0:2] = "10"
        binary_code[2:5] = decimal_to_binary(int(instruction[1][1]))[1:4]
        binary_code[8:12] = decimal_to_binary(int(instruction[2]))
    else:
        if(op_code == "ADD"):
            binary_code[0:2] = "00"
            binary_code[2:5] = decimal_to_binary(int(instruction[1][1]))[1:4]
            binary_code[5:8] = decimal_to_binary(int(instruction[2][1]))[1:4]
        else:
            if(op_code == "NEG"):
                binary_code[0:2] = "01"
                binary_code[2:5] = decimal_to_binary(int(instruction[1][1]))[1:4]
            else:
                if(op_code == "JZR"):
                    binary_code[0:2] = "11"
                    binary_code[2:5] = decimal_to_binary(int(instruction[1][1]))[1:4]
                    binary_code[8:12] = decimal_to_binary(int(instruction[2]))
                else:
                    print("Invalid Instruction")
                    return
    
    print(list_to_str(binary_code))


def get_input():
    user_input = input()
    normalized_input = user_input.replace(",", " ")
    fields = [part.strip() for part in normalized_input.split() if part.strip()]

    if(len(fields) > 3):
        return -1

    if (len(fields) < 3):
        fields.append("")

    if (fields[0] != "MOV" and fields[0] != "ADD" and fields[0] != "NEG" and fields[0] != "JZR"):
        return -1
    
    if (fields[0] == "MOV"):
        if (fields[1][0] != "R" or int(fields[1][1]) < 0 or int(fields[1][1]) >= 8 or int(fields[2]) < 0 or int(fields[2]) >= 16):
            return -1
        
    if (fields[0] == "ADD"):
        if (fields[1][0] != "R" or int(fields[1][1]) < 0 or int(fields[1][1]) >= 8 or fields[2][0] != "R" or int(fields[2][1]) < 0 or int(fields[2][1]) >= 8):
            return -1
    
    if (fields[0] == "NEG"):
        if (fields[1][0] != "R" or int(fields[1][1]) < 0 or int(fields[1][1]) >= 8 or fields[2] != ""):
            return -1
    
    if(fields[0] == "JZR"):
        if (fields[1][0] != "R" or int(fields[1][1]) < 0 or int(fields[1][1]) >= 8 or int(fields[2]) < 0 or int(fields[2]) >= 8):
            return -1
        
    return fields


if __name__ == "__main__":
    print("Main function\n")

    while True:
        user_input = get_input()
        if(user_input != -1):
            translator(user_input)
        else:
            print("Invalid Instruction")
