lista1 = ["a","b","c","d","e"]
lista2 = ["c","e","f","t","g"]
listaTodo = []
lSolo1 = []
lSolo2 = []
lAmbas = []
listaTodo = lista1+lista2
for palabra in lista1:
    if palabra in lista2:
        lAmbas = lAmbas + [palabra]
    else:
        lSolo1 = lSolo1 + [palabra]
for palabra in lista2:
    if palabra not in lista1:
        lSolo2 = lSolo2 + [palabra]
print("Lista 1:",lista1)
print("Lista 2:",lista2)
print("Palabras de las 2 listas:",listaTodo)
print("Palabras que aparecen en la 1er lista y no en la 2da:",lSolo1)
print("Palabras que aparecen en la 2da lista y no en la 1era:",lSolo2)
print("Palabras que aparecen en ambas listas:",lAmbas)