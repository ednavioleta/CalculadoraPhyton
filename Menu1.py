import pedir

def matematicasIncorporadas():
    opc=None
    while opc != 9:
        print ("""
*******************************************
FUNCIONES
1. abs(x): Devuelve el valor absoluto de un número.
2. round(x, n): Redondea un número a n decimales (o a un entero si no se especifica n).
3. pow(x, y): Calcula el valor de x elevado a la potencia y (equivalente a x ** y).
4. divmod(x, y): Devuelve una tupla con el cociente y el resto de la división de x entre y.
5. sum(iterable): Suma los elementos de un iterable.
6. min(iterable): Devuelve el valor mínimo de un iterable.
7. max(iterable): Devuelve el valor máximo de un iterable. 
8. Otras funciones avanzadas
9. Salir
******************************************** """)    
        try:
            opc=int(input("Elige una opcion -> "))
            if   opc < 9: Vr1 , Vr2 = pedir.pedirDatos()
            elif opc == 1: 
            elif opc == 2:


            elif opc == 9: print("Saliendo del programa .......")
            else:          print("Opcion no valida.......")    
        except ValueError:
            print("Selección no es valida")     