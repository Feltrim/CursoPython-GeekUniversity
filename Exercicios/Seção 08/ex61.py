def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    freq1 = {}
    freq2 = {}
    for c in str1:
        freq1[c] = freq1.get(c, 0) + 1
    for c in str2:
        freq2[c] = freq2.get(c, 0) + 1

    return freq1 == freq2
