# xmlrpc-vs-grpc

Implementación de servicios distribuidos en Python usando **XML-RPC** y **gRPC**.  
Dos ejercicios prácticos: calculadora aritmética y conversor de temperaturas.

---

## Estructura

```
xmlrpc-vs-grpc/
├── ejercicio 1/
│   ├── calc xml/
│   │   ├── calculadora_servidor.py
│   │   └── calculadora_cliente.py
│   └── calc_gRPC/
│       ├── calculadora.proto
│       ├── calculadora_pb2.py
│       ├── calculadora_pb2_grpc.py
│       ├── calculadora_servidor.py
│       └── calculadora_cliente.py
│
└── ejercicio 2/
    ├── temp xml/
    │   ├── temperatura_servidor.py
    │   └── temperatura_cliente.py
    └── temp_gRPC/
        ├── temperatura.proto
        ├── temperatura_pb2.py
        ├── temperatura_pb2_grpc.py
        ├── temperatura_servidor.py
        └── temperatura_cliente.py
```

---

## Requisitos

```bash
pip install grpcio grpcio-tools
```

> XML-RPC no requiere instalación adicional, viene incluido en la librería estándar de Python.

---

## Uso

### Ejercicio 1 — Calculadora

**XML-RPC** (puerto 8000)
```bash
# Terminal 1
python "ejercicio 1/calc xml/calculadora_servidor.py"

# Terminal 2
python "ejercicio 1/calc xml/calculadora_cliente.py"
```

**gRPC** (puerto 5000)
```bash
# Terminal 1
python "ejercicio 1/calc_gRPC/calculadora_servidor.py"

# Terminal 2
python "ejercicio 1/calc_gRPC/calculadora_cliente.py"
```

---

### Ejercicio 2 — Conversor de Temperaturas

**XML-RPC** (puerto 8001)
```bash
# Terminal 1
python "ejercicio 2/temp xml/temperatura_servidor.py"

# Terminal 2
python "ejercicio 2/temp xml/temperatura_cliente.py"
```

**gRPC** (puerto 5001)
```bash
# Terminal 1
python "ejercicio 2/temp_gRPC/temperatura_servidor.py"

# Terminal 2
python "ejercicio 2/temp_gRPC/temperatura_cliente.py"
```

---

### Recompilar archivos `.proto` (opcional)

Solo necesario si se modifica algún `.proto`:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculadora.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. temperatura.proto
```

---

## Tecnologías

- Python 3
- XML-RPC — stdlib
- gRPC + Protocol Buffers
