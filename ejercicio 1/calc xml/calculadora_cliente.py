import xmlrpc.client
cliente = xmlrpc.client.ServerProxy("http://localhost:8000/")
operaciones = {
    "1": ("Suma",           "sumar"),
    "2": ("Resta",          "restar"),
    "3": ("Multiplicación", "multiplicar"),
    "4": ("División",       "dividir"),
}
print("     CALCULADORA (XML-RPC)")

while True:
    print("\nSeleccione una operación:")
    for clave, (nombre, _) in operaciones.items():
        print(f"  {clave}. {nombre}")
    print("  5. Salir")

    opcion = input("\nOpción: ").strip()

    if opcion == "5":
        print("Gracias por usar calculadora xml.")
        break

    if opcion not in operaciones:
        print("Opción no válida. Intente de nuevo.")
        continue

    nombre_op, nombre_func = operaciones[opcion]

    try:
        a = float(input(f"Ingrese el primer número:  "))
        b = float(input(f"Ingrese el segundo número: "))
    except ValueError:
        print("Error: ingrese números válidos.")
        continue

    metodo = getattr(cliente, nombre_func)
    resultado = metodo(a, b)

    print(f"\nResultado de {nombre_op}({a}, {b}) = {resultado}")
