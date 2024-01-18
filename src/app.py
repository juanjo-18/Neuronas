import streamlit as st

image_container = st.container()
with image_container:
    st.image('imagenes/fotoNeurona.jpg', width=200)
    st.title("Hola neurona")


tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])


with tab1:
    peso1 = st.slider('Peso W0', 0.00, 5.00, 1.00,key="peso1")
    X0 = st.number_input('Entrada x0',key="x0")
    if st.button('Calcular la salida',key="boton1"):
        calculo1=peso1*X0
        st.write('La salida de la neurona es ',calculo1)
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        peso11 = st.slider('Peso W0', 0.00, 5.00, 1.00, key="peso11")
        X00 = st.number_input('Entrada x0',key="x00")
    with col2:
        peso2 = st.slider('Peso W1', 0.00, 5.00, 1.00, key="peso2")
        X1 = st.number_input('Entrada x1',key="x1")
   
    if st.button('Calcular la salida',key="boton2"):
        calculo2=peso11*X00+peso2*X1
        st.write('La salida de la neurona es ',calculo2)

with tab3:
    col1, col2,col3 = st.columns(3)
    with col1:
        peso111 = st.slider('Peso W0', 0.00, 5.00, 1.00,key="peso111")
        X000 = st.number_input('Entrada x0',key="x000")
    with col2:
        peso22 = st.slider('Peso W1', 0.00, 5.00, 1.00,key="peso22")
        X11 = st.number_input('Entrada x1',key="x11")
    with col3:
        peso3 = st.slider('Peso W2', 0.00, 5.00, 1.00,key="peso3")
        X2 = st.number_input('Entrada x2',key="x2")

    sesgo = st.number_input('Introduzca el valor del sesgo',key="sesgo")
    if st.button('Calcular la salida',key="boton3"):
        calculo3=peso111*X000+peso22*X11+peso3*X2+sesgo
        st.write('La salida de la neurona es ',calculo3)
    
