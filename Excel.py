import re

Medio, Bacteria = {}, {}

with open('MatrizTranspuesta.csv', 'r') as file:
    for line in file:
        line = re.sub(',',', ', line)
        match = re.findall(r'\,([^\n|\r|\,]+)', line)
        if match:
		Medio[match[0]] = match[4:]
		Bacteria[match[2]] = match[4:]
print(Medio)
print(Bacteria)
