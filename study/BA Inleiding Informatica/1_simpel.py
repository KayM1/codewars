# oefening 10.1
def oef1001():
    def opp_rechthoek(m,n):
        return m * n

    def main():
        opp = opp_rechthoek(5,2)
        print(opp)

    main()
pi = 3.14159265

# oefening 10.2
def oef1002():
    def opp_rechthoek(m,n):
        return m * n

    def opp_4kant(n):
        return opp_rechthoek(n,n)

    print(opp_4kant(6))

# oefening 10.4
def oef1004():
    def opp_cirkel(r):
        return str(r * r) + "pi"
    
    print(opp_cirkel(2))
    

def oef1005():
    def inhoud_bol(r):
        return r * r * r * (4/3) * pi
    
    print(inhoud_bol(2))
    
def oef1007():
    def print_tafel(n):
        for i in range(1,11):
            print(str(i) + " keer " + str(n) + " is " + str(i*n) + ".")
    print_tafel(15)

oef1007()


def watdoeik(string):
    ret = 0
    for i in string:
        if i == "*":
            ret += 1
    return ret

print(watdoeik("1*2*2*3"))0