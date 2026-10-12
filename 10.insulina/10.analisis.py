import re

# Leer archivo original

with open("preproinsulin-seq.txt", "r") as file:

    sequence = file.read()

print("Contenido original:")
print(sequence)

print("Cantidad de caracteres originales:", len(sequence))


# Limpiar la secuencia

sequence = re.sub(r"ORIGIN|//|\d+|\s+", "", sequence)

print("Secuencia limpia:")
print(sequence)

print("Cantidad de caracteres después de limpiar:", len(sequence))


# Generar archivo con la secuencia completa

with open("preproinsulin-seq-clean.txt", "w") as file:

    file.write(sequence)


# Generar archivos de cada sección

files = {
    "lsinsulin-seq-clean.txt": sequence[0:24],
    "binsulin-seq-clean.txt": sequence[24:54],
    "cinsulin-seq-clean.txt": sequence[54:89],
    "ainsulin-seq-clean.txt": sequence[89:110]
}


# Crear archivos

for filename, part in files.items():

    with open(filename, "w") as file:

        file.write(part)

    print(filename + ": " + str(len(part)) + " caracteres")