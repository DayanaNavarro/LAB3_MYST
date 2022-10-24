# Mostrado de datos procesados

import data as dt

#lECTURA DE ARCHIVOS

data1 = fn.f_leer_archivo("Data1")
data2 = fn.f_leer_archivo("Data2")
data3 = fn.f_leer_archivo("Data3")

#DATOS CONCATENADOS
tabla = pd.concat([data1,data2,data3]).reset_index()

#PIP SIZE

instruments_pips = fn.f_leer_archivo("instruments_pips")

parametro = "EURUSD"
num_pips1 = fn.f_pip_size1(parametro, instruments_pips)
num_pips2 = fn.f_pip_size2(parametro)

#COLUMNAS TIEMPO
data1 = fn.f_columnas_tiempos(data1)
data2 = fn.f_columnas_tiempos(data2)
data3 = fn.f_columnas_tiempos(data3)

#COLUMANS PIPS
data1 = fn.f_columnas_pips(data1, fn.f_pip_size2)
data2 = fn.f_columnas_pips(data2, fn.f_pip_size2)
data3 = fn.f_columnas_pips(data3, fn.f_pip_size2)

#ESTADISTICAS

df_1_tabla_data1 = fn.f_estadisticas_ba(data1, fn.f_columnas_pips, fn.f_pip_size2)
df_1_tabla_data1 = fn.f_estadisticas_ba(data1, fn.f_columnas_pips, fn.f_pip_size2)
vs.grafica1_rank(df_1_tabla_data1)

df_1_tabla_data2 = fn.f_estadisticas_ba(data2, fn.f_columnas_pips, fn.f_pip_size2)
df_1_tabla_data2 = fn.f_estadisticas_ba(data2, fn.f_columnas_pips, fn.f_pip_size2)
vs.grafica2_rank(df_1_tabla_data2)

df_1_tabla_data3 = fn.f_estadisticas_ba(data3, fn.f_columnas_pips, fn.f_pip_size2)
df_1_tabla_data3 = fn.f_estadisticas_ba(data3, fn.f_columnas_pips, fn.f_pip_size2)
vs.grafica3_rank(df_1_tabla_data3)

df_1_tabla = fn.f_estadisticas_ba2(tabla,fn.f_columnas_pips, fn.f_pip_size2)
df_1_tabla = fn.f_estadisticas_ba2(tabla,fn.f_columnas_pips, fn.f_pip_size2)
vs.grafica4_rank(df_1_tabla)

#METRICAS DE ATRIBUCION AL DESEMPEÑO

yahoo_financials = YahooFinancials('^GSPC')
data = yahoo_financials.get_historical_price_data(start_date='2022-09-19', 
                                                 end_date='2022-09-26', time_interval="daily")
Prices1= pd.DataFrame(data['^GSPC']['prices'])
Prices1 =Prices1.drop('date', axis=1).set_index('formatted_date')
Prices = Prices1['adjclose']

evo_capital_data1=fn.f_evolucion_capital(data1)
Me_atri_desem1= fn.f_estadisticas_mad(data1,Prices)
vs.grafica1_down_up(evo_capital_data1)


yahoo_financials = YahooFinancials('^GSPC')
data = yahoo_financials.get_historical_price_data(start_date='2022-09-19', 
                                                 end_date='2022-09-22', time_interval="daily")
Prices2= pd.DataFrame(data['^GSPC']['prices'])
Prices2 =Prices2.drop('date', axis=1).set_index('formatted_date')
Prices = Prices2['adjclose']

evo_capital_data2=fn.f_evolucion_capital(data2)
Me_atri_desem2= fn.f_estadisticas_mad(data2,Prices)
vs.grafica2_down_up(evo_capital_data2)

yahoo_financials = YahooFinancials('^GSPC')
data = yahoo_financials.get_historical_price_data(start_date='2022-09-21', 
                                                 end_date='2022-09-26', time_interval="daily")
Prices3= pd.DataFrame(data['^GSPC']['prices'])
Prices3 =Prices3.drop('date', axis=1).set_index('formatted_date')
Prices = Prices3['adjclose']

evo_capital_data3=fn.f_evolucion_capital(data3)
Me_atri_desem3= fn.f_estadisticas_mad(data3,Prices)
vs.grafica3_down_up(evo_capital_data3)






















