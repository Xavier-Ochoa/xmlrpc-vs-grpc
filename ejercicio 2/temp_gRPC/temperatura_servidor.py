import grpc
from concurrent import futures
import temperatura_pb2
import temperatura_pb2_grpc


class TemperaturaServidor(temperatura_pb2_grpc.TemperaturaServicer):

    def CelsiusAFahrenheit(self, request, context):
        resultado = (request.valor * 9 / 5) + 32
        return temperatura_pb2.TempSalida(resultado=resultado)

    def FahrenheitACelsius(self, request, context):
        resultado = (request.valor - 32) * 5 / 9
        return temperatura_pb2.TempSalida(resultado=resultado)


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
temperatura_pb2_grpc.add_TemperaturaServicer_to_server(
    TemperaturaServidor(), servidor
)

servidor.add_insecure_port("[::]:5001")
servidor.start()
print("Servidor gRPC (Temperaturas) corriendo en el puerto 5001...")
servidor.wait_for_termination()
