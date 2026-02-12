transacciones = [
    ("2024-01-10", "Ana", "deposito", 5000, "MXN"),
    ("2024-01-12", "Luis", "retiro", 1500, "MXN"),
    ("2024-01-15", "Ana", "retiro", 2000, "MXN"),
    ("2024-01-18", "Carlos", "deposito", 7000, "MXN")
]

balances = {}

for fecha, cliente, tipo, monto, moneda in transacciones:  # unpacking completo
    
    if cliente not in balances:
        balances[cliente] = 0
    
    if tipo == "deposito":
        balances[cliente] += monto
    elif tipo == "retiro":
        balances[cliente] -= monto

cliente_mayor, balance_mayor = max(balances.items(), key=lambda item: item[1])

print("Balances:", balances)
print("Mayor balance:", cliente_mayor, balance_mayor)
