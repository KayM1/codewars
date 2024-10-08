def rot13(text):
  # alphabet = "nopqrstuvwxyzabcdefghijklm"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    retstr = ""
    for i in text:
        if i == " ":
            retstr = retstr + " "
            continue
        index = alphabet.index(i.lower())
        retstr = retstr + alphabet[(index + 13) % 26]
    return retstr

naam = input()
print(rot13(naam))