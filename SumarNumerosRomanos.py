#Programa para sumar numeros Romanos, sin el uso de conversiones a otros sistemas numericos

def main():
    #Escaneo de los numeros.
    numero1 = input(str("Ingrese el primer numero: "))
    numero2 = input(str("Ingrese el segundo numero: "))
    #Cadenas iniciales
    print("1. ",numero1)
    print("2. ",numero2)
    #Descomponer cadenas
    numero1 = descomponerCadena(numero1)
    numero2 = descomponerCadena(numero2)
    print("1. ",numero1)
    print("2. ",numero2)
    #Concatenar en una cadena
    cadenaResult = numero1+numero2
    print(str(cadenaResult))
    cadenaResult = ordenarCadena(cadenaResult)
    #Componer cadena
    cadenaResult = componerCadena(cadenaResult)
    #Reescribir la cadena   
    cadenaResult = reescribirCadena(cadenaResult)
    print("Resultado ",cadenaResult,end="")
    
    
def descomponerCadena(cadena):
    str.upper(cadena)
    if "IV" in cadena:
        cadena = cadena.replace("IV","IIII")
    if "IX" in cadena:
        cadena = cadena.replace("IX","VIIII")
    if "XL" in cadena:
        cadena = cadena.replace("XL","XXXX")
    if "XC" in cadena:
        cadena = cadena.replace("XC","LXXXX")
    if "CD" in cadena:
        cadena = cadena.replace("CD","CCCC")
    if "CM" in cadena:
        cadena = cadena.replace("CM","DCCCC")
    return cadena 
    
def ordenarCadena(cadena):
    cadenaAux = []
    for i in range (cadena.count("M")):
        cadenaAux.append("M")
    for i in range (cadena.count("D")):
        cadenaAux.append("D")
    for i in range (cadena.count("C")):
        cadenaAux.append("C")
    for i in range (cadena.count("L")):
        cadenaAux.append("L")
    for i in range(cadena.count("X")):
        cadenaAux.append("X")
    for i in range (cadena.count("V")):
        cadenaAux.append("V")
    for i in range (cadena.count("I")):
        cadenaAux.append("I")    
    cadena = ""
    return cadena.join(cadenaAux)

def componerCadena(cadena):
    if "DCCCC" in cadena:
        cadena = cadena.replace("DCCCC","CM")
    if "CCCC" in cadena:
        cadena = cadena.replace("CCCC","CD")
    if "LXXXX" in cadena:
        cadena = cadena.replace("LXXXX","XC")
    if "XXXX" in cadena:
        cadena = cadena.replace("XXXX","XL")
    if "VIIII" in cadena:
        cadena = cadena.replace("VIIII","IX")
    if "IIII" in cadena:
        cadena = cadena.replace("IIII","IV")
    return cadena

def reescribirCadena(cadena):
    if (cadena.count("D") == 2):
        cadena = cadena.replace("DD","M")
    elif (cadena.count("D") == 3):
        cadena = cadena.replace("DDD","MD")
    elif (cadena.count("D") == 4):
        cadena = cadena.replace("DDDD","MM")
    elif (cadena.count("D") == 5):
        cadena = cadena.replace("DDDDD","MMD")
    elif (cadena.count("D") == 6):
        cadena = cadena.replace("DDDDDD","MMM")
    elif (cadena.count("D") == 7):
        cadena = cadena.replace("DDDDDDD","MMMD")
    else:
        pass
    if (cadena.count("C") == 4):
        cadena = cadena.replace("CCCC","CD")
    elif (cadena.count("C") == 5):
        cadena = cadena.replace("CCCCC","D")
    elif (cadena.count("C") == 6):
        cadena = cadena.replace("CCCCCC","DC")
    elif (cadena.count("C") == 7):
        cadena = cadena.replace("CCCCCCC","DCC")
    elif (cadena.count("C") == 8):
        cadena = cadena.replace("CCCCCCCC","DCCC")
    elif (cadena.count("C") == 9):
        cadena = cadena.replace("CCCCCCCCC","CM")
    else:
        pass
    if (cadena.count("L") == 2):
        cadena = cadena.replace("LL","C")
    elif (cadena.count("L") == 3):
        cadena = cadena.replace("LLL","CL")
    elif (cadena.count("L") == 4):
        cadena = cadena.replace("LLLL","CC")
    elif (cadena.count("L") == 5):
        cadena = cadena.replace("LLLL","CCL")
    elif (cadena.count("L") == 6):
        cadena = cadena.replace("LLLLL","CCC")
    elif (cadena.count("L") == 7):
        cadena = cadena.replace("LLLLLLL","CCCL")
    elif (cadena.count("L") == 8):
        cadena = cadena.replace("LLLLLLLL","CD")
    else:
        pass
    if (cadena.count("X")) == 4:
        cadena = cadena.replace("XXXX","XL")
    elif (cadena.count("X") == 5):
        cadena = cadena.replace("XXXXX","L")
    elif (cadena.count("X") == 6):
        cadena = cadena.replace("XXXXXX","LX")
    elif (cadena.count("X") == 7):
        cadena = cadena.replace("XXXXXXX","LXX")
    elif (cadena.count("X") == 8):
        cadena = cadena.replace("XXXXXXXXX","LXXX")
    elif (cadena.count("XXXXXXXXX") == 9):
        cadena = cadena.replace("X","XC")
    else:
        pass
    if (cadena.count("I") == 4):
        cadena = cadena.replace("IIII","IV")
    elif (cadena.count("I") == 5):
        cadena = cadena.replace("IIIII","V")
    elif (cadena.count("I") == 6):
        cadena = cadena.replace("IIIIII","VI")
    elif (cadena.count("I") == 7):
        cadena = cadena.replace("IIIIIII","VII")
    elif (cadena.count("I") == 8):
        cadena = cadena.replace("IIIIIIII","VIII")
    elif (cadena.count("I") == 9):
        cadena = cadena.replace("IIIIIIIII","IX")
    else:
        pass
    if (cadena.count("V") == 2):
        cadena = cadena.replace("VV","X")
    elif (cadena.count("V") == 3):
        cadena = cadena.replace("VVV","XV")
    elif (cadena.count("V") == 4):
        cadena = cadena.replace("VVVV","XX")
    elif (cadena.count("V") == 5):
        cadena = cadena.replace("VVVVV","XXV")
    elif (cadena.count("V") == 6):
        cadena = cadena.replace("VVVVVV","XXX")
    elif (cadena.count("V") == 7):
        cadena = cadena.replace("VVVVVVVV","XXXV")
    elif (cadena.count("V") == 8):
        cadena = cadena.replace("VVVVVVVV","XL")
    else:
        pass
    return cadena

#Llamada a la funcion principal
main()