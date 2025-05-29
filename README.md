# Application Web : Parcs et Jardins de Bruxelles

Cette application web interactive permet de visualiser et d'explorer les parcs et jardins de Bruxelles à l’aide de données ouvertes, tout en intégrant des fonctionnalités de cartographie, d’authentification et de recherche de contenus multimédias.

Développée avec Streamlit, elle démontre la capacité à construire une interface utilisateur moderne, connectée à plusieurs APIs, tout en assurant la gestion des accès et la visualisation de données géolocalisées.

---

## Fonctionnalités principales

- Visualisation cartographique des parcs et jardins via Folium
- Sélection interactive des lieux d’intérêt
- Intégration de vidéos associées à chaque parc via l’API YouTube
- Authentification des utilisateurs avec gestion de rôles
- Exploitation des données ouvertes de la Ville de Bruxelles

---

## Technologies et bibliothèques utilisées

| Technologie / Librairie         | Utilisation principale                                  |
|----------------------------------|----------------------------------------------------------|
| **Streamlit**                   | Développement de l’interface utilisateur                 |
| **Folium**                      | Création de cartes interactives                          |
| **streamlit-folium**           | Intégration native des cartes Folium dans Streamlit      |
| **streamlit-authenticator**    | Gestion de l’authentification utilisateur                |
| **streamlit-option-menu**      | Création d’un menu de navigation interactif              |
| **Pandas**                     | Traitement et manipulation des données tabulaires        |
| **Requests**                   | Appels aux APIs (opendata, YouTube, OpenStreetMap)       |
| **YouTube Data API v3**        | Recherche de vidéos associées aux lieux géographiques    |

---

## Authentification

L'application propose un système d'authentification basé sur deux utilisateurs préconfigurés, avec des rôles distincts :

- Nom d’utilisateur : `utilisateur`, mot de passe : `utilisateurMDP`
- Nom d’utilisateur : `root`, mot de passe : `rootMDP`

---

## Données

Les données géographiques des parcs et jardins proviennent du portail officiel de données ouvertes de la Ville de Bruxelles :  
[https://opendata.brussels.be](https://opendata.brussels.be)

---

## Déploiement

L'application est hébergée sur Streamlit Cloud.

### Extrait du fichier `requirements.txt` :

```txt
streamlit==1.45.1
folium==0.15.1
streamlit-folium==0.18.0
streamlit-authenticator==0.4.2
streamlit-option-menu==0.4.0
pandas
requests
