# Uso de variables en Python
mi_variable="Hola"
mi_entero=5
mi_booleana=True

print (mi_variable)

print (type (mi_variable))

# Concatenación de variables en un print

print (mi_variable,"es un string que puedo concatenar con una variable entera ", mi_entero, " y también con una booleana ", mi_booleana)

# Funciones del lenguaje

print (len(mi_variable))

# Variables en una sola línea

name, surname, alias, age= "José", "Marcano", "Kabuto", 51

print ("Mi nombre es",name,"mi apellido es",surname,"y todos me dicen",alias,"con mis",age, "añitos" )

# Input con variables

first_name=input ("¿cuál es tu nombre:")
print ("Tú nombre es:", first_name)

test=mi_entero+mi_entero
print (test)