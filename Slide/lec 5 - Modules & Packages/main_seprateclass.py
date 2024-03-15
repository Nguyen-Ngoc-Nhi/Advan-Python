#import president_seprateclass
#macron = president_seprateclass.President("Macron", 48, "2020 - 2035")
#print(f"Macron term is {macron._get_term()}")

from president_seprateclass import *
macron = President("Macron", 48, "2020 - 2035")
print(f"Macron term is {macron._get_term()}")
#macron.print()