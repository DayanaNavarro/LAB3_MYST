# Realización de funciones utilizadas para el Laboratorio 3

import pandas as pd
from datetime import datetime
import statistics
from datetime import date, timedelta
import MetaTrader5 as mt5
import pytz

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

def f_estadisticas_ba(param_data,f_columnas_pips, f_pip_size2):
    
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
    
    sy = param_data.Símbolo.unique().tolist()
    rank = [param_data[(param_data.Beneficio >0)&(param_data.Símbolo == i)].Posición.nunique() / param_data[param_data.Símbolo == i].Posición.nunique() for i in sy]

    df_2_ranking = pd.DataFrame({"Símbolo": sy, "rank": rank})
    
    for i in range(len(df_2_ranking)):
        df_2_ranking.iloc[i,1] = str(round(df_2_ranking.iloc[i,1]*100,2)) + "%"

    
    
    return df_1_tabla, df_2_ranking


# Función para caluclar estadísticas básicas y ranking por instrumentos (todos los datos)

def f_estadisticas_ba2(tabla,f_columnas_pips, f_pip_size2):
    #tabla=pd.concat([data1,data2,data3]).reset_index()
    ops_totales=len(tabla)
    ops_ganadoras_totales=len(tabla[tabla["Beneficio"]>0])
    ops_ganadoras_compra=len(tabla[(tabla["Beneficio"]>0)&(tabla["Tipo"]=="buy")])
    ops_ganadoras_venta=len(tabla[(tabla["Beneficio"]>0)&(tabla["Tipo"]=="sell")])
    ops_perdedoras_totales=len(tabla[tabla["Beneficio"]<0])
    ops_perdedoras_compra=len(tabla[(tabla["Beneficio"]<0)&(tabla["Tipo"]=="buy")])
    ops_perdedoras_venta=len(tabla[(tabla["Beneficio"]<0)&(tabla["Tipo"]=="sell")])
    mediana=tabla["Beneficio"].median()
    Mediana_pip = statistics.median(f_columnas_pips(tabla,f_pip_size2)['pips'])
    r_efectividad=ops_ganadoras_totales/ops_totales
    r_proporcion=ops_ganadoras_totales/ops_perdedoras_totales
    r_efectividad_c=ops_ganadoras_compra/ops_totales
    r_efectividad_v=ops_ganadoras_venta/ops_totales
    df_1_tabla=pd.DataFrame()
    df_1_tabla["Media"]=["Ops totales","Ganadoras","Ganadoras_c","Ganadoras_v","Perdedoras","Perdedoras_c","Perdedoras_v","Mediana (profit)","Mediana(pips)","r_efectividad","r_proporcion","r_efectividad_c","r_efectividad_v"]
    df_1_tabla["Valor"]=[ops_totales,ops_ganadoras_totales,ops_ganadoras_compra,ops_ganadoras_venta,ops_perdedoras_totales,ops_perdedoras_compra,ops_perdedoras_venta,mediana,Mediana_pip,r_efectividad,r_proporcion,r_efectividad_c,r_efectividad_v]
    df_1_tabla["Descripcion"]=["Operaciones totales","Operaciones ganadoras","Operaciones ganadoras compra","Operaciones ganadoras venta","Operaciones Perdedoras","Operaciones Perdedoras compra","Operaciones Perdedoras venta","Mediana de profit de operaciones","Mediana de pips de operaciones","Ganadoras Totales/Operaciones Totales","Ganadoras Totales/Perdedoras Totales","Ganadoras Compras/Operaciones Totales","Ganadoras Ventas/ Operaciones Totales"]
    
    
    sy = tabla.Símbolo.unique().tolist()
    rank = [tabla[(tabla.Beneficio >0)&(tabla.Símbolo == i)].Posición.nunique() / tabla[tabla.Símbolo == i].Posición.nunique() for i in sy]

    df_2_ranking = pd.DataFrame({"Símbolo": sy, "rank": rank})
    
    for i in range(len(df_2_ranking)):
        df_2_ranking.iloc[i,1] = str(round(df_2_ranking.iloc[i,1]*100,2)) + "%"
    
    
    return df_1_tabla, df_2_ranking

# Función que agrega la evolución de capital diaria

def f_evolucion_capital(param_data): 
    capital = pd.DataFrame()

    fecha_inicial= list(param_data['Fecha/Hora'].apply(lambda x: x.split(' ')[0])) #Fecha en que abrio
    fecha_cierre= list(param_data['Fecha/Hora.1'].apply(lambda x: x.split(' ')[0])) #Fecha en que se cerro

    fecha1 = pd.to_datetime(fecha_inicial, format='%Y.%m.%d')
    fecha2 = pd.to_datetime(fecha_cierre, format='%Y.%m.%d')
    
    fecha_start = fecha1[0]
    fecha_end = fecha1[-1]
    
    fechas = []
    
    # Agregado de fechas en las que no hubo transacciones
    for i in range(int(str(fecha_end-fecha_start)[0])+1):
        
        fechas.append(fecha_start+timedelta(i))

    capital["timestamp"]  = fechas
    capital['profit_d'] = [param_data[fecha2 == j].Beneficio.sum() for j in fechas]
    capital["profit_acm_d"] = capital.profit_d.cumsum() + 100000
    
    return capital, fecha_start, fecha_end


#Función fechas para DrawDown y DrawUp

def fechas_down_up(): 
    
    #Fechas Data1
    fecha_inicial_1_down= '2022-09-25'
    fecha_final_1_down='2022-09-26'

    fecha_inicial_1_up= '2022-09-22'
    fecha_final_1_up='2022-09-23'
    
    
    #Fechas Data2

    fecha_inicial_2_down= '2022-09-21'
    fecha_final_2_down='2022-09-22'

    fecha_inicial_2_up= '2022-09-18'
    fecha_final_2_up='2022-09-19'
    
    
    #Fechas Data3

    fecha_inicial_3_down= '2022-09-22'
    fecha_final_3_down='2022-09-25'

    fecha_inicial_3_up= '2022-09-25'
    fecha_final_3_up='2022-09-26'
    
    return fecha_inicial_1_down,fecha_final_1_down, fecha_inicial_1_up,fecha_final_1_up,fecha_inicial_2_down,fecha_final_2_down,fecha_inicial_2_up, fecha_final_2_up,fecha_inicial_3_down,fecha_final_3_down,fecha_inicial_3_up,fecha_final_3_up

# Función con el DataFrame con las Métricas de Atribución al Desempeño

def f_estadisticas_mad(param_data,Prices):
    
    mad=pd.DataFrame()

    r=0.05

    # Sharpe Ratio Original
    rp=f_evolucion_capital(param_data)[0]["profit_acm_d"].pct_change()
    rp1=rp[1:].mean()
    sdp=rp[1:].std()

    sharpe_original = (rp1 - r)/sdp

    # Sharpe Ratio Actualizado

    r_trader=rp[1:].mean()
    r_b=Prices.pct_change()
    r_benchmark=r_b[1:].mean()

    sharpe_actualizado = (r_trader-r_benchmark)/sdp

    # DrawDown (Capital)
    
    Fecha_inicial_down=fechas_down_up()[8]
    
    Fecha_final_down=fechas_down_up()[9]
    
    drawdown= (f_evolucion_capital(param_data)[0].loc[:,"profit_acm_d"]).min()

    # DrawUp (Capital)
    
    Fecha_inicial_up=fechas_down_up()[10]
    
    Fecha_final_up=fechas_down_up()[11]

    drawup= (f_evolucion_capital(param_data)[0].loc[:,"profit_acm_d"]).max()


    mad["metrica"]=['sharpe_original','sharpe_actualizado','drawdown_capi[Fecha Incial]', 'drawdown_capi[Fecha final]', 'drawdown_capi[$ capital]', 'drawup_capi[Fecha Inicial]', 'drawup_capi[Fecha Final]', 'drawup_capi[$ capital]']

    mad["Valor"]=[sharpe_original,sharpe_actualizado,Fecha_inicial_down,Fecha_final_down,drawdown,Fecha_inicial_up,Fecha_final_up,drawup]

    mad["Descripcion"]=["Sharpe Ratio Fórmula Original","Sharpe Ratio Fórmula Ajustada","Fecha inicial del DrawDown de Capital", "Fecha final del DrawDown de Capital", "Máxima pérdida flotante registrada", "Fecha inicial del DrawUp de Capital", "Fecha final del DrawUp de Capital", "Máxima ganancia flotante registrada"]
    
    return mad

def MetaTrader5(symbol: str):
    pd.set_option('display.max_columns', 500) # number of columns to be displayed
    pd.set_option('display.width', 1500)      # max table width to display
    
    # establish connection to MetaTrader 5 terminal
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()
    
    # set time zone to UTC
    timezone = pytz.timezone("Etc/UTC")
    # create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
    utc_from = datetime(2022, 9, 21, tzinfo=timezone)
    utc_to = datetime(2022, 9, 21, hour = 13, tzinfo=timezone)
    # get bars from USDJPY M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zone
    rates = mt5.copy_rates_range(symbol, mt5.TIMEFRAME_M1, utc_from, utc_to)
    
    # shut down connection to the MetaTrader 5 terminal
    mt5.shutdown()
    
    # create DataFrame out of the obtained data
    rates_frame = pd.DataFrame(rates)

    # convert time in seconds into the 'datetime' format
    rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
    
    return rates_frame






