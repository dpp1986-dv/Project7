import pandas as pd
import plotly.graph_objects as go
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

build_histogram = st.checkbox('Construir histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_histogram:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')

    st.plotly_chart(fig, width='stretch')

if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    fig = go.Figure(data=[
        go.Scatter(
            x=car_data['odometer'],
            y=car_data['price'],
            mode='markers'
        )
    ])

    fig.update_layout(
        title='Relación entre Odómetro y Precio',
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )

    st.plotly_chart(fig, width='stretch')
