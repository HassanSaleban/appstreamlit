import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# --- Configuration de l'authentification ---
credentials = {
    'usernames': {
        'utilisateur': {
            'name': 'Utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'role': 'utilisateur'
        },
        'root': {
            'name': 'Administrateur',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    credentials,
    cookie_name='streamlit_cookie',
    key='streamlit_key',
    cookie_expiry_days=30
)

# --- Page de connexion ---
name, authentication_status, username = authenticator.login('Connexion', 'main')

if authentication_status:
    # --- Menu principal ---
    selection = option_menu(
        menu_title='Mon menu',
        options=['Accueil', 'Photos', 'Colonnes', 'Sidebar'],
        icons=['house', 'images', 'layout-text-window', 'sidebar-collapse'],
        default_index=0,
        orientation='horizontal'
    )

    if selection == 'Accueil':
        st.write("Bienvenue sur la page d'accueil de mon menu !")

    elif selection == 'Photos':
        st.write("Bienvenue sur mon album photo !")
        cols = st.columns(3)
        urls = [
            'https://static.streamlit.io/examples/cat.jpg',
            'https://static.streamlit.io/examples/dog.jpg',
            'https://static.streamlit.io/examples/owl.jpg'
        ]
        titles = ['A cat', 'A dog', 'An owl']
        for col, title, url in zip(cols, titles, urls):
            with col:
                st.header(title)
                st.image(url)

    elif selection == 'Colonnes':
        st.write("Exemple de répartition de colonnes personnalisée")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.subheader('Colonne 1 (ratio 1)')
            st.write('Contenu de la première colonne')
        with col2:
            st.subheader('Colonne 2 (ratio 2)')
            st.write('Contenu de la deuxième colonne')

    elif selection == 'Sidebar':
        st.write("Exemple d'éléments dans la barre latérale")
        contact = st.sidebar.selectbox(
            "Comment souhaitez-vous être contacté ?",
            ['Email', 'Home phone', 'Mobile phone']
        )
        shipping = st.sidebar.radio(
            "Choisissez un mode de livraison",
            ['Standard (5-15 jours)', 'Express (2-5 jours)']
        )
        st.write(f"Contact via : {contact}")
        st.write(f"Mode de livraison : {shipping}")

    # Bouton de déconnexion
    authenticator.logout('Déconnexion', 'sidebar')

elif authentication_status is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect.")
elif authentication_status is None:
    st.warning("Veuillez renseigner vos identifiants.")
