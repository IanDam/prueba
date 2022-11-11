import streamlit as st
import pandas as pd
import numpy as np

st.title("Proyecto 6")
st.write(" En la presente pagina, a partir de un dataset dentro del que se determina la potabilidad del agua a partir de caracteristicas especificas como la cantidad de carbono organico o su condutividad, se realizan lo siguiente: ")
st.subheader("Exploracion inicial: ")
st.write("Para la exploración inicial obtenemos información acerca del dataset cargado. En este encontramos 3276 entradas y un total de 10 variables dentro de ella (columnas). Así mismo vemos que de las 10 columnas de datos; 1 es de typo int, 9 de tipo float.Adicionalmente se observa que existen datos nulos en las variables ph, Sulfate y Trihalomethanes.")
