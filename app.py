import streamlit as st
from pandas import DataFrame
from numpy.random import random
import plotly.graph_objects as go

data1 = DataFrame(random((100, 3)))
data2 = DataFrame(random((100, 3)))

trace1 = [go.Scatter3d(x=data1[0], y=data1[1], z=data1[2])]
trace2 = [go.Scatter3d(x=data2[0], y=data2[1], z=data2[2])]

fig = go.Figure(trace1 + trace2, layout=go.Layout(uirevision='foo'))

title = st.text_input('Movie title', 'Life of Brian')
st.plotly_chart(fig, use_container_width=True)
st.title("Proyecto 12")
st.write(" En la presente pagina, se presenta una presentacion de un indice de felicidad constriudo a partir de 10 diferentes variables de 60 paises ")
st.subheader("Explicacion variables usadas: ")
st.write("1 Inflacion:")
st.write("2 IDH:")
st.write("3 PIB per Capita:")
st.write("4 :")
st.write("5 Tasa de suicidios:")
st.write("6 Salario medio de los empleados:")
st.write("7 Desempleo total:")
st.write("8 Esperanza de vida:")
st.write("9 Poblacion mayor a los 65 años:")
st.write("10 Tasa de homicidios intencionales:")

st.subheader("Reduccion de dimencionalidad (PCA): ")
st.subheader("Cluster y Kmeans:")
