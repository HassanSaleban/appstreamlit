
import streamlit as st
import pandas as pd
# Titre principal de l'application (affiché en haut de la page)
st.title("Ou Manger")

# Titre de section important (taille 1)
st.header("Il est important de bien manger pour rester en bonne santé")

# Sous-titre (taille 2), utile pour organiser le contenu par sous-sections
st.subheader("ALLONS Y")



# Affiche une ligne de texte simple (sans mise en forme particulière)
st.text("Dis nous ou tu manges habituellement")

# Affiche du texte avec mise en forme Markdown
st.markdown(''':rainbow: :blue-background[mon test]''')  # Ici, un effet arc-en-ciel est appliqué

# Affiche un dataframe (st.write accepte plusieurs arguments et plusieurs types de données)
st.write(
    pd.DataFrame({
            "restaurant": ['Pepe chicken', 'Break dej', 'Kebab', 'Food truck'],
            "Score": [0, 1, 0, 3]}
    )
)

if st.button("Ajouter"):
    st.write("+1")