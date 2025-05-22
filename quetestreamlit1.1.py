import streamlit as st
import datetime
from datetime import datetime, timedelta
# Titre de mon app 
st.title("Bienvenue sur le site web de Hassan")

arron = st.selectbox("Indiquez votre arrondissement de récupération",
             ['Manhattan', 'Queens', 'Aucun', 'Bronx', 'Brooklyn']) 

dic_arron = {'Manhattan' : 'https://www.les-covoyageurs.com/ressources/images-lieux/photo-lieu-1239-1.jpg', 
             'Queens' : 'https://media.routard.com/image/50/8/pont-de-queensboro-entre-manhattan-et-long-island-city.1614508.w630.jpg', 
             'Aucun' : 'https://resize.elle.fr/article_960_webp/var/plain_site/storage/images/loisirs/cinema/news/matrix-quel-est-le-lien-entre-la-saga-culte-et-les-sushis-3977899/95849590-1-fre-FR/Matrix-quel-est-le-lien-entre-la-saga-culte-et-les-sushis.jpg', 
             'Bronx' : 'https://cdn.generationvoyage.fr/2023/09/Vue-aerienne-du-Bronx-1000x667.jpeg', 
             'Brooklyn' : 'https://st.depositphotos.com/1006799/1995/i/950/depositphotos_19954511-stock-photo-manhattan-panorama.jpg'}
imga = dic_arron[arron]

st.write('___')
st.date_input("Sélectionnez votre date de départ")
st.write('___')
t = st.time_input("Sélectionnez votre heure de départ")

st.write('___')

st.write(f'Vous avez choisi : {arron}')
st.write(f'Vous serez attendu à: {t}')
st.image(imga)