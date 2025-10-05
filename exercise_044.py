# Crea una función que calcule y retorne cuántos días hay entre dos cadenas
# de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha correcta se
#   lanzará una excepción.
# - No se pueden usar funciones del propio lenguaje o librerias que lo hagan directamente
# - No importa el bisiesto y un mes tiene 30 dias.

def calculate_dates(date_01,date_02):
    #Comprobation 01
    if "/" not in date_01 or "/" not in date_02:
        raise ValueError("Error. Faltan '/'") ; return 
    if date_01.count("/") != 2 or date_02.count("/") != 2:
        raise ValueError("Error. Faltan '/'") ; return

    #Make lists of dates
    list_date_01 = str(date_01).split("/")
    list_date_02 = str(date_02).split("/")

    #Comprobation 02
    if len(list_date_01[0]) != 2 or len(list_date_02[0]) != 2:
        raise ValueError("Error. Verifique los dias.") ; return
    if len(list_date_01[1]) != 2 or len(list_date_02[1]) != 2:
        raise ValueError("Error. Verifique los meses.") ; return
    if len(list_date_01[2]) != 4 or len(list_date_02[2]) != 4:
        raise ValueError("Error. Verifique los años") ; return
    
    #Comprobation 03
    if int(list_date_01[0]) > 30 or int(list_date_02[0]) > 30:
        raise ValueError("Error. Verifique los dias.") ; return
    if int(list_date_01[1]) > 12 or int(list_date_02[1]) > 12:
        raise ValueError("Error. Verifique los meses.") ; return

    # calculate the difference
    total_days_01 = (int(list_date_01[0])) + (int(list_date_01[1])*30) + (int(list_date_01[2])*365)
    total_days_02 = (int(list_date_02[0])) + (int(list_date_02[1])*30) + (int(list_date_02[2])*365)

    return abs(total_days_01 - total_days_02)

user_str_01 = "03/01/2020"
user_str_02 = "05/02/2025"

print(f"De las fechas {user_str_01} y {user_str_02}. La diferencia es de: {calculate_dates(user_str_01,user_str_02)} dias.")

#59:29 minutos