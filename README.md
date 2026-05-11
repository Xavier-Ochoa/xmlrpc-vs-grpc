# RPC Distributed Examples

Implementación de servicios distribuidos usando **XML-RPC** y **gRPC** en Python.  
Incluye dos ejercicios: calculadora aritmética y conversor de temperaturas.

---

## Estructura

```
├── xmlrpc/
│   ├── calculadora_servidor.py
│   ├── calculadora_cliente.py
│   ├── temperatura_servidor.py
│   └── temperatura_cliente.py
│
└── grpc/
    ├── calculadora.proto
    ├── calculadora_servidor.py
    ├── calculadora_cliente.py
    ├── temperatura.proto
    ├── temperatura_servidor.py
    └── temperatura_cliente.py
```

---

## Requisitos

```bash
pip install grpcio grpcio-tools
```

---

## Uso

### XML-RPC

```bash
# Terminal 1
python calculadora_servidor.py

# Terminal 2
python calculadora_cliente.py
```

### gRPC — compilar primero

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculadora.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. temperatura.proto
```

```bash
# Terminal 1
python calculadora_servidor.py

# Terminal 2
python calculadora_cliente.py
```

---

## Tecnologías

- Python 3
- XML-RPC (stdlib)
- gRPC + Protocol Buffers
