cats = ["short hair", "maine coon", "orange", "siamese", "russian"]

print('Print testing')
x = cats[0]
y = cats[0:3]
y2 = cats[0:3:1]
y3 = cats[0:3:2]
z = cats[4]
print(x)
print(y)
print(y2)
print(y3)
print(z)

###########################
print("\nChange element")
cats[0] = "mybabi"
cats[4] = "daddy"
print(cats)

###########################
print('\nnumber of elements')
a = len(cats)
print(a)

###########################
print("\nPrint each element")
for _ in cats:
    print(_)

###########################
print("\nAdding elements 1st way")
cats.append("syph")
print(cats)

print("\nAdding elements 2nd way, with specific position")
cats.insert(0, "meowmeow")
print(cats)

print("\nMerge elements")
dogs = ["corgi", "golden", "wurfwurf"]
cats.extend(dogs)
print(cats)

print("\nMerge elements w/ tuple")
human = ("male", "female", "nomale")
dogs.extend(human)
print(dogs)

###########################
print('\nRemove elements')
cats.pop(1)
print(cats)

cats.remove("daddy")
print(cats)

print('\nDelete all elemets')
cats.clear()
print(cats)

print('\nCount a value') 
b = dogs.count('corgi')
print(b)

print("\nReverse array")
dogs.reverse()
print(dogs)
