import streamlit as st
import pandas as pd
import numpy as np


st.title("Mi primera aplicación en python")

st.sidebar.title("Opciones")
st.sidebar.image("dmc.png")

st.write("Elaborado por: Victor Hugo Ramirez")

#Ejemplo de SelectBox
opcion = st.sidebar.selectbox(
    "Seleccione una opción",
    ("Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4")
)

if opcion == "Home":
   st.write("¡Bienvenido al menú Home!")
    
elif opcion == "Ejercicio 1":
   st.write("¡Bienvenido al menú Ejercicio 1!")
    
elif opcion == "Ejercicio 2":
   st.write("¡Bienvenido al menú Ejercicio 2!")
   
elif opcion == "Ejercicio 3":
   st.write("¡Bienvenido al menú Ejercicio 3!")

elif opcion == "Ejercicio 4":
   st.write("¡Bienvenido al menú Ejercicio 4!")
