def intercala_string(str1, str2):
    intercalada = ''
    for c1, c2 in zip(str1, str2):
        intercalada += c1 + c2
    if len(str1) > len(str2):
        intercalada += str1[len(str2):]
    elif len(str1) < len(str2):
        intercalada += str2[len(str1):]
    str1 = intercalada
    return str1
