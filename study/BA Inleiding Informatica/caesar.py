def caesar(n, string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    retstr = ""
    for i in string:
        if i.lower() in alphabet:
            if i.islower():
                index = alphabet.index(i)
                retstr += alphabet[(index + n) % 26]
            elif i.isupper():
                index = alphabet.index(i.lower())
                retstr += alphabet[(index + n) % 26].upper()
        else:
            retstr += i
    return retstr

input_string = "HGallo jaapje! GodverDOMME!!!"
print(caesar(13, input_string))
input_string = "AaBbCccDddd"
print(caesar(3, input_string))
