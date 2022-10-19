
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def grafica1_rank(df_1_tabla_data1):

    labels = df_1_tabla_data1[1]['Símbolo']
    values = [53.85,55.56,50]

    fig = go.Figure()
    fig.add_trace(go.Pie(labels=labels, values=values, pull=[0, 0.1, 0]))
    fig.update_layout(title="Gráfica 1: Ranking Sebastian")
    fig.show()
    return

def grafica2_rank(df_1_tabla_data2):

    labels = df_1_tabla_data2[1]['Símbolo']
    values = [40,40,33]

    fig = go.Figure()
    fig.add_trace(go.Pie(labels=labels, values=values, pull=[0, 0.1, 0]))
    fig.update_layout(title="Gráfica 2: Ranking Dayana")
    fig.show()
    return

def grafica3_rank(df_1_tabla_data3):

    labels = df_1_tabla_data3[1]['Símbolo']
    values = [50,75,33.33,100,63.64,66.67,100,80,100,100,100]

    fig = go.Figure()
    fig.add_trace(go.Pie(labels=labels, values=values, pull=[0,0,0,0.1]))
    fig.update_layout(title="Gráfica 3: Ranking Jorge")
    return fig.show()

def grafica4_rank(df_1_tabla):

    labels = df_1_tabla[1]['Símbolo']
    values = [53.85,55.56,50,40,40,33,50,75,33.33,100,63.64,66.67,100,80,100,100,100]

    fig = go.Figure()
    fig.add_trace(go.Pie(labels=labels, values=values, pull=[0,0,0,0,0,0,0,0,0,0,0,0,0.1,0,0,0,0]))
    fig.update_layout(title="Gráfica 4: Datos de los 3 concatenados")
    fig.show()
    return

def grafica1_down_up(evo_capital_data1):


    fig = go.Figure()

    fig.add_trace(go.Scatter(x=evo_capital_data1[0].timestamp, y=evo_capital_data1[0].profit_acm_d, mode='lines',name='Beneficio acumulado',line=dict(color='black')))

    fig.add_shape(type="line",
    x0='2022-09-25', y0=evo_capital_data1[0].profit_acm_d.iloc[-1], x1='2022-09-26', y1=evo_capital_data1[0].profit_acm_d.iloc[-1],
    line=dict(color="Red",width=3,dash='dot'))

    fig.add_shape(type="line",
    x0='2022-09-22', y0=evo_capital_data1[0].profit_acm_d.iloc[-1], x1='2022-09-23', y1=evo_capital_data1[0].profit_acm_d.iloc[-1],
    line=dict(color="Green",width=3,dash='dot')) 


    fig.update_layout(title="Gráfica 1: DrawDown y DrawUp")
    fig.show()
    
    return

def grafica2_down_up(evo_capital_data2):


    fig = go.Figure()

    fig.add_trace(go.Scatter(x=evo_capital_data2[0].timestamp, y=evo_capital_data2[0].profit_acm_d, mode='lines',name='Beneficio acumulado',line=dict(color='black')))

    fig.add_shape(type="line",
    x0='2022-09-21', y0=evo_capital_data2[0].profit_acm_d.iloc[-1], x1='2022-09-22', y1=evo_capital_data2[0].profit_acm_d.iloc[-1],
    line=dict(color="Red",width=3,dash='dot'))

    fig.add_shape(type="line",
    x0='2022-09-18', y0=evo_capital_data2[0].profit_acm_d.iloc[-1], x1='2022-09-19', y1=evo_capital_data2[0].profit_acm_d.iloc[-1],
    line=dict(color="Green",width=3,dash='dot')) 


    fig.update_layout(title="Gráfica 2: DrawDown y DrawUp")
    fig.show()
    
    return


def grafica3_down_up(evo_capital_data3):


    fig = go.Figure()

    fig.add_trace(go.Scatter(x=evo_capital_data3[0].timestamp, y=evo_capital_data3[0].profit_acm_d, mode='lines',name='Beneficio acumulado',line=dict(color='black')))

    fig.add_shape(type="line",
    x0='2022-09-22', y0=evo_capital_data3[0].profit_acm_d.iloc[-1], x1='2022-09-25', y1=evo_capital_data3[0].profit_acm_d.iloc[-1],
    line=dict(color="Red",width=3,dash='dot'))

    fig.add_shape(type="line",
    x0='2022-09-25', y0=evo_capital_data3[0].profit_acm_d.iloc[-1], x1='2022-09-26', y1=evo_capital_data3[0].profit_acm_d.iloc[-1],
    line=dict(color="Green",width=3,dash='dot')) 


    fig.update_layout(title="Gráfica 3: DrawDown y DrawUp")
    fig.show()
    
    return





