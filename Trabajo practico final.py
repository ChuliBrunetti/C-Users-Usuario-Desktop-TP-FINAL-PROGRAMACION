
cancion1 = {"titulo": "Somebody Like You", "cantante": "Keith Urban", "Letra": "Theres a new wind blowinlike Ive never known Im breathing deeper than Ive ever done And it sure feels good To finally feel the way I do.. "}
cancion2 = {"titulo": "Tennessee Whiskey", "cantante": "Chris Stapleton", "Letra": "Used to spend my nights out in a barroom Liquor was the only love Ive know But you rescued me from reachin for the bottom And brought me back from being too far gone..." }
cancion3 = {"titulo": "Before He Cheats", "cantante": "Carrie Underwwod", "Letra": "Right now hes problably slow dancin With a bleacheblond tramp and shes probably gettin frisky..."}
cancion4 = {"titulo": "Colder Weather", "cantante": "Zac Brown Band", "Letra": "Shes trade Colorado if hed take her with him Closes the door before the winter lets the cold in And wonders if her love is strong enough to make him stay..."}
cancion5 = {"titulo": "Alright", "cantante": "Darius Rcker", "Letra": "Alright alright Yeah its alright alright dont need no five star reservations Igot spaghetti and a cheaper bottle of wine..."}

listaCanciones = [cancion1, cancion2, cancion3, cancion4, cancion5]

def textoMenu():
    print("Para Agregar una cancion, 1")
    print("Para Buscar una cancion, 2")
    print("Para Modificar una cancion, 3")
    print("Para Salir del menu, 4")
    elecUser = int(input())
    if elecUser == 1:
        agregarCancion(listaCanciones)
    elif elecUser == 2:
        buscarCancion(listaCanciones)
    elif elecUser == 3:
        modificarCancion(listaCanciones)
    else:
        print("Slir del menu")
textoMenu()

elecUser = textoMenu()

def agregarCancion(listaCanciones):
    nuevaCancion = input("Ingresar letra")
    listaCanciones.append(nuevaCancion)
    print(listaCanciones)


def buscarCancion(listaCanciones):
    cancionBuscar = input("Buscar nueva cancion")

    def imprimircancion (cancion):
        print("El nombre es: ", cancion ["titulo"])
        print("artista es: ", cancion ["cantante"])
        print("cancion es:", cancion ["Letra"])

    for cancion in listaCanciones:
        if cancion ["titulo"] == buscarCancion:
            imprimircancion (cancion)
            return
        print ("no se encontro")

def modificarCancion(listaCanciones):
    tituloBuscado = input ("Ingrese el titulo a modificar")
    encontradoen = -1 
    for i in range(len(listaCanciones)):
        if(listaCanciones[i]["Titulo"] == tituloBuscado):
            encontradoen = i

    if encontradoen != -1:
        nuevoNombre = input("Ingrese el nuevo nombre")
        listaCanciones[encontradoen]["Titulo"] == nuevoNombre
        print ("El titulo nuevo es:", listaCanciones)
    else:
        print("No exite el titulo")
        

    

    




