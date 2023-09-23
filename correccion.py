def mostrar_mensaje(mensaje):
    #comilla
    print("***************")
    # corchete
    print(mensaje)
    # es print
    print("*****************")

#definir carga suma
#la llave no va a aqui
def carga_suma():
    valor1 = int(input("ingrese el primer valor:"))
    valor2 = int(input("ingrese el segundo valor:"))
    suma = valor1 + valor2
    

    #la coma
    print("la suma de los valores es:", suma)
# //programa principal

mostrar_mensaje("el programa calcula la suma de dos valores ingresados por el teclado.")
#falta el guion bajo
carga_suma()

# mostrar_mensaje es el que no esta para nada