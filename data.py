# Cargado y limpieza de datos

import functions as fn
import pandas as pd

# Cargado de datos
data1 = fn.f_leer_archivo("Data1")
data2 = fn.f_leer_archivo("Data2")
#data3 = fn.f_leer_archivo("Data3")
data_total = pd.concat([data1,data2]).reset_index()
instruments_pips = fn.f_leer_archivo("instruments_pips")


parametro = "EURUSD"
fn.f_pip_size1(parametro, instruments_pips)

fn.f_pip_size2(parametro)

# Agregado de columnas de tiempo
data1 = fn.f_columnas_tiempos(data1)
data2 = fn.f_columnas_tiempos(data2)
#data3 = fn.f_columnas_tiempos(data3)

# Agregado de columnas de pips
data1 = fn.f_columnas_pips(data1, fn.f_pip_size2)
data2 = fn.f_columnas_pips(data2, fn.f_pip_size2)
#data3 = fn.f_columnas_pips(data3, fn.f_pip_size2)

# Estadísticas de transacciones
data1 = fn.f_estadisticas_ba(data1, fn.f_columnas_pips, fn.f_pip_size2)
data2 = fn.f_estadisticas_ba(data2, fn.f_columnas_pips, fn.f_pip_size2)
#data3 = fn.f_estadisticas_ba(data3, fn.f_columnas_pips, fn.f_pip_size2)

# Estadísticas de transacciones por equipo
df_1_tabla = fn.f_estadisticas_ba2(data_total)