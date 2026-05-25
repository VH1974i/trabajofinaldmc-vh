import streamlit as st
import pandas as pd
from clase_actividad import actividad

if "actividades" not in st.session_state:
    st.session_state.actividades = []

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

   nombre = st.text_input("Ingrese el nombre de la actividad")
   tipo   = st.selectbox("Seleccione el tipo:", ("Comercio", "Transporte", "Restaurantes", "Turismo"))
   ppto   = st.number_input("Ingrese el presupuesto", min_value =0, value=0, step=1000)
   gasto  = st.number_input("Ingrese el gasto", min_value =0, value=0, step=500)

   if st.button("Agregar", type="primary"):
       if nombre:
           registro = { "Nombre": nombre,
                        "Tipo": tipo,
                        "Presupuesto": ppto,
                        "Gasto real": gasto,
                        "Estado": ""}

           existe_duplicado = any(
              registro["Nombre"].strip().lower() == nombre.strip().lower() 
              for registro in st.session_state.actividades
           )

           if len(st.session_state.actividades)>0 and existe_duplicado:
               # Si ya existe, mostramos una alerta y detenemos el proceso
               st.error(f"⚠️ La actividad '{nombre}' ya existe en la lista. Elige un nombre diferente.")
           else:
               st.session_state.actividades.append(registro)
               st.success("¡Registro agregado satisfactoriamente!")
               
   if st.button("Evaluar actividades!"):
       for actividad in st.session_state.actividades:
           if actividad["Gasto real"] <= actividad["Presupuesto"]:
               actividad["Estado"] = "Gasto está dentro del presupuesto!"
           else:
               actividad["Estado"] = "Presupuesto fue excedido!"
               
       st.success("Las actividades fueron evaluadas!")

   df_actividades = pd.DataFrame(st.session_state.actividades)
   evento = st.dataframe(df_actividades, on_select="rerun", selection_mode="multi-row", width="content")
   st.write("Registros", len(st.session_state.actividades))
   #st.rerun()

   indices_seleccionados = evento.selection.rows

   if indices_seleccionados:
       if st.button("❌ Eliminar filas seleccionadas!", type="primary"):
           st.write("Filas a eliminar: ", len(indices_seleccionados))

           st.session_state.actividades = [ actividad
                                            for i, actividad in enumerate(st.session_state.actividades)
                                            if i not in indices_seleccionados ]
           st.rerun()

elif opcion == "Ejercicio 3":
   st.write("¡Bienvenido al menú Ejercicio 3!")
   st.subheader("Funciones y Programación Funcional")

   tasa   = st.slider("Seleccione la tasa", min_value= 0, max_value= 100, value=10)
   meses  = st.number_input("Ingrese la cantidad de meses", min_value =0, value=0, step=5)

   if st.button("Calcular", type="primary"):
       if len(st.session_state.actividades)>0:
           calcular_retorno = list(map(lambda x: x["Presupuesto"]*(tasa/100)*meses, st.session_state.actividades))

           st.write("##### Listado de retorno esperado por actividad!")
           st.divider()

           for i, actividad in enumerate(st.session_state.actividades):
                  st.write(f"Actividad **{actividad['Nombre']}**   Presupuesto {actividad['Presupuesto']:,.2f};   Tasa {tasa}%;   Meses {meses};   Retorno **{calcular_retorno[i]:,.2f}**")
       else:
           st.warning("!No hay actividades cargadas previamente en el ejercicio 2!")

elif opcion == "Ejercicio 4":
   st.write("¡Bienvenido al menú Ejercicio 4!")
   st.subheader("Programación Orientada a Objetos (POO)")

   if len(st.session_state.actividades)>0:
       for i, var in enumerate(st.session_state.actividades):
           actividad_reg = actividad(var["Nombre"], var["Tipo"], var["Presupuesto"], var["Gasto real"])
           st.write(f"Registro de actividad {i}:    {actividad_reg.nombre}")
           st.write(actividad_reg.mostrar_info())

       
