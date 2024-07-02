import json
from datetime import datetime

# Lista para almacenar las ventas
ventas = []

# Función para obtener tipo de cliente y aplicar descuento
def obtener_descuento(tipo_cliente):
    if tipo_cliente == "Regular":
        return 0.10
    elif tipo_cliente == "Premium":
        return 0.15
    else:
        return 0.0
# Tabla de precios
precios = {
    "Billy Ocean": {"soul": 5000 },
    "ABC": {"new romantic": 6000 },
    "Laura Branigan": {"pop": 5200 },
    "King": {"pop": 5700 },
    "Black": {"soft rock": 6100 },
    "Savage": {"disco": 6300 },
    "Johnny Hates Jazz": {"pop": 4900 },
    "Stacey Q": {"pop": 5700 },
    "Murray Head": {"new wave": 6300 },
    "Baltimora": {"new wave": 6200 },
}




# Función para mostrar el menú
def menu_vinilos():
    print("\n===== Menú de opciones =====")
    print("(1) Registrar una venta")
    print("(2) Mostrar todas las ventas")
    print("(3) Buscar ventas por cliente")
    print("(4) Guardar las ventas en un archivo")
    print("(5) Cargar las ventas desde un archivo")
    print("(6) Generar boleta")
    print("(7) Salir del programa")
    opcion = input("Seleccione una opción (1-7): ")
    return opcion


def registrar_venta():
    cliente  = input("Nombre del cliente: ")
    tipo_cliente = input("Tipo de cliente (Regular/Premium/): ").lower()
    artista = input("nombre del artista: ").lower()
    genM = input("Genero musica: ").lower()
    cantidad = int(input("Cantidad de vinilos: "))

  

    if artista in precios and genM in precios[tipo_cliente]:
        precio_unitario = precios[artista][genM]
        total = precio_unitario * cantidad

       

        venta = {
            "cliente": cliente,
            "tipo_cliente": tipo_cliente,
            "artista": artista,
             "genM": genM,
            "cantidad": cantidad,
            "total": total,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        ventas.append(venta)
        print("Venta registrada exitosamente.")
    else:
        print("artista o genero invalido.")

# Función para mostrar todas las ventas
def mostrar_ventas():
    if ventas:
        for venta in ventas:
            print(f"Cliente: {venta['cliente']}, Tipo Cliente: {venta['tipo_cliente']}, artista: {venta['artista']}, genM {venta['genM']}, Cantidad: {venta['cantidad']},  Total: ${venta['total']}, Fecha: {venta['fecha']}")
    else:
        print("No hay ventas registradas.")

# Función para buscar ventas por cliente
def buscar_ventas_por_cliente():
    cliente = input("Ingrese el nombre del cliente para buscar las ventas: ").lower()
    encontradas = [venta for venta in ventas if venta['cliente'].lower() == cliente]
    if encontradas:
        for venta in encontradas:
            print(f"Cliente: {venta['cliente']}, Tipo Cliente: {venta['tipo_cliente']}, artista: {venta['artista']}, genM {venta['genM']}, Cantidad: {venta['cantidad']},  Total: ${venta['total']}, Fecha: {venta['fecha']}")
    else:
        print(f"No se encontraron ventas para el cliente '{cliente}'.")

# Función para guardar las ventas en un archivo JSON
def guardar_ventas():
    with open('ventas.json', 'w') as archivo:
        json.dump(ventas, archivo)
    print("Ventas guardadas en el archivo 'ventas.json'.")

# Función para cargar las ventas desde un archivo JSON
def cargar_ventas():
    global ventas
    try:
        with open('ventas.json', 'r') as archivo:
            ventas = json.load(archivo)
        print("Ventas cargadas desde el archivo 'ventas.json'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.json'. No hay ventas cargadas.")

# Función para generar una boleta
def generar_boleta():
    cliente = input("Ingrese el nombre del cliente para generar la boleta: ").lower()
    boleta = f"=================== Boleta de Venta ===================\n"
    boleta += f"Cliente: {cliente}\n"
    boleta += f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    boleta += f"{'artista':<15} {'genero musica':<10} {'Cantidad':<10}  {'Total ($)'}\n"
    boleta += f"--------------------------------------------------------\n"

    encontradas = [venta for venta in ventas if venta['cliente'].lower() == cliente]
    if encontradas:
        total_general = 0
        for venta in encontradas:
            boleta += f"{venta['artista']:<15} {venta['genero_musical']:<10} {venta['cantidad']:<10}  {venta['total']:>10.2f}\n"
            total_general += venta['total']
        boleta += f"--------------------------------------------------------\n"
        boleta += f"{'Total a pagar:':<50} {total_general:>10.2f}\n"
        boleta += f"========================================================\n"
    else:
        boleta += f"No se encontraron ventas para el cliente '{cliente}'.\n"

    print(boleta)

# Función principal para ejecutar el programa
def main():
    while True:
        opcion = menu_vinilos()

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_ventas()
        elif opcion == "3":
            buscar_ventas_por_cliente()
        elif opcion == "4":
            guardar_ventas()
        elif opcion == "5":
            cargar_ventas()
        elif opcion == "6":
            generar_boleta()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()