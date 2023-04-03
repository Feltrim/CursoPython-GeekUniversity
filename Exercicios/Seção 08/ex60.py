def find_substring(s: str, sub: str) -> int:
    """
    Retorna a primeira posição da sub-string 'sub' dentro da string 's'.
    Caso a sub-string não seja encontrada, retorna -1.
    """
    if sub == "":
        return 0
    for i in range(len(s)):
        if s[i:i+len(sub)] == sub:
            return i
    return -1
