def isLongPressedName(name, typed):
    name_pointer = 0
    typed_pointer = 0
    name_len = len(name)
    typed_len = len(typed)
    prev = name[0]

    while True:
        if ((name_pointer == name_len - 1) and (typed_pointer == typed_len -1)):
            if name[name_pointer] == typed[typed_pointer]:
                return True
            return False
        name_char = name[name_pointer]
        typed_char = typed[typed_pointer]
        
        if name_char == typed_char:
            prev = name_char
            if name_pointer < name_len - 1:
                name_pointer += 1
            if typed_pointer < typed_len - 1:
                typed_pointer += 1
            continue
        if typed_char == prev:
            if typed_pointer < typed_len -1:
                typed_pointer += 1
            continue
        return False
print(isLongPressedName("alex", "alex"))