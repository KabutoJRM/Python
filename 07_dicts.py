# Uso de diccionarios en Python

my_dict = dict ()
my_other_dict= {}

print (type(my_dict))
print (type(my_other_dict))

my_other_dict = {"Nombre": "Koji", 
                 "Apellido": "Kabuto",
                "Edad": 51}

print (my_other_dict)

print (my_other_dict["Edad"])
my_other_dict ["Edad"] = 52
print (my_other_dict["Edad"])

my_other_dict ["Estatura"] = 1.76
print (my_other_dict)

del my_other_dict ["Estatura"]
print (my_other_dict)

print (my_other_dict.items())
print (my_other_dict.keys())
print (my_other_dict.values())