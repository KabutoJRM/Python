# Uso de cadenas o strings en Python

my_string= "Mi string"
my_other_string= "Mi otro string"

print (len (my_string))
print (len (my_other_string))

print (my_string+" "+my_other_string)

my_new_string= "Esto es un string\ncon salto de linea"
print (my_new_string)

my_tab_string= "\tEsto es un string con tabulación"
print (my_tab_string)

# Formateo

name, surname, age= "José", "Marcano", 51

print ("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print ("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print (f"Mi nombre es {name} {surname} y mi edad es {age}") # la forma más recomendada de formatear texto

# desempaquetado de caracteres

string_des = "python"
a, b, c, d, e, f = string_des

print (a)
print (f)
division_string = string_des [1:3]
print (division_string)

division_string = string_des [1:]
print (division_string)

# reversed

reversed_string = string_des [::-1]
print (reversed_string)

# Funciones del sistema para string 

print (string_des.capitalize())
print (string_des.upper())
print (string_des.count("t"))
print (string_des.isnumeric())
print (string_des.lower())
print (string_des.upper().isupper())