import streamlit as st
import pandas as pd
# La commande st.checkbox vous permet d’afficher une case à cocher. Plusieurs checkbox peuvent être cocher en même temps.
st.checkbox(label = "Tu es incollable sur l'univers du Roi lion.") # label : paramètre (facultatif à écrire) qui permet d'afficher le contenu associé 
st.write('___')  # Ligne de séparation pour aérer l’interface visuellement.

# La commande radio permet à l'utilisateur de choisir UNE seule réponse parmi plusieurs propositions.
st.radio("Est-ce que Le Roi lion est le meilleur Disney ?", 
         ['Oui !', 'Evidemment !', 'La question ne se pose même pas.']) #Les réponses possibles sont stockées dans une liste 
st.write('___')

# Un interrupteur (toggle). Il s’agit d’un bouton on/off. 
st.toggle("Tu as vu Le Roi lion", value=True) #Ici, il est activé par défaut (value=True).
st.write('___')

# Un menu déroulant où l'utilisateur peut sélectionner une seule option.
st.selectbox("Qui a tué Mufasa ?",
             ['Simba', 'Scar', 'Zazu']) 
st.write('___')

# Une liste à choix multiples. L’utilisateur peut sélectionner plusieurs réponses à la fois.
st.multiselect("Quels sont vos personnages favoris ?", 
               ['Simba', 'Mufasa', 'Scar', 'Nala']) 
st.write('___')

# Un curseur avec des valeurs textuelles. L’utilisateur choisit son appréciation du film.
st.select_slider("Donnez votre appréciation sur le Roi lion", 
                 ['Mauvais', 'Bon', 'Excellent'], 
                 value='Excellent') # Paramètre permettant de positiionner le curseur par défaut sur "Excellent"

