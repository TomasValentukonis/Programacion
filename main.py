from data_storage import *
from bicicleta import *

def main():
    lista_opciones = [
        "Cargar bicicleta",
        "Mostrar todos los datos de las bicicletas",
        "De las bicicletas disponibles, cuál es/son las que tienen mas cantidad de km recorridos (mostrar codigo y modelo)", 
        "Ordenar bicicletas por km recorridos",
        "Contar cantidad de bicicletas por estaciones",
        "Calcular promedio de km recorridos entre todas las bicicletas por estación",
        "Salir"
    ]

    estaciones_activas = [
    "Caballito", "Palermo", "Belgrano", "Almagro","Boedo",
    ]

    estados_activos = [
    "Disponible",
    "En uso",
    "Mantenimiento"
    ]

    while True:
        print("------ Menu de opciones ------")
        for i in range(len(lista_opciones)):
            print(f"{i+1}. {lista_opciones[i]}")
        opcion = input("Seleccionar opcion (1-7): ")
        if opcion == "1":
            cargar_bicicleta(codigos, modelos, estaciones, kilometros_recorridos, estados)
        elif opcion == "2":
            mostrar_bicicletas(codigos, modelos, estaciones, kilometros_recorridos, estados)
        elif opcion == "3":
            buscar_maximo_km_bicicleta_disponible(codigos, modelos, kilometros_recorridos, estados)
        elif opcion == "4":
            ordenar_bicicletas_por_km(codigos, modelos, estaciones, kilometros_recorridos, estados)
        elif opcion == "5":
            calcular_cantidad_por_estacion(codigos, estaciones)
        elif opcion == "6":
            calcular_promedio_km_por_estacion(estaciones, kilometros_recorridos)
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Error.. ingrese un numero valido(1-7): ")
            input("Presione enter para volver al menu...")


if __name__ == "__main__":
    main()