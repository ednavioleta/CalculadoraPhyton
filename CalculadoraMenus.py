#Definición de funciones
def inicio():
    print ("""
 ************************************************
 ***** Calculadora de operaciones en Python *****
 *****     Ingrese los valores a operar     *****
 *****     Seleccionar tipo de operacion    *****
 ************************************************ """)    
def pedirDatos():
    a = int(input("Digite el primer valor  -> "))
    b = int(input("Digite el segundo valor -> "))
    return a,b
def menuPrincipal():
    opc = None
    while opc != 6: 
        print("""
    OPERACIONES
 1. Operaciones Matemáticas
 2. Operaciones de Comparación
 3. Operaciones Lógicas
 4. Operaciones de Asignación
 5. Operaciones de bits
 6. Salir """) 
        try:
            opc = int(input("Elige una opción        -> "))
            if   opc==1: matemáticas()
            elif opc==2: comparación()
            elif opc==3: logicas()
            elif opc==4: asignacion()
            elif opc==5: bits()
            elif opc==6: print("Saliendo del programa .......")
            else:        print("Opcion no valida.......")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")
def matemáticas():
    opc = None
    while opc != 8:
        print("""
    OPERACIONES MATEMATICAS       
 1. Suma             +
 2. Resta            -  
 3. Multiplicación   *
 4. División         /
 5. División Entera  //
 6. Módulo           %
 7. Exponenciación   **
 8. Menu Principal   <--""")
        try:
            opc = int(input("Elige una opción        -> "))
            if   opc < 8: Vr1 , Vr2 = pedirDatos()
            if   opc==1: suma(Vr1,Vr2)
            elif opc==2: resta(Vr1,Vr2)
            elif opc==3: multiplica(Vr1,Vr2)
            elif opc==4: divide(Vr1,Vr2)
            elif opc==5: divideEntera(Vr1,Vr2)
            elif opc==6: modulo(Vr1,Vr2)
            elif opc==7: exponente(Vr1,Vr2)
            elif opc==8: menuPrincipal()
            else:        print("Opcion no valida.......")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def comparación():
    opc = None
    while opc != 7:
        print("""
    OPERACIONES DE COMPARACIÓN
 1. Igual a           == 
 2. Diferente de      != 
 3. Mayor que         >
 4. Menor que         < 
 5. Mayor o igual que >=
 6. Menor o igual que <=
 7. Menu Principal    <--""")
        try:
            opc = int(input("Elige una opción        -> "))
            if   opc < 7: Vr1 , Vr2 = pedirDatos()
            if   opc==1: igual(Vr1,Vr2)
            elif opc==2: diferente(Vr1,Vr2)
            elif opc==3: mayorQue(Vr1,Vr2)
            elif opc==4: menorQue(Vr1,Vr2)
            elif opc==5: mayorIgual(Vr1,Vr2)
            elif opc==6: menorIgual(Vr1,Vr2)
            elif opc==7: menuPrincipal()
            else:        print("Opcion no valida.......")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def logicas():
    opc = None
    while opc != 4:
        print("""
    OPERACIONES LOGICAS
 1. y lógico         and
 2. o lógico         or 
 3. negación lógica  not
 4. Menu Principal <----""")
        try:
            opc = int(input("Elige una opción        -> "))
            if   opc < 4: Vr1 , Vr2 = pedirDatos()
            if   opc==1: yLogico(Vr1,Vr2)
            elif opc==2: oLogico(Vr1,Vr2)
            elif opc==3: noLogico(Vr1,Vr2)
            elif opc==4: menuPrincipal()
            else:        print("Opcion no valida.......")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def asignacion():
    opc = None
    while opc != 9:
        print("""
    OPERACIONES DE ASIGNACION
 1. Asignación               =
 2. Suma y asigna            +=
 3. Resta y asigna           -=
 4. Multiplica y asigna      *=
 5. Divide y asigna          /=
 6. División entera y asigna //=
 7. Módulo y asigna          %=
 8. Exponente y asigna       **=            
 9. Menu Principal <------------""")
        try:
            opc = int(input("Elige una opción        -> "))
            if   opc < 9: Vr1 , Vr2 = pedirDatos()
            if   opc==1: asigna(Vr1,Vr2)
            elif opc==2: sAsigna(Vr1,Vr2)
            elif opc==3: rAsigna(Vr1,Vr2)
            elif opc==4: mAsigna(Vr1,Vr2)
            elif opc==5: dAsigna(Vr1,Vr2)
            elif opc==6: deAsigna(Vr1,Vr2)
            elif opc==7: modAsigna(Vr1,Vr2)
            elif opc==8: expAsigna(Vr1,Vr2)
            elif opc==9: menuPrincipal()
            else:        print("Opcion no valida.......")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def bits():
    opc = None
    while opc != 7:
        print("""
    OPERACIONES CON BITS
1. AND a nivel de bits            &
2. OR a nivel de bits             |
3. XOR a nivel de bits            ^
4. NOT a nivel de bits            ~
5. Desplazamiento a la izquierda  <<
6. Desplazamiento a la derecha    >>
7. Menu Principal <-----------------""")
        try: 
            opc = int(input("Elige una opción        -> "))
            if   opc < 7: Vr1 , Vr2 = pedirDatos()
            if   opc==1: yBit(Vr1,Vr2)
            elif opc==2: oBit(Vr1,Vr2)
            elif opc==3: xoBit(Vr1,Vr2)
            elif opc==4: noBit(Vr1,Vr2)
            elif opc==5: diBit(Vr1,Vr2)
            elif opc==6: ddBit(Vr1,Vr2)
            elif opc==7: menuPrincipal()
            else:        print("Opcion no valida.......")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")
def suma(x,y):
    return print(f"----------> Suma: {x} + {y} -> {x + y} ") 
def resta(x,y):
    return print(f"----------> Resta: {x} - {y} -> {x - y} ")
def multiplica(x,y):
    return print(f"----------> Multiplica: {x} * {y} -> {x * y} ")
def divide(x,y):
    return print(f"----------> Divide: {x} / {y} -> {x / y} ") if y!=0 else print("Error, División entre cero") 
def divideEntera(x,y):
    return print(f"----------> Divide Exacta: {x} // {y} -> {x // y} ") if y!=0 else print("Error, División entre cero") 
def modulo(x,y):
    return print(f"----------> Residuo: {x} % {y} -> {x % y} ") if y!=0 else print("Error, División entre cero") 
def exponente(x,y):
    return print(f"----------> Potencia: {x} ** {y} -> {x ** y} ")
def igual(x,y):
    return print(f"----------> Igual: {x} == {y} -> {x == y} ") 
def diferente(x,y):
    return print(f"----------> Diferente: {x} != {y} -> {x != y} ") 
def mayorQue(x,y):
    return print(f"----------> Mayor que: {x} > {y} -> {x > y} ") 
def menorQue(x,y):
    return print(f"----------> Menor que: {x} < {y} -> {x < y} ") 
def mayorIgual(x,y):
    return print(f"----------> Mayor igual: {x} >= {y} -> {x >= y} ") 
def menorIgual(x,y):
    return print(f"----------> Menor igual: {x} <= {y} -> {x <= y} ") 
def yLogico(x,y):
    return print(f"----------> Y: {x}>0 y {y}>0 -> {x>0 and y>0} ") 
def oLogico(x,y):
    return print(f"----------> O: {x}>0 o {y}>0 -> {x>0 or y>0} ") 
def noLogico(x,y):
    return print(f"----------> No({x}>0) -> {not(x>0)} ") 
def asigna(x,y):
    a=x
    x=y
    return print(f"----------> Asigna: {a} = {y} -> {x} ") 
def sAsigna(x,y):
    a=x
    x+=y
    return print(f"----------> Suma y Asigna: {a} += {y} -> {x} ") 
def rAsigna(x,y):
    a=x
    x-=y
    return print(f"----------> Resta y Asigna: {a} -= {y} -> {x} ") 
def mAsigna(x,y):
    a=x
    x*=y
    return print(f"----------> Multiplica y Asigna: {a} *= {y} -> {x} ") 
def dAsigna(x,y):
    a=x
    x/=y
    return print(f"----------> Divide y Asigna: {a} /= {y} -> {x} ") if y!=0 else print("Error, División entre cero") 
def deAsigna(x,y):
    a=x
    x//=y
    return print(f"----------> Divide Exacta y Asigna: {a} //= {y} -> {x} ") if y!=0 else print("Error, División entre cero") 
def modAsigna(x,y):
    a=x
    x%=y
    return print(f"----------> Residuo y Asignación: {a} %= {y} -> {x} ") if y!=0 else print("Error, División entre cero") 
def expAsigna(x,y):
    a=x
    x**=y
    return print(f"----------> Exponente y Asigna: {a} **= {y} -> {x} ") 
def yBit(x,y):
    return print(f"----------> y bits: {x} & {y} -> {x & y} ") 
def oBit(x,y):
    return print(f"----------> y bits: {x} | {y} -> {x | y} ") 
def xoBit(x,y):
    return print(f"----------> y bits: {x} ^ {y} -> {x ^ y} ") 
def noBit(x,y):
    return print(f"----------> y bits: ~ {x} -> {~x} ") 
def diBit(x,y):
    return print(f"----------> y bits: {x} << {y} -> {x << y} ") 
def ddBit(x,y):
    return print(f"----------> y bits: {x} >> {y} -> {x >> y} ") 
######################################################################################
#Inicio de ejecución del programa
inicio()
menuPrincipal()