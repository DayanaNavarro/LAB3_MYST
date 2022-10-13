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
def f_pip_size1(param_ins: str, instruments_pips):
    
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

# Función para detectar pips de activos que no están en el archivo

def f_pip_size2(size):

    di = {"EURUSD":10000,"USDJPY":100,"GBPUSD":10000,"EURCAD":10000,"BITCOIN":100,"GBPJPY":100,"USDCAD":10000,
         "EURJPY":100,"CHFJPY":100,"NAT.GAS":100,"EURMXN":100,"AUDCAD":10000,"EURGBP":10000,"CADCHF":10000,"WTI":100,
         "RENA.PA":100,"BRENT":100,"GT.O":100,"MSFT.O":100}

    return  di[size]

# Función para agregar columnas de transformaciones de pips

def f_columnas_pips(param_data,f_pip_size):

    param_data["pips"]=0

    for i in range(len(param_data)):

        if param_data.loc[i,"Tipo"]=="buy":
            param_data.loc[i,"pips"] = (float(param_data.loc[i,'Precio']) - float(param_data.loc[i,'Precio.1']))*f_pip_size(param_data.loc[i,"Símbolo"])

        else:
            param_data.loc[i,"pips"] = (float(param_data.loc[i,'Precio.1']) - float(param_data.loc[i,'Precio']))*f_pip_size(param_data.loc[i,"Símbolo"])

    param_data['pips_acm'] = param_data.pips.cumsum()
    param_data['profit_acm'] = param_data.Beneficio.cumsum()
    
    return param_data


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

# Función para caluclar estadísticas básicas y ranking por instrumentos (individual)

def f_estadisticas_ba(param_data, f_columnas_pips, f_pip_size2):
    
    Ops_totales = param_data.Posición.nunique()
    Ganadoras = param_data[param_data.Beneficio > 0].Posición.nunique()
    Ganadoras_c = param_data[(param_data.Beneficio >0) &(param_data.Tipo == "buy")].Posición.nunique()
    Ganadoras_v = param_data[(param_data.Beneficio >0) &(param_data.Tipo == "sell")].Posición.nunique()
    Perdedoras = param_data[param_data.Beneficio< 0].Posición.nunique()
    Perdedoras_c = param_data[(param_data.Beneficio <0) &(param_data.Tipo == "buy")].Posición.nunique()
    Perdedoras_v = param_data[(param_data.Beneficio <0) &(param_data.Tipo == "sell")].Posición.nunique()
    Mediana_profit = statistics.median(param_data['Beneficio'])
    Mediana_pip = statistics.median(f_columnas_pips(param_data,f_pip_size2)['pips'])
    r_efectividad = Ganadoras/Ops_totales
    r_proporcion = Ganadoras/Perdedoras
    r_efectividad_c = Ganadoras_c/Ops_totales
    r_efectividad_v = Ganadoras_v/Ops_totales

    df_1_tabla=pd.DataFrame()
    df_1_tabla["Media"]=["Ops totales","Ganadoras","Ganadoras_c","Ganadoras_v","Perdedoras","Perdedoras_c","Perdedoras_v","Mediana (profit)","Mediana(pips)","r_efectividad","r_proporcion","r_efectividad_c","r_efectividad_v"]
    df_1_tabla["Valor"]=[Ops_totales,Ganadoras,Ganadoras_c,Ganadoras_v,Perdedoras,Perdedoras_c,Perdedoras_v,Mediana_profit,Mediana_pip,r_efectividad,r_proporcion,r_efectividad_c,r_efectividad_v]
    df_1_tabla["Descripcion"]=["Operaciones totales","Operaciones ganadoras","Operaciones ganadoras compra","Operaciones ganadoras venta","Operaciones Perdedoras","Operaciones Perdedoras compra","Operaciones Perdedoras venta","Mediana de profit de operaciones","Mediana de pips de operaciones","Ganadoras Totales/Operaciones Totales","Ganadoras Totales/Perdedoras Totales","Ganadoras Compras/Operaciones Totales","Ganadoras Ventas/ Operaciones Totales"]
    
    return df_1_tabla

# Función para caluclar estadísticas básicas y ranking por instrumentos (todos los datos)
def f_estadisticas_ba2(tabla):

    ops_totales=len(tabla)
    ops_ganadoras_totales=len(tabla[tabla["Beneficio"]>0])
    ops_ganadoras_compra=len(tabla[(tabla["Beneficio"]>0)&(tabla["Tipo"]=="buy")])
    ops_ganadoras_venta=len(tabla[(tabla["Beneficio"]>0)&(tabla["Tipo"]=="sell")])
    ops_perdedoras_totales=len(tabla[tabla["Beneficio"]<0])
    ops_perdedoras_compra=len(tabla[(tabla["Beneficio"]<0)&(tabla["Tipo"]=="buy")])
    ops_perdedoras_venta=len(tabla[(tabla["Beneficio"]<0)&(tabla["Tipo"]=="sell")])
    mediana=tabla["Beneficio"].median()
    r_efectividad=ops_ganadoras_totales/ops_totales
    r_proporcion=ops_perdedoras_totales/ops_totales
    r_efectividad_c=ops_ganadoras_compra/ops_totales
    r_efectividad_v=ops_ganadoras_venta/ops_totales
    df_1_tabla=pd.DataFrame()
    df_1_tabla["Media"]=["Ops totales","Ganadoras","Ganadoras_c","Ganadoras_v","Perdedoras","Perdedoras_c","Perdedoras_v","Mediana (profit)","Mediana(pips)","r_efectividad","r_proporcion","r_efectividad_c","r_efectividad_v"]
    df_1_tabla["Valor"]=[ops_totales,ops_ganadoras_totales,ops_ganadoras_compra,ops_ganadoras_venta,ops_perdedoras_totales,ops_perdedoras_compra,ops_perdedoras_venta,mediana,0,r_efectividad,r_proporcion,r_efectividad_c,r_efectividad_v]
    df_1_tabla["Descripcion"]=["Operaciones totales","Operaciones ganadoras","Operaciones ganadoras compra","Operaciones ganadoras venta","Operaciones Perdedoras","Operaciones Perdedoras compra","Operaciones Perdedoras venta","Mediana de profit de operaciones","Mediana de pips de operaciones","Ganadoras Totales/Operaciones Totales","Ganadoras Totales/Perdedoras Totales","Ganadoras Compras/Operaciones Totales","Ganadoras Ventas/ Operaciones Totales"]
    
    return df_1_tabla
