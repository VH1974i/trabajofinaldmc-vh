import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.image("dmc.png")
st.sidebar.title("Opciones")

#Ejemplo de SelectBox
opcion = st.sidebar.selectbox(
    "Seleccione una opción",
    ("Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4")
)

if opcion == "Home":
   st.write("¡Bienvenido al menú Home!")

   st.title("DMC Modulo 1 - Python Fundamentals")
   st.write("Alumno: Victor Hugo Ramírez Ruiz")
   st.write("Curso : Python Fundamentals")
   st.write("Año   : 2026")
   st.write("Alumno: Victor Hugo Ramírez Ruiz")
   st.write("Tecnologías utilizadas: Python, Streamlit.")
    
elif opcion == "Ejercicio 1":
   st.write("¡Bienvenido al menú Ejercicio 1!")

   st.subheader("Variables y condicionales")
   ppto  = st.number_input("Ingrese el presupuesto", min_value =0, value=0)
   gasto = st.number_input("Ingrese el gasto", min_value =0, value=0)

   if st.button("Evaluación"):
       resultado = ppto - gasto
       st.write(f"El resultado es {resultado}")
       
       if gasto <= ppto:
           st.success("El gasto está dentro del presupuesto!")
       else:
           st.warning("El presupuesto fue excedido!")
    
elif opcion == "Ejercicio 2":
   st.write("¡Bienvenido al menú Ejercicio 2!")
   st.subheader("Listas y Diccionarios")
   actividades = {}

   nombre = st.text_input("Ingrese el nombre de la actividad")
   tipo = st.selectbox("Seleccione el tipo:", ("Comercio", "Transporte", "Restaurantes", "Turismo"))
   ppto = st.number_input("Ingrese el presupuesto", min_value =0, value=0, step=1000)
   gasto = st.number_input("Ingrese el gasto", min_value =0, value=0)

   if st.button("Agregar"):
      registro = { "Nombre": nombre,
                   "Tipo": tipo,
                   "Presupuesto": ppto,
                   "Gasto real": gasto }
      actividades.append(registro)
      tabla=pd.DataFrame(actividades)
      event = st.dataframe(tabla)
   
elif opcion == "Ejercicio 3":
   st.write("¡Bienvenido al menú Ejercicio 3!")

elif opcion == "Ejercicio 4":
   st.write("¡Bienvenido al menú Ejercicio 4!")
