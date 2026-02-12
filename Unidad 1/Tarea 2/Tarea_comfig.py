config_base = {
    "host": "localhost",
    "port": 3306,
    "debug": False
}

config_desarrollo = {
    "debug": True,
    "log_level": "verbose"
}

config_produccion = {
    "host": "192.168.1.10",
    "log_level": "error"
}

config_dev_final = {**config_base, **config_desarrollo}

config_prod_final = {**config_base, **config_produccion}

def conectar(host, port, debug, log_level="info"):
    print(f"Conectando a {host}:{port}")
    print(f"Debug: {debug}")
    print(f"Log level: {log_level}")

conectar(**config_dev_final)
conectar(**config_prod_final)

def conectar_flexible(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

conectar_flexible(**config_dev_final)
