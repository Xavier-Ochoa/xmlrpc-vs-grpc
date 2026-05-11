import grpc
from concurrent import futures
import calculadora_pb2
import calculadora_pb2_grpc
class CalculadoraServidor(calculadora_pb2_grpc.CalculadoraServicer):

    def Sumar(self, request, context):
        resultado = request.a + request.b
        return calculadora_pb2.Resultado(r=resultado)

    def Restar(self, request, context):
        resultado = request.a - request.b
        return calculadora_pb2.Resultado(r=resultado)

    def Multiplicar(self, request, context):
        resultado = request.a * request.b
        return calculadora_pb2.Resultado(r=resultado)

    def Dividir(self, request, context):
        if request.b == 0:
            return calculadora_pb2.ResultadoDivision(
                r=0, error="Error: no se puede dividir entre 0"
            )
        resultado = request.a / request.b
        return calculadora_pb2.ResultadoDivision(r=resultado, error="")

servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
calculadora_pb2_grpc.add_CalculadoraServicer_to_server(
    CalculadoraServidor(), servidor
)
servidor.add_insecure_port("[::]:5000")
servidor.start()
print("Servidor gRPC (Calculadora) corriendo en el puerto 5000...")
servidor.wait_for_termination()
