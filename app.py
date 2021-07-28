import streamlit as st
from multiapp import MultiApp
from apps import main, edsa_recommender  # import your app modules here

app = MultiApp()

st.markdown("""
# Ejemplos de Recomendadores
Navega en el sitio y elije del menu las implementaciones.
""")
# This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
#
# """)

# Add all your application here
app.add_app("Implementacion Propia", main.app)
app.add_app("Dataset de Peliculas", edsa_recommender.app)
# app.add_app("Model", model.app)
# The main app
app.run()
