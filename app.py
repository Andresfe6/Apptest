import streamlit as st
import random

# Título de la aplicación
st.header('Lanzar una moneda')

# Instrucción al usuario
st.write('Haz clic en el botón para lanzar una moneda.')

# Botón para lanzar la moneda
if st.button('Lanzar'):
    # Lógica para lanzar la moneda
    resultado = random.choice(['Cara', 'Cruz'])
    st.write(f'El resultado del lanzamiento es: {resultado}')
else:
    st.write('Haz clic en "Lanzar" para ver el resultado.')