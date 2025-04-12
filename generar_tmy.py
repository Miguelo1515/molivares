import pandas as pd
import numpy as np
from datetime import datetime

def calcular_fs(datos_mes, variables):
    """
    Calcula el Factor de Selección (FS) para cada variable
    """
    fs = {}
    for var in variables:
        # Calcular CDF para la variable
        sorted_data = np.sort(datos_mes[var])
        cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        fs[var] = {'sorted_data': sorted_data, 'cdf': cdf}
    return fs

def calcular_estadisticas(df_mes):
    """
    Calcula estadísticas mensuales para cada variable
    """
    return {
        'GHI_mean': df_mes['GHI'].mean(),
        'DNI_mean': df_mes['DNI'].mean(),
        'DHI_mean': df_mes['DHI'].mean(),
        'Tdry_mean': df_mes['Tdry'].mean(),
        'RH_mean': df_mes['RH'].mean(),
        'Wspd_mean': df_mes['Wspd'].mean()
    }

def seleccionar_mes_tmy(datos_por_anio, variables_peso):
    """
    Selecciona el mes más representativo basado en el método de Sandia
    """
    # Pesos para cada variable
    pesos = {
        'GHI': 0.3,    # Mayor peso para radiación solar
        'DNI': 0.2,
        'DHI': 0.1,
        'Tdry': 0.2,   # Peso importante para temperatura
        'RH': 0.1,     # Menor peso para humedad
        'Wspd': 0.1    # Menor peso para velocidad del viento
    }
    
    min_suma_fs = float('inf')
    anio_seleccionado = None
    
    # Calcular estadísticas para todos los años
    stats_por_anio = {año: calcular_estadisticas(datos) 
                     for año, datos in datos_por_anio.items()}
    
    # Calcular promedios generales
    all_stats = pd.DataFrame(stats_por_anio).mean(axis=1)
    
    # Calcular suma ponderada de diferencias
    for año, datos in datos_por_anio.items():
        suma_fs = 0
        for var in variables_peso:
            diff = abs(stats_por_anio[año][f'{var}_mean'] - all_stats[f'{var}_mean'])
            diff_norm = diff / all_stats[f'{var}_mean']  # Normalizar diferencia
            suma_fs += diff_norm * pesos[var]
        
        if suma_fs < min_suma_fs:
            min_suma_fs = suma_fs
            anio_seleccionado = año
            
    return anio_seleccionado

# Leer el archivo CSV
df = pd.read_csv('CLASE 1/antofagasta.csv', skiprows=2)

# Crear columna de fecha
df['Fecha'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])

# Variables a considerar para el TMY
variables_tmy = ['GHI', 'DNI', 'DHI', 'Tdry', 'RH', 'Wspd']

# Diccionario para almacenar el TMY
tmy_data = []

# Procesar cada mes
for mes in range(1, 13):
    # Filtrar datos para el mes actual
    datos_mes = df[df['Month'] == mes]
    
    # Separar datos por año
    datos_por_anio = {año: datos_mes[datos_mes['Year'] == año] 
                     for año in datos_mes['Year'].unique()}
    
    # Seleccionar el año más representativo para este mes
    anio_seleccionado = seleccionar_mes_tmy(datos_por_anio, variables_tmy)
    
    # Agregar los datos del mes seleccionado al TMY
    tmy_data.append(datos_por_anio[anio_seleccionado])

# Concatenar todos los meses seleccionados
tmy_df = pd.concat(tmy_data)

# Ordenar por fecha
tmy_df = tmy_df.sort_values('Fecha')

# Guardar el TMY
tmy_df.to_csv('CLASE 1/antofagasta_tmy.csv', index=False)
print("TMY generado y guardado como 'antofagasta_tmy.csv'")

# Imprimir resumen de los meses seleccionados
print("\nResumen de meses seleccionados para el TMY:")
for mes in range(1, 13):
    datos_mes = tmy_df[tmy_df['Month'] == mes]
    if not datos_mes.empty:
        anio = datos_mes['Year'].iloc[0]
        print(f"Mes {mes}: Datos del año {anio}")
        print(f"    GHI promedio: {datos_mes['GHI'].mean():.2f} W/m²")
        print(f"    Temperatura promedio: {datos_mes['Tdry'].mean():.2f}°C") 