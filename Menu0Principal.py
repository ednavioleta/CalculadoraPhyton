import Menu1
import Menu2


def inicio():
    print ("""
 ************************************************
 ***** Calculadora de operaciones en Python *****
 *****     Ingrese los valores a operar     *****
 *****     Seleccionar tipo de operacion    *****
 ************************************************ """)    

def menuPrincipal():
    opc=None
    while opc != 7:
        print ("""
*******************************************
   FUNCIONES
1. Funciones matemáticas incorporadas
2. Funciones matematicas del módulo math
3. Funciones trigonométricas
4. Funciones hiperbólicas
5. Funciones de constantes
6. Otras funciones avanzadas
7. Salir
******************************************** """)    
        try:
            opc=int(input("Elige una opcion -> "))
            if   opc == 1: Menu1.matematicasIncorporadas()
            elif opc == 2:


            elif opc == 7: print("Saliendo del programa .......")
            else:          print("Opcion no valida.......")    
        except ValueError:
            print("Selección no es valida")

inicio()
menuPrincipal()
