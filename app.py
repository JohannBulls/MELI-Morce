# Se importa Flask para el uso de api
#from flask import Flask

#app = Flask(__name__)

# Se importa la libreria bookshop
import bookshop

#@app.route("/menup")



def menu():
    
    #Función que muestra nuevamente el menu
    
    print("\nSelecciona una opción: ")
    print("\t1 - Texto a Morse.")
    print("\t2 - Morse a Texto.")
    print("\t3 - Morse a Bits.")
    print("\t4 - Bits a Morse.")
    print("\t5 - Texto a Bits a Morse.")
    print("\t0 - Salir.")


def menup():

    #Función que muestra la bienvenida del programa
    print("\n------------    Programa de mensajería discreta    ------------")
    print("\n-------------->   Bienvenidos a este programa   <--------------\n ")
    print("----------------------------------------------------------------")
    print("¦ Por medio de este programa podrá enviar mensajería de las    ¦\n¦ maneras indicadas a continuación, tenga en cuenta que al     ¦\n¦ escribirlo en morse al terminar la palabra deberá indicar    ¦\n¦ dos espacios o más. También tenga en cuenta que al momento   ¦")
    print("¦ de escribir en cualquiera de las formas no ingresar          ¦\n¦ caracteres especiales (@,-*&/+ etc …)                       ¦")
    print("----------------------------------------------------------------")
    return "El progrma se esta ejecutando en consola"


menup()


while True:
    menu()
    # Solicituamos una opción al usuario
    opcionMenu = input(" >> ")

    if opcionMenu == "1":
        x=bookshop.texto_morse()
        print(x)
        print("")
    elif opcionMenu == "2":
        x=bookshop.morse_texto()
        print(x)
        print("")
    elif opcionMenu == "3":
        x=bookshop.morse_bits()
        print(x)
        print("")
    elif opcionMenu == "4":
        x=bookshop.bits_morse()
        print(x)
        print("")
    elif opcionMenu == "5":
        x,y=bookshop.txt_bits_morse()
        print(x)
        print(">>> La traduccion a Bits a Morse es:")
        print(y)
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
#if __name__ == '__main__':
    #app.run(debug=True, port=4000)