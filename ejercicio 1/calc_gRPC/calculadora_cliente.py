import grpc
import calculadora_pb2
import calculadora_pb2_grpc

canal = grpc.insecure_channel("localhost:5000")
stub = calculadora_pb2_grpc.CalculadoraStub(canal)

operaciones = {
    "1": "Suma",
    "2": "Resta",
    "3": "Multiplicación",
    "4": "División",
}
print("    CALCULADORA REMOTA (gRPC)")
while True:
    print("\nSeleccione una operación:")
    for clave, nombre in operaciones.items():
        print(f"  {clave}. {nombre}")
    print("  5. Salir")

    opcion = input("\nOpción: ").strip()

    if opcion == "5":
        print("¡Hasta luego!")
        break

    if opcion not in operaciones:
        print("Opción no válida. Intente de nuevo.")
        continue

    try:
        a = float(input("Ingrese el primer número:  "))
        b = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: ingrese números válidos.")
        continue

    op = calculadora_pb2.Operacion(a=a, b=b)

    if opcion == "1":
        res = stub.Sumar(op)
        print(f"\nResultado de Suma({a}, {b}) = {res.r}")
    elif opcion == "2":
        res = stub.Restar(op)
        print(f"\nResultado de Resta({a}, {b}) = {res.r}")
    elif opcion == "3":
        res = stub.Multiplicar(op)
        print(f"\nResultado de Multiplicación({a}, {b}) = {res.r}")
    elif opcion == "4":
        res = stub.Dividir(op)
        if res.error:
            print(f"\n{res.error}")
        else:
            print(f"\nResultado de División({a}, {b}) = {res.r:.4f}")
