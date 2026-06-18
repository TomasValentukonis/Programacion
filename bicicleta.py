from data_storage import *

def cargar_bicicleta(codigos, modelos, estaciones, kilometros_recorridos, estados):
    estaciones_totales = ["Caballito", "Palermo", "Belgrano", "Almagro", "Boedo"]
    estados_totales = ["Disponible", "En uso", "Mantenimiento"]
    modelos_totales = ["Urbana", "Mountain Bike", "Electrica", "Plegable",]
    while True:
        nuevo_codigo = input("Ingrese el codigo de la bicicleta: ")
        if nuevo_codigo.isdigit() and len(nuevo_codigo) == 4:
            codigos.append(nuevo_codigo)
            break
        print("Error... ingrese un codigo de 4 numeros")
    while True:
        nuevo_modelo = input(f"Ingrese el modelo {modelos_totales}: ")
        if nuevo_modelo in modelos:
            modelos.append(nuevo_modelo)
            break
        print("Error... Ingrese un nombre valido(Atencion a las mayusculas)")
    while True:
        nueva_estacion = input(f"Ingrese la estacion {estaciones_totales}: ")
        if nueva_estacion in estaciones:
            estaciones.append(nueva_estacion)
            break
        print("Error... Ingrese una estacion valida(Atencion a las mayusculas)")
    while True:
        km_check = input("Ingrese los kilómetros recorridos: ")
        if km_check.replace('.', '', 1).isdigit():
            nuevos_km = float(km_check)
            if nuevos_km >= 0 and nuevos_km < 10000:
                kilometros_recorridos.append(nuevos_km)
                break
            else:
                print("Error... Ingrese un numero valido")
        else:
            print("Error... Ingrese un numero valido")
    while True:
        nuevo_estado = input(f"Ingrese el estado {estados_totales}: ")
        if nuevo_estado in estados:
            estados.append(nuevo_estado)
            break
        print("Error... Ingrese un estado valido(Atencion a las mayusculas)")
    print("Bicicleta cargada con exito")
    input("Presione enter para volver al menu...")

def mostrar_bicicletas(codigos, modelos, estaciones, kilometros_recorridos, estados):
    for i in range(len(codigos)):
        print("-" * 30)
        print(f"Codigo: {codigos[i]}")
        print(f"Modelo: {modelos[i]}")
        print(f"Estacion: {estaciones[i]}")
        print(f"Kilometros Recorridos: {kilometros_recorridos[i]}")
        print(f"Estado: {estados[i]}")
    input("Presione enter para volver al menu...")

def buscar_maximo_km_bicicleta_disponible(codigos, modelos, kilometros_recorridos, estados):
    km_maximo = -1
    for i in range(len(estados)):
        if estados[i] == "Disponible":
            if kilometros_recorridos[i] > km_maximo:
                km_maximo = kilometros_recorridos[i]
    print("-" * 30)
    print("La/las bicicleta/s con mayor km: ")
    for i in range(len(estados)):
        if estados[i] == "Disponible" and kilometros_recorridos[i] == km_maximo:
            print("-" * 30)
            print(f"Modelo: {modelos[i]}")
            print(f"Codigo: {codigos[i]}")
            print(f"Kilometros: {kilometros_recorridos[i]}")
    input("Presione enter para volver al menu...")

def ordenar_bicicletas_por_km(codigos, modelos, estaciones, kilometros_recorridos, estados):
    for j in range(len(kilometros_recorridos)):
        posicion_maxima = j
        for i in range(j, len(kilometros_recorridos)):
            if kilometros_recorridos[i] > kilometros_recorridos[posicion_maxima]:
                posicion_maxima = i
        kilometros_recorridos[j], kilometros_recorridos[posicion_maxima] = kilometros_recorridos[posicion_maxima], kilometros_recorridos[j]
        codigos[j], codigos[posicion_maxima] = codigos[posicion_maxima], codigos[j]
        modelos[j], modelos[posicion_maxima] = modelos[posicion_maxima], modelos[j]
        estaciones[j], estaciones[posicion_maxima] = estaciones[posicion_maxima], estaciones[j]
        estados[j], estados[posicion_maxima] = estados[posicion_maxima], estados[j]
    print("Las bicicletas ordenadas por km: ")
    for k in range(len(kilometros_recorridos)):
        print("-" * 30)
        print(f"Modelo: {modelos[k]}")
        print(f"Codigo: {codigos[k]}")
        print(f"Kilometros: {kilometros_recorridos[k]}")
        print(f"Estado: {estados[k]}")
        print(f"Estacion: {estaciones[k]}")
    input("Presione enter para volver al menu...")

def calcular_cantidad_por_estacion(codigos, estaciones):
    bicis_caballito = 0
    bicis_almagro = 0
    bicis_boedo = 0
    bicis_palermo = 0
    bicis_belgrano = 0
    for i in range(len(codigos)):
        if estaciones[i] == "Caballito":
            bicis_caballito += 1
        elif estaciones[i] == "Almagro":
            bicis_almagro += 1
        elif estaciones[i] == "Boedo":
            bicis_boedo += 1
        elif estaciones[i] == "Palermo":
            bicis_palermo += 1
        elif estaciones[i] == "Belgrano":
            bicis_belgrano += 1
    print("-" * 30)
    print("Cantidad de bicicletas por estacion: ")
    print(f"En Almagro hay un total de {bicis_almagro} bicicleta/s")
    print(f"En Boedo hay un total de {bicis_boedo} bicicleta/s")
    print(f"En Palermo hay un total de {bicis_palermo} bicicleta/s")
    print(f"En Belgrano hay un total de {bicis_belgrano} bicicleta/s")
    print(f"En Caballito hay un total de {bicis_caballito} bicicleta/s")
    input("Presione enter para volver al menu...")

def calcular_promedio_km_por_estacion(estaciones, kilometros_recorridos):
    cantidad_caballito = 0
    caballito_suma = 0
    cantidad_almagro = 0
    almagro_suma = 0
    cantidad_boedo = 0
    boedo_suma = 0
    cantidad_palermo = 0
    palermo_suma = 0
    cantidad_belgrano = 0
    belgrano_suma = 0
    for i in range(len(kilometros_recorridos)):
        if estaciones[i] == "Caballito":
            cantidad_caballito += 1
            caballito_suma += kilometros_recorridos[i]
        elif estaciones[i] == "Almagro":
            cantidad_almagro += 1
            almagro_suma += kilometros_recorridos[i]
        elif estaciones[i] == "Boedo":
            cantidad_boedo += 1
            boedo_suma += kilometros_recorridos[i]
        elif estaciones[i] == "Palermo":
            cantidad_palermo += 1
            palermo_suma += kilometros_recorridos[i]
        elif estaciones[i] == "Belgrano":
            cantidad_belgrano += 1
            belgrano_suma += kilometros_recorridos[i]
    print("-" * 30)
    print("Promedio de Km por estacion: ")
    print(f"El promedio de Km en Caballito es: {caballito_suma / cantidad_caballito}")
    print(f"El promedio de Km en Boedo es: {boedo_suma / cantidad_boedo}")
    print(f"El promedio de Km en Belgrano es: {belgrano_suma / cantidad_belgrano}")
    print(f"El promedio de Km en Almagro es: {almagro_suma / cantidad_almagro}")
    print(f"El promedio de Km en Palermo es: {palermo_suma / cantidad_palermo}")
    input("Presione enter para volver al menu...")
