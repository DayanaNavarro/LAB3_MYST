# Realización de funciones utilizadas para el Laboratorio 3

import pandas as pd
from datetime import datetime
import statistics

# Función para leer archivos 
def f_leer_archivo(param_archivo: str):
    direccion = "files/" + param_archivo + ".csv"
    data = pd.read_csv(direccion)
    return data

# Función para detectar pips
def f_pip_size1(param_ins: str):
    
    for i in range(len(instruments_pips)):
        
        # Convertimos al mismo formato
        param = instruments_pips.iloc[i,0]
        character = "_"
        for j in range(len(character)):
            param = param.replace(character[j],"")
            
            # Al encontrar el mismo parámetro convierte a los pips
            if param_ins == param:
                PipLocation = instruments_pips.iloc[i,4]
                PipLocation = abs(PipLocation)
                pips = "1" + (str(0) * PipLocation)
                pips = int(pips)
            else:
                pass
        
    return pips


# Agregado de columnas de tiempo en segundos
def f_columnas_tiempos(param_data):
    
    lista = []
    for i in range(len(param_data)):
        tiempo1 = param_data.iloc[i,0]
        tiempo2 = param_data.iloc[i,8]
        
        characters = ".: "
        for j in range(len(characters)):
            tiempo1 = tiempo1.replace(characters[j]," ")
            tiempo2 = tiempo2.replace(characters[j]," ")
            
        tiempo1 = tiempo1.split(' ')
        tiempo2 = tiempo2.split(' ')
        
        open_op = datetime(int(tiempo1[0]),
                           int(tiempo1[1]),
                           int(tiempo1[2]),
                           int(tiempo1[3]),
                           int(tiempo1[4]),
                           int(tiempo1[5]))

        close_op = datetime(int(tiempo2[0]),
                            int(tiempo2[1]),
                            int(tiempo2[2]),
                            int(tiempo2[3]),
                            int(tiempo2[4]),
                            int(tiempo2[5]))
        
        time_opened = close_op - open_op
        time_opened = time_opened.total_seconds()
        lista.append(time_opened)

    param_data["Tiempo_abierta_seg"] = lista
    
    return param_data





