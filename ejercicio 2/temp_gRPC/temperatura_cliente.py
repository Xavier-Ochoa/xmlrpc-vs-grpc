import grpc
import temperatura_pb2
import temperatura_pb2_grpc

canal = grpc.insecure_channel("localhost:5001")
stub = temperatura_pb2_grpc.TemperaturaStub(canal)

conversiones = {
    "1": ("Celsius  → Fahrenheit", "°C", "°F"),
    "2": ("Fahrenheit → Celsius",  "°F", "°C"),
}

print("  CONVERSOR DE TEMPERATURAS (gRPC)")

while True:
    print("\nSeleccione el tipo de conversión:")
    for clave, (nombre, _, _u) in conversiones.items():
        print(f"  {clave}. {nombre}")
    print("  3. Salir")

    opcion = input("\nOpción: ").strip()

    if opcion == "3":
        print("¡Hasta luego!")
        break

    if opcion not in conversiones:
        print("Opción no válida. Intente de nuevo.")
        continue

    nombre_conv, unidad_in, unidad_out = conversiones[opcion]

    try:
        valor = float(input(f"Ingrese la temperatura en {unidad_in}: "))
    except ValueError:
        print("Error: ingrese un número válido.")
        continue

    entrada = temperatura_pb2.TempEntrada(valor=valor)

    if opcion == "1":
        res = stub.CelsiusAFahrenheit(entrada)
    else:
        res = stub.FahrenheitACelsius(entrada)

    print(f"\n{valor}{unidad_in}  =  {res.resultado:.2f}{unidad_out}")
