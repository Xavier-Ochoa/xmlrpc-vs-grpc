import xmlrpc.client

cliente = xmlrpc.client.ServerProxy("http://localhost:8001/")

conversiones = {
    "1": ("Celsius  → Fahrenheit", "celsius_a_fahrenheit", "°C", "°F"),
    "2": ("Fahrenheit → Celsius",  "fahrenheit_a_celsius",  "°F", "°C"),
}

print("   CONVERSOR DE TEMPERATURAS (XML-RPC)")

while True:
    print("\nSeleccione el tipo de conversión:")
    for clave, (nombre, _, unidad_in, _u) in conversiones.items():
        print(f"  {clave}. {nombre}")
    print("  3. Salir")

    opcion = input("\nOpción: ").strip()

    if opcion == "3":
        print("¡Hasta luego!")
        break

    if opcion not in conversiones:
        print("Opción no válida. Intente de nuevo.")
        continue

    nombre_conv, nombre_func, unidad_in, unidad_out = conversiones[opcion]

    try:
        temp = float(input(f"Ingrese la temperatura en {unidad_in}: "))
    except ValueError:
        print("Error: ingrese un número válido.")
        continue

    metodo = getattr(cliente, nombre_func)
    resultado = metodo(temp)

    print(f"\n{temp}{unidad_in}  =  {resultado:.2f}{unidad_out}")
