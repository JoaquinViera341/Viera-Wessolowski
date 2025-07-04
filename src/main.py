import pickle # libreria de archivos
from INCUCAI.INCUCAI import INCUCAI
from datetime import date
try :
    with open("incucai.pkl", "rb") as f :
        incucai = pickle.load(f)
except (FileNotFoundError, EOFError):
    incucai = INCUCAI([], [], [])
hoy = date.today()
while True :
    print("Bienvenido al sistema INCUCAI:")
    print("1. Acceder a centros de salud")
    print("2. Acceder a donantes")
    print("3. Acceder a receptores")
    print("\n")
    opcion = input("Seleccione una opción: ")
    print("\n")
    if opcion == "1":
        incucai.menu_centros_salud()
    elif opcion == "2":
        incucai.menu_donantes()
    elif opcion == "3":
        incucai.menu_receptores()
    else:
        print("Opción no valida, por favor intente de nuevo.")
    hoy = incucai.revision_fecha(hoy)
    with open("incucai.pkl", "wb") as f:
            pickle.dump(incucai, f)