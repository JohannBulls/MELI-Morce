import bookshop


def menu():
    """
    Función que muestra nuevamente el menu
    """
    print("Selecciona una opción")
    print("\t1 - Texto a Morse")
    print("\t2 - Morse a Texto")
    print("\t3 - Morse a Bits")
    print("\t4 - Bits a Morse")
    print("\t5 - Texto a Bits a Morse")
    print("\t0 - Salir")


def menu_p():
    print("----> Bienvenidos a este programa <---- ")
    print("Usted podrá convertir texto a morse viceversa y bits a texto viceversa \n")


menu_p()
while True:
    menu()
    # solicituamos una opción al usuario
    opcionMenu = input(" >> ")

    if opcionMenu == "1":
        bookshop.texto_morse()
        print("")
    elif opcionMenu == "2":
        bookshop.morse_texto()
        print("")
    elif opcionMenu == "3":
        bookshop.morse_bits()
        print("")
    elif opcionMenu == "4":
        bookshop.bits_morse()
        print("")
    elif opcionMenu == "5":
        bookshop.txt_bits_morse()
        print("")
    elif opcionMenu == "0":
        print("-- Saliendo --")
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa Enter para continuar")


"""
Codigo Morse
.... --- .-.. .-   -- . .-.. ..
"""
