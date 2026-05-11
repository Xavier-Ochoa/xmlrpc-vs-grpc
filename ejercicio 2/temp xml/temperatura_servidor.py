from xmlrpc.server import SimpleXMLRPCServer

def celsius_a_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9

servidor = SimpleXMLRPCServer(("localhost", 8001))
print("Servidor XML-RPC (Temperaturas) escuchando en el puerto 8001...")

servidor.register_function(celsius_a_fahrenheit, "celsius_a_fahrenheit")
servidor.register_function(fahrenheit_a_celsius, "fahrenheit_a_celsius")

servidor.serve_forever()
