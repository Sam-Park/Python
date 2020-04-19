def remove_duplicates(lista):
    lista2 = []
    if lista:
        for item in lista:
            if item not in lista2:
                lista2.append(item)
    else:
        return lista
    return lista2

print(remove_duplicates([1,1,1,2,2,3,3,]))