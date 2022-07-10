# Diccionario de abecedario a morse

dicctm = {
    'A': '.-',
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "----",
    "1": ".---",
    "2": "..--",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "-.-.--",
    "?": "..--..",
    "\"": ".-..-.",
    " ": " ",
    "  ": ".-.-.-"
}

# Diccionario de binario a morse

diccbm = {
    "01000001": ".-",
    "01000010": "-...",
    "01000011": "-.-.",
    "01000100": "-..",
    "01000101": ".",
    "01000110": "..-.",
    "01000111": "--.",
    "01001000": "....",
    "01001001": "..",
    "01001010": ".---",
    "01001011": "-.-",
    "01001100": ".-..",
    "01001101": "--",
    "01001110": "-.",
    "11010001": "--.--",
    "01001111": "---",
    "01010000": ".--.",
    "01010001": "--.-",
    "01010010": ".-.",
    "01010011": "...",
    "01010100": "-",
    "01010101": "..-",
    "01010110": "...-",
    "01010111": ".--",
    "01011000": "-..-",
    "01011001": "-.--",
    "01011010": "--..",
    "0000": "----",
    "0001": ".---",
    "0010": "..--",
    "0011": "...--",
    "0100": "....-",
    "0101": ".....",
    "0110": "-....",
    "0111": "--...",
    "1000": "---..",
    "1001": "----.",
    "": " "
}

def espacio(x):

    #Funcion que agrega un espcio entre cada frase

    lista, fra = [], ""
    for i in range(len(x)):
        if x[i] != " ":
            fra += x[i]
        else:
            lista.append(fra)
            fra = ""
    lista.append(fra)
    return(lista)


def texto_morse():

    #Funcion para traducir de Texto a morse

    new = ""
    x = list(input("Ingrese una frase:   ").upper())
    for i in range(len(x)):
        new += dicctm[x[i]] + " "
    print(">>> La traduccion a Morse es")
    return(new)


def morse_texto():

    #Funcion para traducir de morse a texto
    print("ejemplo de binario")
    print(".... --- .-.. .-   -- . .-.. ..")
    list_of_key = list(dicctm.keys())
    list_of_value = list(dicctm.values())
    new = ""

    x = list(input("Ingrese el Codigo Morse:   "))
    x = espacio(x)
    for i in range(len(x)):
        if x[i] == "":
            x[i] = " "
        position = list_of_value.index(x[i])
        new += list_of_key[position]
    print(">>> La traduccion a Texto es")
    return(new)


def morse_bits():

    #Funcion para traducir de morse a bits

    list_of_key = list(diccbm.keys())
    list_of_value = list(diccbm.values())
    new = ""
    x = input("Ingrese el Codigo Morse:   ").split()
    for i in range(len(x)):
        position = list_of_value.index(x[i])
        new += list_of_key[position]
    print(">>> La traduccion a Bits es")
    return(new)


def bits_morse():

    #Funcion para traducir de bits a morse

    print("Ejemplo de binario")
    print("00000000110110110011100000111111000111111001111110000000111011111111011101110000000110001111110000000000111111001111110000000110000110111111110111011100000011011100000000000")
    x = list(input("Ingrese el Binario:   "))
    morse, cont, cont_0 = "", 0, 0
    for i in x:
        if i == "1":
            cont += 1
        else:
            cont_0 += 1
            if cont > 3:
                morse += "-"
                cont, cont_0 = 0, 0

            elif cont > 0:
                morse += "."
                cont, cont_0 = 0, 0
            if cont_0 > 2 and cont_0 <= 6:
                morse += " "
                cont_0 = 0
            elif cont_0 > 6:
                morse += ".-.-.-"
                cont_0 = 0
    print(">>> La traduccion de Bits a morse es:")
    return(morse)

def txt_bits_morse():

    #Funcion para traducir de Texto a bits a morse

    list_of_key = list(diccbm.keys())
    list_of_value = list(diccbm.values())
    new, new_2, new_3 = "", "", ""
    x = list(input("Ingrese una frase:   ").upper())
    for i in range(len(x)):
        new_2 = dicctm[x[i]]
        new_3 += new_2+" "
        position = list_of_value.index(new_2)
        new += list_of_key[position]
    print(">>> La traduccion a Texto a Bits es:")
    return(new,new_3)

