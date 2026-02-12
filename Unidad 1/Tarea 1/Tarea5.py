partidas = [
    ("Alex", "Bosque", 120),
    ("Luis", "Desierto", 90),
    ("Alex", "Bosque", 150),
    ("Ana", "Ciudad", 200),
    ("Luis", "Bosque", 110)
]

puntos_jugador = {}    
conteo_partidas = {}   
mapas_jugados = set()  
puntos_mapa = {}        

for jugador, mapa, puntos in partidas:
    puntos_jugador[jugador] = puntos_jugador.get(jugador, 0) + puntos
    
    conteo_partidas[jugador] = conteo_partidas.get(jugador, 0) + 1
    
    mapas_jugados.add(mapa)
    
    puntos_mapa[mapa] = puntos_mapa.get(mapa, 0) + puntos

promedios = {jugador: puntos_jugador[jugador] / conteo_partidas[jugador] 
             for jugador in puntos_jugador}

mapa_top = max(puntos_mapa, key=puntos_mapa.get)

print(f"Puntos totales: {puntos_jugador}")
print(f"Mapas explorados: {mapas_jugados}")
print(f"Promedio por jugador: {promedios}")
print(f"Mapa más lucrativo: {mapa_top} ({puntos_mapa[mapa_top]} pts)")