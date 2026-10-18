def duración_viaje(distancia, velocidad_media):
    minutos_totales = round((distancia / velocidad_media) * 60)
    horas = minutos_totales // 60
    minutos_restantes = minutos_totales % 60
    return horas, minutos_restantes
horas, minutos_restantes = duración_viaje(45,90)
print(f"{horas} h {minutos_restantes} min")