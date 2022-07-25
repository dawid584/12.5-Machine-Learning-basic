#łączenie zbiorów

shopping_A = {"pieczywo", "masło", "ser"}
shopping_B = {"wędlina", "masło", "cytryna"}

xc = shopping_A.union(shopping_B)

print(xc)

xd = shopping_A | shopping_B
print(xd)

# częśc wspólna
xv = shopping_A & shopping_B
print(xv)

# iloczyn zbioróWarning
xb =  shopping_A - shopping_B

print(xb)


dictionary = {"key_1" : ["azjatka" , "robot"], 123 : ["lizak" , "cukierek"]}
print(dictionary)

print(dictionary.keys())
print(dictionary.values())
print(dictionary[123])
print(dictionary.get("key_1"))
