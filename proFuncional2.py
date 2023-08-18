# Escribir una funcion que reciba un diccionario con las asignaturas 
# y las notas de un alumno y devuelva otro diccionario con las asignaturas
# en mayuscula y las calificaciones correspondientes a las notas aprobadas

# sorter : va a ser el clasificador que aplicara a cada uno de los elementos de mi lista notes
# map es un objeto

subjects = {"Math":4, "Biology":6, "Physics":10, "History":8, "Chemistry":7}

def sorter(note):
    if note <=5:
        return "Reprobate"
    elif note <=7:
        return "Approved"
    elif note <=9:
        return "Outstanding"
    elif note ==10:
        return "Excellent"
    else: 
        return "ERROR"

def main(dictionary):
    kys =map(str.upper, dictionary.keys())
    valu =map(sorter, dictionary.values())
    result = dict(zip(kys, valu))
    for ky, val in dictionary.items():
        if val <=5:
            del(result[ky.upper()])
    return result

print("\nYou will be shown a list with your subjects and your grade \n")
print(subjects)
print("\nThe subjects that YES have been APPROVED will be shown \n")
print(main(subjects))
