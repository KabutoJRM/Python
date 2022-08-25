# Uso de sets en Python

my_set = set()
my_other_set = {}

print (type(my_set))
print (type(my_other_set))

my_other_set = {"Koji", "Kabuto", 51}
print (type(my_other_set))

print (len(my_other_set))

my_other_set.add ("Mediatech")
print (my_other_set) # un set no es ordenado

my_other_set.add ("Mediatech")
print (my_other_set) # un set no admite duplicados

print ("Koji" in my_other_set)
print ("Koje" in my_other_set)

my_other_set.remove ("Mediatech")
print (my_other_set)

my_other_set.clear()
print (len (my_other_set))

my_set = {"Pilder", "Boss", "Afrodita"}
my_other_set = {"Koji", "Kabuto", 51}

my_new_set = my_set.union (my_other_set)
print (my_new_set)

print("hola")