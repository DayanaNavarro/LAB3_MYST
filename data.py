# Cargado y limpieza de datos

import functions as fn
import pandas as pd


### --- 
#import MetaTrader5 as MT5
#MT5.initialize()
# MT5.copy_rate_range() <- (EURUSD,frec(5m,15m,...),dates)
### ---

# Cargado de datos
data1 = fn.f_leer_archivo("Data1")
data2 = fn.f_leer_archivo("Data2")
data3 = fn.f_leer_archivo("Data3")
data_total = pd.concat([data1,data2,data3]).reset_index()
instruments_pips = fn.f_leer_archivo("instruments_pips")

# Número de pips
parametro = "EURUSD"
num_pips1 = fn.f_pip_size1(parametro, instruments_pips)
num_pips2 = fn.f_pip_size2(parametro)

# Agregado de columnas de tiempo
data1 = fn.f_columnas_tiempos(data1)
data2 = fn.f_columnas_tiempos(data2)
data3 = fn.f_columnas_tiempos(data3)

# Agregado de columnas de pips
data1 = fn.f_columnas_pips(data1, fn.f_pip_size2)
data2 = fn.f_columnas_pips(data2, fn.f_pip_size2)
data3 = fn.f_columnas_pips(data3, fn.f_pip_size2)

# Estadísticas de transacciones
df_1_tabla_data1 = fn.f_estadisticas_ba(data1, fn.f_columnas_pips, fn.f_pip_size2)
df_1_tabla_data2 = fn.f_estadisticas_ba(data2, fn.f_columnas_pips, fn.f_pip_size2)
df_1_tabla_data3 = fn.f_estadisticas_ba(data3, fn.f_columnas_pips, fn.f_pip_size2)

# Estadísticas de transacciones por equipo
df_1_tabla = fn.f_estadisticas_ba2(tabla,fn.f_columnas_pips, fn.f_pip_size2)


# Evolución de capital
evo_capital_data1=fn.f_evolucion_capital(data1)
evo_capital_data2=fn.f_evolucion_capital(data2)
evo_capital_data2=fn.f_evolucion_capital(data3)


#Metricas de Atribución al desempeño

Me_atri_desem1= fn.f_estadisticas_mad(data1,Prices)
Me_atri_desem2= fn.f_estadisticas_mad(data2,Prices)
Me_atri_desem3= fn.f_estadisticas_mad(data3,Prices)