# Uso de listas en Python

from turtle import clear


my_list = list()
my_other_list = []

print (len(my_list))

my_list = [35, 24, 51, 62, 18, 35]

print (my_list)
print (len(my_list))

my_other_list = [51, 1.76, "Koji", "Kabuto"]

print (type (my_other_list))
print (type (my_list))

print (my_other_list [0])
print (my_other_list [1])
print (my_other_list [-1])
print (my_other_list [-3])

print (my_other_list.count("Koji"))
print (my_other_list.count(30))

age, height, name, surname = my_other_list

print (surname)
print (age)

print (my_list+my_other_list)

my_other_list.append ("Mediatech Game Studio")
print (my_other_list)

my_other_list.insert (1,"Azul")
print (my_other_list)

my_other_list.remove ("Azul")
print (my_other_list)

my_other_list.pop ()
print (my_other_list)

del my_list[2]
print (my_list)

my_new_list = my_list.copy()

my_list.clear()
print (my_list)
print (my_new_list)

my_new_list.reverse()
print (my_new_list)

my_new_list.sort()
print (my_new_list)

print (my_new_list[1:3])

my_other_list[2] = "Kenzo"
print (my_other_list)